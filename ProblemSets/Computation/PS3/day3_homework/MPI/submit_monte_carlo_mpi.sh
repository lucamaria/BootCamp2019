#!/bin/bash -l

#SBATCH --ntasks=16

#SBATCH --time=00:01:00

#SBATCH --output=monte_carlo_mpi.out
#SBATCH --error=monte_carlo_mpi.err


### MPI executable
mpiexec -np $SLURM_NTASKS ./monte_carlo_mpi.exec
