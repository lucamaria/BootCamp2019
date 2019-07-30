#!/bin/bash -l

#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8

#SBATCH --time=00:01:00


#SBATCH --job-name=monte_carlo_parallel
#SBATCH --output=monte_carlo_parallel10000.out
#SBATCH --error=monte_carlo_parallel.err


export OMP_NUM_THREADS=4


### openmp executable

./monte_carlo_parallel.exec
