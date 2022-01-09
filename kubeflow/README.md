# kubeflow-docs
Short tutorial on how to use Kubeflow on kubeflow.cerit-sc.cz.

Includes working examples and also examples currently in development.


# Local development
Best way(that I found) tu run kubeflow locally is to use k3s in combination with K3ai:

[https://k3s.io/](https://k3s.io/)

[https://docs.k3ai.in/](https://docs.k3ai.in/)

with your .kube/config correctly set you can simply apply the component that you wish to use. E.g.

`k3ai apply -g kubeflow-pipelines-traefik`

# Cerit cluster

[https://kubeflow.cerit-sc.cz/](https://kubeflow.cerit-sc.cz/)


# Examples
I found the following github to be the most useful resource for learning Kubeflow. 
`https://github.com/kubeflow/pipelines/tree/master/samples`

The "official" repo is quite difficult to navigate as many of the examples work only with the use of Google Cloud or AWS. The examples included here are mostly selected out of that repo, with the intetion that they should work without the need for Google cloud or any other paid solution.


There are multiple ways to run the examples. The jupyter ones are easily run directly from a notebook server inside kubeflow.

`https://kubeflow.cerit-sc.cz/_/jupyter/?ns=uhrinmat`

where **ns** points to your assigned namespace(usually a school ID).


The pure python ones can be compiled into a .yaml and uploaded.

```
import kfp
kfp.compiler.Compiler().compile(pipeline, pipeline_path)
```


Or you can directly connect to the Cerit kubeflow using a cookie, process best explained in one of the examples: [here](in-development/pytorch-samples/Pipeline-Bert.ipynb).

```
INGRESS_GATEWAY='http://istio-ingressgateway.istio-system.svc.cluster.local'
AUTH="<enter your token here>"
COOKIE="authservice_session="+AUTH
client = kfp.Client(host=INGRESS_GATEWAY+"/pipeline", cookies=COOKIE)
```

**Note**: The cookie authentication so far seems to work only from within cluster

# Contact
Should you need additional help, want to cooperate or add your own working example, dont hesitate to contact me:

uhrinmat`<at>`fel.cvut.cz 
# Additional resources
[https://kubeflow-pipelines.readthedocs.io/en/latest/index.html](https://kubeflow-pipelines.readthedocs.io/en/latest/index.html)


# Additional Notes
**Note**: Replace uhrinmat everywhere with your respective Kubeflow namespace.



