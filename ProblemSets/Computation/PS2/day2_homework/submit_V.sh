#!/bin/bash

#SBATCH --job-name=VFI

#SBATCH --output=VFI.out

#SBATCH --ntasks=1

#SBATCH --partition=broadwl

# Run the process

./VFI
