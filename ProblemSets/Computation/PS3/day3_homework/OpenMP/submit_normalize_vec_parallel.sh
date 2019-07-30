#!/bin/bash -l

#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8

#SBATCH --time=00:01:00


#SBATCH --job-name=normalize_vec_parallel
#SBATCH --output=normalize_vec_parallel.out
#SBATCH --error=normalize_vec_parallel.err

export OMP_NUM_THREADS=6


### openmp executable
./normalize_vec_parallel.exec
