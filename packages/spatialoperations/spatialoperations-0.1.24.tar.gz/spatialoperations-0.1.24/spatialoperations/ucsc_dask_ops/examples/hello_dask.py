from ucsc_dask_ops import UCSC_DaskOps

dask_ops = UCSC_DaskOps(
    id="my-notebook-cluster",  # Choose a unique name\n",
    num_workers=5,             # Start with 5 workers\n",
    cluster_timeout="1 hour",   # Auto-shutdown after 1 hour\n",
    use_pvc=True,
    pvc_name="jcm-dask-shared-data-pvc"
)

# Get a Dask client to interact with the cluster
client = dask_ops.get_client()

# When finished. If this is skipped then the cluster will be killed after the
# `cluster_timeout` has elapsed.
dask_ops.shutdown()
