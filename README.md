# MLops review 
MLops tools review focused on pipeline execution using multiple clusters: slurm, kubernetes, dask...

Working examples so far:
1. **Ploomber pipelines** - runs on Slurm, K8s, Airflow, Kubeflow(in progress), no complex DAGs with loops/recursions yet.
   1. Kubernetes - example runs pipeline on local k8s using argo
   2. Slurm - example transforms pipeline using a script into batch jobs
   
```
    For example, since we want the tasks to run in the conda environment we created, edit the template.sh so it looks like this:

    #!/bin/bash
    #SBATCH --job-name={{name}}
    #SBATCH --output=result.out
    #
    
    # activate myenv
    conda activate myenv
    srun {{command}}
```

2. **Nextflow** - runs very well on K8s, Slurm, Dask and many others, not focused on ML and hence not ML friendly. No complex DAGs with loops. 

   [http://docs.cerit.io/docs/nextflow.html](http://docs.cerit.io/docs/nextflow.html)


3. **Kubeflow pipelines** - runs on K8s, supports complex DAGs with loops and recursions, running on slurm would require additional development

   [http://docs.cerit.io/docs/kubeflow.html](http://docs.cerit.io/docs/kubeflow.html)


