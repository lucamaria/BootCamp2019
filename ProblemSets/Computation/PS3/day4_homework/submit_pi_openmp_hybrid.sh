#!/bin/bash
# a sample job submission script to submit a hybrid MPI/OpenMP job to the broadwl
# partition on Midway please change the --partition option if you want to use
# another partition on Midway

# set the job name to pi_openmp_hybrid
#SBATCH --job-name=pi_openmp_hybrid

# send output to hello-hybrid.out
#SBATCH --output=pi_openmp_hybrid.out

# this job requests 4 MPI processes
#SBATCH --ntasks=6


# and request 8 cpus per task for OpenMP threads
#SBATCH --cpus-per-task=12

# this job will run in the broadwl partition on Midway
#SBATCH --partition=broadwl

# load the openmpi default module
module load openmpi

# set OMP_NUM_THREADS to the number of --cpus-per-task we asked for
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Run the process with mpirun. Notice -n is not required. mpirun will
# automatically figure out how many processes to run from the slurm options
mpirun ./pi_openmp_hybrid.exec
