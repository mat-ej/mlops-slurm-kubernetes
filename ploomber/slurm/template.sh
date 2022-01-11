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