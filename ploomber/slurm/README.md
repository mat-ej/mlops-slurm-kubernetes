# Running ploomber pipelines on Slurm

#### Notes:
1. ploomber containerizes with a single container i.e. single conda/singularity environment for the whole pipeline.

**slurm commands**

    ml avail | grep "singularity"


## Remote slurm cluster = rci
ssh into rci

    #!/usr/bin/env bash
    sshpass -p <password> ssh <login>@login.rci.cvut.cz
    
    #rm -rf ~/rci_home
    #mkdir ~/rci_home
    sshfs -o password_stdin uhrinmat@login.rci.cvut.cz:/home/uhrinmat ~/rci_home/ <<< '<password>'

## optional:  ploomber installation
install into some conda environment on a slurm login node

    (base)$pip install ploomber --upgrade
    (base)$pip install soopervisor --upgrade

### load example project
    ploomber examples -n cookbook/grid -o grid
    cd grid

### prepare env for batch jobs (Anaconda)
load the module
    
    ml Anaconda3/2021.05
    eval "$(conda shell.bash hook)"

create folder to hold pipeline environment and build env from .yml into prefix location

    mkdir ~/anaconda
    conda env create --prefix ~/anaconda/cookbook-grid --file environment.yml
    
    # verify the environment
    conda activate $HOME/anaconda/cookbook-grid
    which python

#### set up template.sh for slurm jobs
go to grid project folder

    # if cluster directory does not exist
    soopervisor add cluster --backend slurm

modify cluster/template.sh as follows:

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

where **$HOME/anaconda** is our environment folder and **cookbook-grid** is our environment.


### singularity for environment
for more complex environments beyond python packages, singularity container will be required.
    
    ml singularity
    singularity version

    # the following fails for more complex containers
    singularity run docker://godlovedc/lolcow

singularity run fails for some docker containers
in that case, rebuilt at a local machine and push into singularity repo works best.

## Local slurm cluster
TODO