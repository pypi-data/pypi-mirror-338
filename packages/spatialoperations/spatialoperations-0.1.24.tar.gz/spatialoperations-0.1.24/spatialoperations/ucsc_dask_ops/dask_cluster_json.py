import random
import string
from typing import Dict, List, Optional, Any

class PVCJson:
    """
    Generate a JSON representation of a Kubernetes PersistentVolumeClaim.

    This class creates a dictionary that represents a Kubernetes PVC,
    which can be used to create persistent storage for Dask clusters.
    """

    def __init__(self,
                 kill_at: int,
                 name: str,
                 namespace: str,
                 size: str = "10Gi",
                 storage_class_name: str = "rook-cephfs",
                 annotations: Optional[Dict[str, str]] = None,
                 labels: Dict[str, str] = {}):
        """
        Initialize a PVCJson instance.

        Args:
            name: Name for the PVC
            namespace: Kubernetes namespace to deploy the PVC
            size: Size of the persistent volume (e.g. "10Gi")
            storage_class_name: Name of the storage class to use
            annotations: Optional annotations to add to the PVC
            labels: Optional labels to add to the PVC
        """
        labels["kill-at"] = str(kill_at)
        self.spec = {
            "apiVersion": "v1",
            "kind": "PersistentVolumeClaim",
            "metadata": {
                "name": name,
                "namespace": namespace,
                "labels": labels
            },
            "spec": {
                "accessModes": ["ReadWriteMany"],
                "resources": {
                    "requests": {
                        "storage": size
                    }
                },
                "storageClassName": storage_class_name
            }
        }

        if annotations:
            self.spec["metadata"]["annotations"] = annotations


class DaskClusterJson:
    def __init__(self,
                 cluster_name,
                 dashboard_port,
                 id,
                 image,
                 image_pull_secrets,
                 kill_at,
                 namespace,
                 num_workers,
                 scheduler_resources,
                 scheduler_port,
                 worker_resources,
                 volume_mounts: Optional[List[Dict[str, Any]]] = None,
                 volumes: Optional[List[Dict[str, Any]]] = None):
        self.spec = {
            "apiVersion": "kubernetes.dask.org/v1",
            "kind": "DaskCluster",
            "namespace": namespace,
            "metadata": {
                "name": cluster_name,
                "labels": {
                    "app.kubernetes.io/name": "dask",
                    "app.kubernetes.io/instance": id,
                    "kill-at": str(kill_at),
                }
            },
            "spec": {
                "worker": {
                    "metadata": {
                        "annotations": {
                            "rollme": self._generate_random_string(5)
                        }
                    },
                    "replicas": num_workers,
                    "spec": {
                        "imagePullSecrets": image_pull_secrets,
                        "containers": [
                            {
                                "name": "worker",
                                "image": image,
                                "args": [
                                    "conda", "run", "-n", "geospatial-analysis-environment",
                                    "dask", "worker", "--name", "$(DASK_WORKER_NAME)",
                                    "--dashboard", "--dashboard-address", str(dashboard_port)
                                ],
                                "ports": [
                                    {
                                        "name": "http-dashboard",
                                        "containerPort": dashboard_port,
                                        "protocol": "TCP"
                                    }
                                ],
                                "resources": worker_resources,
                                "env": [
                                    {
                                        "name": "AWS_ENDPOINT_URL",
                                        "valueFrom": {
                                            "secretKeyRef": {
                                                "name": "aws-secret",
                                                "key": "AWS_ENDPOINT_URL"
                                            }
                                        }
                                    },
                                    {
                                        "name": "AWS_ACCESS_KEY_ID",
                                        "valueFrom": {
                                            "secretKeyRef": {
                                                "name": "aws-secret",
                                                "key": "AWS_ACCESS_KEY_ID"
                                            }
                                        }
                                    },
                                    {
                                        "name": "AWS_SECRET_ACCESS_KEY",
                                        "valueFrom": {
                                            "secretKeyRef": {
                                                "name": "aws-secret",
                                                "key": "AWS_SECRET_ACCESS_KEY"
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "scheduler": {
                    "metadata": {
                        "annotations": {
                            "rollme": self._generate_random_string(5)
                        }
                    },
                    "spec": {
                        "imagePullSecrets": image_pull_secrets,
                        "containers": [
                            {
                                "name": "scheduler",
                                "image": image,
                                "imagePullPolicy": "Always",
                                "args": [
                                    "conda", "run", "-n", "geospatial-analysis-environment",
                                    "dask", "scheduler"
                                ],
                                "ports": [
                                    {
                                        "name": "tcp-comm",
                                        "containerPort": scheduler_port,
                                        "protocol": "TCP"
                                    },
                                    {
                                        "name": "http-dashboard",
                                        "containerPort": dashboard_port,
                                        "protocol": "TCP"
                                    }
                                ],
                                "readinessProbe": {
                                    "httpGet": {
                                        "port": "http-dashboard",
                                        "path": "/health"
                                    },
                                    "initialDelaySeconds": 5,
                                    "periodSeconds": 10
                                },
                                "livenessProbe": {
                                    "httpGet": {
                                        "port": "http-dashboard",
                                        "path": "/health"
                                    },
                                    "initialDelaySeconds": 15,
                                    "periodSeconds": 20
                                },
                                "resources": scheduler_resources,
                                "env": [
                                    {
                                        "name": "AWS_ENDPOINT_URL",
                                        "valueFrom": {
                                            "secretKeyRef": {
                                                "name": "aws-secret",
                                                "key": "AWS_ENDPOINT_URL"
                                            }
                                        }
                                    },
                                    {
                                        "name": "AWS_ACCESS_KEY_ID",
                                        "valueFrom": {
                                            "secretKeyRef": {
                                                "name": "aws-secret",
                                                "key": "AWS_ACCESS_KEY_ID"
                                            }
                                        }
                                    },
                                    {
                                        "name": "AWS_SECRET_ACCESS_KEY",
                                        "valueFrom": {
                                            "secretKeyRef": {
                                                "name": "aws-secret",
                                                "key": "AWS_SECRET_ACCESS_KEY"
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    "service": {
                        "type": "LoadBalancer",
                        "selector": {
                            "dask.org/component": "scheduler",
                            "app.kubernetes.io/name": "dask",
                            "app.kubernetes.io/instance": id
                        },
                        "ports": [
                            {
                                "name": "tcp-comm",
                                "protocol": "TCP",
                                "port": scheduler_port,
                                "targetPort": "tcp-comm"
                            },
                            {
                                "name": "http-dashboard",
                                "protocol": "TCP",
                                "port": dashboard_port,
                                "targetPort": "http-dashboard"
                            }
                        ]
                    }
                }
            }
        }

        # Add volume mounts to containers if provided
        if volume_mounts:
            # Add to worker container
            worker_container = self.spec["spec"]["worker"]["spec"]["containers"][0]
            worker_container["volumeMounts"] = volume_mounts

            # Add to scheduler container
            scheduler_container = self.spec["spec"]["scheduler"]["spec"]["containers"][0]
            scheduler_container["volumeMounts"] = volume_mounts

        # Add volumes to pod specs if provided
        if volumes:
            # Add to worker spec
            self.spec["spec"]["worker"]["spec"]["volumes"] = volumes

            # Add to scheduler spec
            self.spec["spec"]["scheduler"]["spec"]["volumes"] = volumes

    def _generate_random_string(self, length: int) -> str:
        """Generate a random alphanumeric string of specified length."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
