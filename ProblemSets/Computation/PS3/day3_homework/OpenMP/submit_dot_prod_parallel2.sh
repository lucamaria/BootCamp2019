#!/bin/bash -l

#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8

#SBATCH --time=00:02:00


#SBATCH --job-name=dot_prod_parallel2
#SBATCH --output=dot_prod_parallel2.out
#SBATCH --error=dot_prod_parallel2.err

export OMP_NUM_THREADS=1

### openmp executable
./dot_prod_parallel.exec

export OMP_NUM_THREADS=2

### openmp executable
./dot_prod_parallel.exec

export OMP_NUM_THREADS=3

### openmp executable
./dot_prod_parallel.exec

export OMP_NUM_THREADS=4

### openmp executable
./dot_prod_parallel.exec

export OMP_NUM_THREADS=5

### openmp executable
./dot_prod_parallel.exec

export OMP_NUM_THREADS=6

### openmp executable
./dot_prod_parallel.exec

export OMP_NUM_THREADS=7

### openmp executable
./dot_prod_parallel.exec

export OMP_NUM_THREADS=8

### openmp executable
./dot_prod_parallel.exec
