#!/bin/bash

#SBATCH --job-name=eat_pie

#SBATCH --output=eat_pie.out

#SBATCH --account=osmlab

#SBATCH --ntasks=1

#SBATCH --partition=broadwl

# Run the process

./comp_pi.x
