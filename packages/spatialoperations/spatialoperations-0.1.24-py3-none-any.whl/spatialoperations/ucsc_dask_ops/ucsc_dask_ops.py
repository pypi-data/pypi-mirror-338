import time
import logging
import datetime
from pydantic import BaseModel, Field
import pytimeparse
from typing import Optional, Dict, Any, cast, List
from kubernetes import client, config
from kubernetes.client import ApiException
from dask.distributed import Client
from dask_cluster_json import DaskClusterJson, PVCJson

ONE_WEEK_IN_SECONDS = 604800

class WorkerSpec(BaseModel):
    replicas: int

class DaskClusterSpec(BaseModel):
    worker: WorkerSpec

class DaskService(BaseModel):
    worker: WorkerSpec

class DaskClusterMetadata(BaseModel):
    name: str
    namespace: str

class DaskCluster(BaseModel):
    kind: str
    apiVersion: str
    metadata: DaskClusterMetadata
    spec: DaskClusterSpec
    class Config:
        extra = "allow"

class V1ServicePort(BaseModel):
    port: int
    target_port: Optional[Any] = None
    protocol: Optional[str] = "TCP"
    name: Optional[str] = None
    node_port: Optional[int] = None

class V1ServiceSpec(BaseModel):
    ports: List[V1ServicePort]
    selector: Optional[Dict[str, str]] = None
    cluster_ip: Optional[str] = Field(None, alias="clusterIP")
    type: Optional[str] = "ClusterIP"
    external_name: Optional[str] = Field(None, alias="externalName")
    session_affinity: Optional[str] = Field(None, alias="sessionAffinity")
    external_traffic_policy: Optional[str] = Field(None, alias="externalTrafficPolicy")

class V1ObjectMeta(BaseModel):
    name: str
    namespace: Optional[str] = None
    labels: Optional[Dict[str, str]] = None
    annotations: Optional[Dict[str, str]] = None
    generation: Optional[int] = None
    resource_version: Optional[str] = Field(None, alias="resourceVersion")
    uid: Optional[str] = None
    creation_timestamp: Optional[str] = Field(None, alias="creationTimestamp")

class V1Service(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = "Service"
    metadata: V1ObjectMeta
    spec: V1ServiceSpec
    status: Optional[Dict[str, Any]] = None

    class Config:
        allow_population_by_field_name = True
        extra = "allow"

class V1PersistentVolumeClaimResources(BaseModel):
    requests: Dict[str, str]

class V1PersistentVolumeClaimSpec(BaseModel):
    access_modes: List[str] = Field([], alias="accessModes")
    resources: V1PersistentVolumeClaimResources
    storage_class_name: Optional[str] = Field(None, alias="storageClassName")

class V1PersistentVolumeClaim(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = "PersistentVolumeClaim"
    metadata: V1ObjectMeta
    spec: V1PersistentVolumeClaimSpec
    status: Optional[Dict[str, Any]] = None

    class Config:
        allow_population_by_field_name = True
        extra = "allow"


class UCSC_DaskOps:
    """
    A Python client for creating and managing dedicated Dask clusters on Kubernetes.

    This class utilizes the DaskCluster custom resource to create and manage
    Dask clusters on Kubernetes in a user-friendly way. It also supports creating
    and using persistent volumes for shared storage between workers.

    Example without persistent storage:
        ```python
        import ucsc_dask_ops

        dask_ops = UCSC_DaskOps(
            id="my-cluster",
            num_workers=100,
            cluster_timeout='3days'
        )

        # Get a Dask client to interact with the cluster
        client = dask_ops.get_client()

        # When finished
        dask_ops.shutdown()
        ```

    Example with persistent storage:
        ```python
        import ucsc_dask_ops

        # Create a cluster with a persistent volume
        dask_ops = UCSC_DaskOps(
            id="my-cluster",
            num_workers=100,
            cluster_timeout='3days',
            use_pvc=True,
            pvc_size="50Gi",
            pvc_mount_path="/data"
        )

        # Get a client to interact with the cluster
        client = dask_ops.get_client()

        # Files saved to /data will persist across cluster restarts

        # When finished, the PVC will be removed upon shutdown
        dask_ops.shutdown()
        ```
    """

    def __init__(
        self,
        id: str,
        num_workers: int = 20,
        cluster_timeout: str = "6 hours",
        namespace: str = "ucsc-vizlab",
        image: str = "gitlab-registry.nrp-nautilus.io/ucsc-vizlab/spatialops/dask:latest",
        image_pull_secrets: List[Dict[str, str]] = [{"name": "ucsc-vizlab-container-registry"}],
        scheduler_port: int = 8786,
        dashboard_port: int = 8787,
        worker_resources: Optional[Dict[str, Dict[str, str]]] = None,
        scheduler_resources: Optional[Dict[str, Dict[str, str]]] = None,
        use_pvc: bool = False,
        pvc_size: str = "10Gi",
        pvc_mount_path: str = "/shared-data",
        pvc_name: str | None = None
    ):
        """
        Initialize a UCSC_DaskOps instance.

        Args:
            cluster_timeout: How long the cluster should live before auto-shutdown (max "1 week")
            dashboard_port: Port for the Dask dashboard
            id: A unique identifier for the cluster
            image: Docker image for the Dask scheduler
            namespace: Kubernetes namespace to deploy the cluster
            num_workers: Number of worker pods to create (1-500)
            scheduler_port: Port for scheduler communication
            scheduler_resources: Resource requests/limits for scheduler pod
            worker_resources: Resource requests/limits for worker pods
            use_pvc: Whether to create and use a PersistentVolumeClaim
            pvc_size: Size of the persistent volume (e.g. "10Gi")
            pvc_mount_path: Path where the volume will be mounted in containers
            pvc_name: Override for the volume name. If this volume already
            exists it will be mounted but not created nor destroyed
        """
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger("UCSC_DaskOps")

        if not 1 <= num_workers <= 500:
            raise ValueError("num_workers must be between 1 and 500")

        timeout_seconds = pytimeparse.parse(cluster_timeout)
        if timeout_seconds is None:
            raise ValueError(f"Invalid cluster_timeout format: {cluster_timeout}")
        timeout_seconds = int(timeout_seconds)

        if int(timeout_seconds) > ONE_WEEK_IN_SECONDS:
            raise ValueError(f"cluster_timeout cannot exceed 1 week")
        kill_at = int(time.time() + timeout_seconds)

        self.cluster_name = f"dask-{id}"
        self.num_workers = num_workers
        self.namespace = namespace
        self.scheduler_port = scheduler_port
        self.dashboard_port = dashboard_port
        self.use_pvc = use_pvc
        self.pvc_mount_path = pvc_mount_path
        self.pvc_spec = None
        self.volume_mounts = None
        self.volumes = None
        self.owns_pvc = not pvc_name
        self.pvc_name = pvc_name or f"{self.cluster_name}-data"

        if self.use_pvc:
            self.pvc_spec = PVCJson(
                kill_at=kill_at,
                name=self.pvc_name,
                namespace=self.namespace,
                size=pvc_size,
                labels={
                    "app.kubernetes.io/name": "dask",
                    "app.kubernetes.io/instance": id
                }
            ).spec

            # Configure volume mounts and volumes for the Dask cluster
            self.volume_mounts = [
                {
                    "name": "shared-data",
                    "mountPath": self.pvc_mount_path
                }
            ]

            self.volumes = [
                {
                    "name": "shared-data",
                    "persistentVolumeClaim": {
                        "claimName": self.pvc_name
                    }
                }
            ]

        # Create DaskCluster spec
        self.cluster_spec = DaskClusterJson(
            id=id,
            cluster_name=self.cluster_name,
            dashboard_port=dashboard_port,
            kill_at=kill_at,
            image=image,
            image_pull_secrets=image_pull_secrets,
            namespace=self.namespace,
            num_workers=self.num_workers,
            scheduler_port=scheduler_port,
            worker_resources=worker_resources or {
                "requests": {"cpu": "400m", "memory": "16Gi"},
                "limits": {"cpu": "1600m", "memory": "32Gi"}
            },
            scheduler_resources=scheduler_resources or {
                "requests": {"cpu": "400m", "memory": "16Gi"},
                "limits": {"cpu": "1600m", "memory": "32Gi"}
            },
            volume_mounts=self.volume_mounts,
            volumes=self.volumes
        ).spec

        self.shutdown_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout_seconds)

        config.load_kube_config()
        self.logger.info("Loaded local kubeconfig")

        self.core_api = client.CoreV1Api()
        self.custom_api = client.CustomObjectsApi()

        self._dask_client = None
        self._scheduler_address = None

        if self.use_pvc and not self._pvc_exists():
            self._create_pvc()

        if self._cluster_exists():
            self.logger.info(f"Connecting to existing Dask cluster: {self.cluster_name}")
            if self._get_worker_count() != self.num_workers:
                self.logger.info(f"Updating worker count from {self._get_worker_count()} to {self.num_workers}")
                self._update_worker_count()
        else:
            self.logger.info(f"Creating new Dask cluster: {self.cluster_name}")
            self._create_cluster()

    def _cluster_exists(self) -> bool:
        """
        Check if a DaskCluster with the given ID already exists.

        Returns:
            True if the cluster exists, False otherwise.
        """
        try:
            self.custom_api.get_namespaced_custom_object(
                group="kubernetes.dask.org",
                version="v1",
                namespace=self.namespace,
                plural="daskclusters",
                name=self.cluster_name
            )
            return True
        except ApiException as e:
            if e.status == 404:
                return False
            else:
                self.logger.error(f"Error checking for existing cluster: {e}")
                raise

    def _get_cluster(self)  -> DaskCluster:
        try:
            cluster = cast(Dict[str, Any], self.custom_api.get_namespaced_custom_object(
                group="kubernetes.dask.org",
                version="v1",
                namespace=self.namespace,
                plural="daskclusters",
                name=self.cluster_name
            ))
            assert(isinstance(cluster, dict))
            return DaskCluster(**cluster)
        except ApiException as e:
            self.logger.error(f"Error getting cluster: {e}")
            raise

    def _get_scheduler_service(self):
        service_name = f"{self.cluster_name}-scheduler"
        try:
            service = self.core_api.read_namespaced_service(
                name=service_name,
                namespace=self.namespace
            )
            assert isinstance(service, client.V1Service)  # Runtime check
            return service
        except ApiException as e:
            self.logger.error(f"Error getting service: {e}")
            raise

    def _get_worker_count(self) -> int:
        """
        Get the current number of workers in the cluster.

        Returns:
            The current number of worker replicas.
        """
        return self._get_cluster().spec.worker.replicas

    def _update_worker_count(self) -> None:
        """Update the number of workers in an existing cluster."""
        try:
            cluster = self._get_cluster()
            cluster.spec.worker.replicas = self.num_workers
            self.custom_api.patch_namespaced_custom_object(
                group="kubernetes.dask.org",
                version="v1",
                namespace=self.namespace,
                plural="daskclusters",
                name=self.cluster_name,
                body=cluster
            )

            self.logger.info(f"Updated worker count to {self.num_workers}")
        except ApiException as e:
            self.logger.error(f"Error updating worker count: {e}")
            raise

    def _create_cluster(self) -> None:
        """Create a new Dask cluster using the DaskCluster CRD."""
        try:
            self.custom_api.create_namespaced_custom_object(
                group="kubernetes.dask.org",
                version="v1",
                namespace=self.namespace,
                plural="daskclusters",
                body=self.cluster_spec
            )

            self._wait_for_scheduler()

            self.logger.info(f"Created Dask cluster: {self.cluster_name}")
        except ApiException as e:
            self.logger.error(f"Error creating cluster: {e}")
            raise

    def _generate_random_string(self, length: int) -> str:
        """Generate a random alphanumeric string of specified length."""
        import random
        import string
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def _wait_for_scheduler(self, timeout: int = 120) -> None:
        """
        Wait for the scheduler service to be ready.

        Args:
            timeout: Maximum time to wait in seconds

        Raises:
            TimeoutError: If the scheduler is not ready within the timeout period
        """
        start_time = time.time()
        self.logger.info(f"Waiting for scheduler service to be ready...")

        while time.time() - start_time < timeout:
            try:
                service = self._get_scheduler_service()
                assert service.spec != None
                assert service.status != None

                if service.spec.type == "LoadBalancer":
                    if service.status.load_balancer.ingress:
                        ingress = service.status.load_balancer.ingress[0]
                        ip = ingress.ip or ingress.hostname
                        if ip:
                            self._scheduler_address = f"{ip}:{self.scheduler_port}"
                            self._dashboard_addess = f"https://{ip}:{self.dashboard_port}"
                            self.logger.info(f"Scheduler is ready at {self._scheduler_address}")
                            self.logger.info(f"👀 Dashboard will be live shortly at {self._dashboard_addess}")
                            return
                else:
                    cluster_ip = service.spec.cluster_ip
                    if cluster_ip:
                        self._scheduler_address = f"{cluster_ip}:{self.scheduler_port}"
                        self.logger.info(f"Scheduler is ready at {self._scheduler_address}")
                        return

            except ApiException as e:
                if e.status != 404:
                    self.logger.warning(f"Error checking scheduler service: {e}")

            time.sleep(5)

        raise TimeoutError(f"Scheduler service not ready after {timeout} seconds")

    def _get_scheduler_address(self) -> str:
        """
        Get the address of the Dask scheduler.

        Returns:
            The scheduler address in the format "host:port"
        """
        if self._scheduler_address:
            return self._scheduler_address

        try:
            service = self._get_scheduler_service()
            assert service.spec != None
            assert service.status != None

            if service.spec.type == "LoadBalancer" and service.status.load_balancer.ingress:
                ingress = service.status.load_balancer.ingress[0]
                host = ingress.ip or ingress.hostname
            else:
                host = service.spec.cluster_ip

            for port in service.spec.ports:
                if port.name == "tcp-comm":
                    self._scheduler_address = f"{host}:{port.port}"
                    return self._scheduler_address

            raise ValueError(f"Could not find scheduler port in service")

        except ApiException as e:
            self.logger.error(f"Error getting scheduler address: {e}")
            raise

    def get_client(self) -> Client:
        """
        Get a Dask client connected to the cluster.

        Returns:
            A Dask client object
        """
        if self._dask_client is None:
            scheduler_address = self._get_scheduler_address()
            self.logger.info(f"Connecting to Dask scheduler at {scheduler_address}")
            self._dask_client = Client(f"tcp://{scheduler_address}")

        return self._dask_client

    def _pvc_exists(self) -> bool:
        """
        Check if a PersistentVolumeClaim with the given name already exists.

        Returns:
            True if the PVC exists, False otherwise.
        """
        try:
            self.core_api.read_namespaced_persistent_volume_claim(
                name=self.pvc_name,
                namespace=self.namespace
            )
            return True
        except ApiException as e:
            if e.status == 404:
                return False
            else:
                self.logger.error(f"Error checking for existing PVC: {e}")
                raise

    def _create_pvc(self) -> None:
        """Create a new PersistentVolumeClaim."""
        if not self.pvc_spec:
            self.logger.warning("No PVC spec defined, skipping PVC creation")
            return

        try:
            self.logger.info(f"Creating PersistentVolumeClaim: {self.pvc_name}")
            self.core_api.create_namespaced_persistent_volume_claim(
                namespace=self.namespace,
                body=self.pvc_spec
            )
            self.logger.info(f"Created PVC: {self.pvc_name}")
        except ApiException as e:
            if e.status == 409:  # Conflict (already exists)
                self.logger.info(f"PVC {self.pvc_name} already exists")
            else:
                self.logger.error(f"Error creating PVC: {e}")
                raise

    def _delete_pvc(self) -> None:
        """Delete the PersistentVolumeClaim."""
        if not self.use_pvc or not self.owns_pvc:
            return

        try:
            self.logger.info(f"Deleting PVC: {self.pvc_name}")
            self.core_api.delete_namespaced_persistent_volume_claim(
                name=self.pvc_name,
                namespace=self.namespace
            )
            self.logger.info(f"Deleted PVC: {self.pvc_name}")
        except ApiException as e:
            if e.status == 404:
                self.logger.info(f"PVC {self.pvc_name} already deleted")
            else:
                self.logger.error(f"Error deleting PVC: {e}")
                raise

    def shutdown(self) -> None:
        """
        Shut down the Dask cluster and delete the optional associated PVC.
        """
        if self._dask_client:
            self.logger.info("Closing Dask client connection")
            self._dask_client.close()
            self._dask_client = None

        try:
            self.logger.info(f"Deleting Dask cluster: {self.cluster_name}")
            self.custom_api.delete_namespaced_custom_object(
                group="kubernetes.dask.org",
                version="v1",
                namespace=self.namespace,
                plural="daskclusters",
                name=self.cluster_name
            )
        except ApiException as e:
            if e.status == 404:
                self.logger.info(f"Cluster {self.cluster_name} already deleted")
            else:
                self.logger.error(f"Error deleting cluster: {e}")
                raise

        if self.use_pvc:
            self._delete_pvc()
