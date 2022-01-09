# NextFlow-on-Kubernetes

In case of K8s, workflow controller is run as a Pod in Kubernetes cluster. 
Its task is to run worker pods according to pipeline definition. The workflow controller pod has some generated name like naughty-williams. 
The workers have hashed names like nf-81dae79db8e5e2c7a7c3ad5f6c7d59c6.

# Requirements

Installed kubectl with configuration file. (https://cerit-sc.github.io/kube-docs/docs/kubectl.html)

Kubernetes Namespace to run in. (https://cerit-sc.github.io/kube-docs/docs/ns.html)

Created PVC. (https://cerit-sc.github.io/kube-docs/docs/pvc.html)

# Nextflow Installation
To install Nextflow enter this command in your terminal:

    curl -s https://get.nextflow.io | bash
    
You can install specific Nextflow version exporting NXF_VER environment variable before running the install command, e.g.:

    export NXF_VER=20.10.0
    curl -s https://get.nextflow.io | bash

# Running Nextflow

Running the Nextflow in Kubernetes requires local configuration. You can download nextflow.config (https://cerit-sc.github.io/kube-docs/docs/deployments/nextflow.config) which can be used as is in the case, you change namespace to correct value and specify launchDir and workDir to point somewhere on the PVC. Take care, if running Nextflow in parallel, always use different launchDir and workDir for the parallel runs.
You need to keep the file in the current directory where the nextflow command is run and it has to be named nextflow.config.
To instruct the Nextflow to run the hello pipeline in Kubernetes, you can run the following command:

    nextflow kuberun hello -pod-image 'cerit.io/nextflow:21.09.1' -v PVC:/mnt 
 
where PVC is name of the PVC as discussed above. It will be mounted as /mnt. You should use this mount point as some pipelines expect this location.

If everything was correct then you should see output like this:

    Pod started: naughty-williams
    N E X T F L O W  ~  version 21.09.0-SNAPSHOT
    Launching `nextflow-io/hello` [naughty-williams] - revision: e6d9427e5b [master]
    [f0/ce818c] Submitted process > sayHello (2)
    [8a/8b278f] Submitted process > sayHello (1)
    [5f/a4395f] Submitted process > sayHello (3)
    [97/71a2e0] Submitted process > sayHello (4)
    Ciao world!
    Hola world!
    Bonjour world!
    Hello world!
