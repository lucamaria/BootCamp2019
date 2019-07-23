#!/bin/bash

#SBATCH --job-name=Hello_LM_hard

#SBATCH --output=Hello_LM_hard.out

#SBATCH --ntasks=1

#SBATCH --partition=broadwl

# Run the process

./Hello_LM_hard.x
