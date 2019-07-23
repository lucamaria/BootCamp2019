#!/bin/bash

#SBATCH --job-name=BS

#SBATCH --output=BS.out

#SBATCH --ntasks=1

#SBATCH --partition=broadwl

# Run the process

./BS.x
