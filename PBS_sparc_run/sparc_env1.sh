module purge
module load intel/19.0.5
module load anaconda3/2020.02

export PATH=/storage/home/hpaceice1/ggoodwin6/sparc_run/SPARC/lib:$PATH
export PYTHONPATH=/storage/home/hpaceice1/ggoodwin6/sparc_run/SPARC/src/ase:$PYTHONPATH
export PATH=/storage/home/hpaceice1/ggoodwin6/sparc_run/SPARC/src/ase/bin:$PATH
export PYTHONPATH=/storage/home/hpaceice1/ggoodwin6/sparc_run/SPARC/src/sparc-dft-api/:$PYTHONPATH
export SPARC_PSP_PATH=/storage/home/hpaceice1/ggoodwin6/sparc_run/SPARC/src/sparc-dft-api/sparc/pseudos/PBE_pseudos

if [[ -z "${PBS_NP}" ]]; then
  export ASE_SPARC_COMMAND="/storage/home/hpaceice1/ggoodwin6/sparc_run/SPARC/lib/sparc -name PREFIX"
else
  export ASE_SPARC_COMMAND="mpirun -np $PBS_NP /storage/home/hpaceice1/ggoodwin6/sparc_run/SPARC/lib/sparc -name PREFIX"
fi
