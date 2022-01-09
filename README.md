# MLops review 
MLops tools review focused on execution using multiple cluster types: slurm, kubernetes, dask...

Examples so far:
1. **Ploomber pipelines** - able to run on Slurm, K8s, Airflow, Kubeflow(in progress)
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
2. **Kubeflow pipelines** - runs on K8s, supports complex DAGs, running on slurm would requires additional development

   [http://docs.cerit.io/docs/kubeflow.html](http://docs.cerit.io/docs/kubeflow.html)

3. **Nextflow** - able to run on K8s and Slurm, not ML friendly

   [http://docs.cerit.io/docs/nextflow.html](http://docs.cerit.io/docs/nextflow.html)
