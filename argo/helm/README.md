# install argo on k8s
    helm repo add bitnami https://charts.bitnami.com/bitnami
    helm repo update

    helm install my-release bitnami/argo-workflows