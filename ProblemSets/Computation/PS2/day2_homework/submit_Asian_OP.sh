#!/bin/bash

#SBATCH --job-name=Asian_Op

#SBATCH --output=Asian_Op.out

#SBATCH --ntasks=1

#SBATCH --partition=broadwl

# Run the process

./Asian_Op.x
