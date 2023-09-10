
#PBS -N proof_optimization
#PBS -l walltime=0:30:00
#PBS -l nodes=1:ppn=4
#PBS -j oe
cd $PBS_O_WORKDIR
echo $PBS_O_WORKDIR
module load python/3.6-conda5.2
python -u proof_optimization.py 10000 10000 0.05 0.1 >& proof_optimization_4nodes.log
