#!/bin/bash -l
#SBATCH --job-name="HJ161007922RRapro"
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=512
#SBATCH --cpus-per-task=1
#SBATCH --partition=normal
#SBATCH --constraint=mc
#SBATCH --hint=nomultithread
#SBATCH --account=uzh10

module load cmake gnu14

chmod u+x MCproCSCS.sh
srun --bcast --wait=0 MCproCSCS.sh $SLURM_ARRAY_TASK_ID 

