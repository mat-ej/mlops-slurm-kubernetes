# Running ploomber pipelines on Slurm

#### Notes:
Q: Why does slurm not require containerization? it is enough to set the env once. 


## Local slurm cluster
run docker compose up.
TODO
## Remote slurm cluster = rci
ssh into rci

    #!/usr/bin/env bash
    sshpass -p <password> ssh uhrinmat@login.rci.cvut.cz
    
    #rm -rf ~/rci_home
    #mkdir ~/rci_home
    sshfs -o password_stdin uhrinmat@login.rci.cvut.cz:/home/uhrinmat ~/rci_home/ <<< '<password>'


#### optional install miniconda
    # install miniconda (to get a Python environment ready, not needed if
    # there's already a Python environment up and running)
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash ~/Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda
    
## set up environment
    # init conda
    eval "$($HOME/miniconda/bin/conda shell.bash hook)"
    

### env create fails on rci slurm 
    # create and activate env
    conda env create --name myenv
    conda activate myenv
TODO find out why

#### pip install ploomber soopervisor
    # install ploomber and soopervisor in the base environment
    pip install ploomber
    # install soopervisor from the slurm branch
    pip install git+https://github.com/ploomber/soopervisor

#### cd into example project
ploomber/slurm/example

    # install project dependencies
    pip install -r requirements.txt
    
#### optional set up example project 
    # download sample pipeline to example/
    ploomber examples -n templates/ml-basic -o example
    cd example
    
    # install project dependencies
    pip install -r requirements.txt


#### optional: set up slurm as executor
    # register a soopervisor environment with the SLURM backend
    soopervisor add cluster --backend slurm

creates submit script template.sh in cluster subfolder.

#### set up slurm job submit script: template.sh
in cluster/template.sh edit it accordiingly.

    #!/bin/bash
    #SBATCH --job-name={{name}}
    #SBATCH --output=result.out
    #
    
    # activate base
    conda activate base
    srun {{command}}