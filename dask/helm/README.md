# Dask set up

## set up pvc
    kubectl apply -f pvc.yaml

## set up values.yaml

## install helm chart
    helm repo add dask https://helm.dask.org/
    helm repo update
    helm install my-dask dask/dask
    kubectl describe