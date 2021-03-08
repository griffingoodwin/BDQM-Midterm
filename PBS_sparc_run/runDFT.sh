#!/bin/bash
#PBS -l nodes=1:ppn=5
#PBS -l walltime=0:25:00
#PBS -q pace-ice
#PBS -N DFT_Test
#PBS -o stdout
#PBS -e stderr
cd $PBS_O_WORKDIR
source /storage/home/hpaceice1/ggoodwin6/PBS_sparc_run/sparc_env1.sh
python DFT.py
