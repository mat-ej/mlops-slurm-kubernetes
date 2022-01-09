#!/bin/bash
#SBATCH --job-name={{name}}
#SBATCH --output=result.out
#

# activate base
conda activate base
srun {{command}}