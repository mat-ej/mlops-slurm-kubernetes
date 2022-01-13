# How to run ploomber pipelines on a local k8s cluster

prerequisites: kubectl, docker.

NOTE: see Dockerfile for installation if missing. 

## set up local k8s
install k3d

    curl -s https://raw.githubusercontent.com/rancher/k3d/main/install.sh | bash

create cluster

    k3d cluster create mycluster

    #optional: export config into a default location
    k3d kubeconfig get mycluster > ~/.kube/config
    export KUBECONFIG=~/.kube/config
    
    # check cluster
    kubectl get nodes

wait for cluster to deploy all the required pods. (status = "Running")

## deploy argo to local k8s
    kubectl create ns argo
    kubectl apply -n argo -f argo-pns.yaml

    # check argo pods (once they're all running, argo is ready)
    kubectl get pods -n argo

## set up argo cli
    curl -sLO https://github.com/argoproj/argo-workflows/releases/download/v3.2.6/argo-linux-amd64.gz
    gunzip argo-linux-amd64.gz
    chmod +x argo-linux-amd64
    mv ./argo-linux-amd64 /usr/local/bin/argo
    argo version
    
    #test argo with hello world pipeline
    argo submit -n argo --watch https://raw.githubusercontent.com/argoproj/argo-workflows/master/examples/hello-world.yaml


NOTE: argo command requires KUBECONFIG env var to point to a correct config e.g.: ~/.kube/config

#### optional: port forward into argo

    # port forwarding to enable the UI
    kubectl -n argo port-forward svc/argo-server 2746:2746

Then, open: https://127.0.0.1:2746

# Ploomber project set up
See ../ploomber.md to set up conda environment

    #make folder for pipeline outputs
    export SHARED_DIR=$HOME/ploomber-k8s
    mkdir -p $SHARED_DIR

    conda activate ploomber39
    # optional remove existing project cloned from github
    rm -rf ml-intermediate

    # generate example from one of the template projects
    ploomber examples -n templates/ml-intermediate -o ml-intermediate
    cd ml-intermediate
    
    # configure development environment
    cp environment.yml environment.lock.yml
    pip install -r requirements.txt

## set up argo as executor
create template file soopervisor.yaml where executor config is 

    soopervisor add training --backend argo-workflows

set up soopervisor.yaml or use one from this repo

    cp ../soopervisor-k8s.yaml soopervisor.yaml
    cp ../env-k8s.yaml env.yaml


### run pipeline on argo

    # build docker image (takes a few minutes the first time) and generate an argo's yaml spec
    soopervisor export training --skip-tests --mode force
    
    # import image to the k8s cluster
    k3d image import ml-intermediate:latest --cluster mycluster 
    
    # submit workflow
    argo submit -n argo --watch training/argo.yaml

### clean up cluster    

    k3d cluster delete mycluster
    

NOTE:
--mode force is to force re run of tasks, if pipeline already ran, some steps would be skipped. 