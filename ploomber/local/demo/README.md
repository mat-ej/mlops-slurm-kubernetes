# demo
Requires [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

## Setup development environment

```sh
# configure dev environment
ploomber install


# ...or use conda directly
conda env create --file environment.yml

# activate conda environment
conda activate demo
```



## Running the pipeline

```sh
ploomber build

# start an interactive session
ploomber interact
```

## Exporting to other systems

[soopervisor](https://soopervisor.readthedocs.io/) allows you to run ploomber projects in other environments (Kubernetes, AWS Batch, AWS Lambda and Airflow). Check out the docs to learn more.