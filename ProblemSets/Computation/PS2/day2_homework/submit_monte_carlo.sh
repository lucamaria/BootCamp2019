#!/bin/bash

#SBATCH --job-name=monte_carlo

#SBATCH --output=monte_carlo.out

#SBATCH --ntasks=1

#SBATCH --partition=broadwl

# Run the process

./monte_carlo.x
