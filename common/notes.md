# useful docker commands
    docker kill $(docker ps -q)
    docker rm $(docker ps -a -q)

# Installation of kubectl 
#TODO

# Argo
### argo workflows env variables.
    kubectl create ns argo
    kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/stable/manifests/install.yaml

    export ARGO_SERVER='127.0.0.1:2746' 
    export ARGO_HTTP1=true  
    export ARGO_SECURE=true
    export ARGO_BASE_HREF=
    export ARGO_TOKEN='' 
    export ARGO_NAMESPACE=argo
    export ARGO_INSECURE_SKIP_VERIFY=true
    export KUBECONFIG=/dev/null


### argo executor set up
https://argoproj.github.io/argo-workflows/workflow-executors/

    kubectl edit configmap/workflow-controller-configmap -n argo




# Install k3ai
    curl -sfL https://get.k3ai.in | sh -
    k3ai up
    
provide personal auth token from github, read repo privileges are required

    k3ai cluster deploy -t k3s -n local

set up KUBECONFIG env variable:
    
    cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
    export KUBECONFIG=~/.kube/config

verify that the cluster is up and running.
    
    kubectl get node


