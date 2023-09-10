#PBS -N real
#PBS -l walltime=12:00:00
#PBS -l nodes=1:ppn=1
#PBS -l mem=1000MB
#PBS -j oe

generation_size=${G}
population_size=${P}
elite_factor=${E}
mutation_factor=${M}

echo "Generation size: $generation_size"
echo "Population size: $population_size"
echo "Elite factor: $elite_factor"
echo "Mutation factor: $mutation_factor"
echo "all mutations"
echo "real"

cd $PBS_O_WORKDIR
echo $PBS_O_WORKDIR

module load python/3.6-conda5.2
python -u proof_optimization.py $generation_size $population_size $elite_factor $mutation_factor >& ./logs/real.log
