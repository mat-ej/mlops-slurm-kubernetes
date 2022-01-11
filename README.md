# MLops review 
MLops tools review focused on pipeline execution using multiple clusters: slurm, kubernetes, dask...

Working examples so far:
1. **Ploomber pipelines** - runs on Slurm, K8s, Airflow, Kubeflow(in progress), no complex DAGs with loops/recursions yet.
   1. Kubernetes - example runs pipeline on local k8s using argo
   2. Slurm - Ploomber transforms the pipeline into batch jobs waiting for the completion of the previous jobs. Example batch job submit template looks as follows: 
```
   #!/bin/bash
   #SBATCH --job-name={{name}}
   #SBATCH --output=result.out
   #
   
   # load anaconda module
   module purge
   ml Anaconda3/2021.05
   # activate prepared environment
   
   eval "$(conda shell.bash hook)"
   conda activate $HOME/anaconda/cookbook-grid
   
   #srun with specified env variables above.
   srun {{command}}
```

2. **Nextflow pipelines** - runs very well on K8s, Slurm, Dask and many others, not focused on ML and hence not ML friendly. No complex DAGs with loops. 

   [http://docs.cerit.io/docs/nextflow.html](http://docs.cerit.io/docs/nextflow.html)


3. **Kubeflow pipelines** - runs on K8s, supports complex DAGs with loops and recursions, running on slurm would require additional development

   [http://docs.cerit.io/docs/kubeflow.html](http://docs.cerit.io/docs/kubeflow.html)

   **working-examples include:**
   1. recursion.py - how to define recursive pipeline using kubeflow
   2. produce_consume_df.py - how to pass pandas dataframe between pipeline components.
   3. others...


