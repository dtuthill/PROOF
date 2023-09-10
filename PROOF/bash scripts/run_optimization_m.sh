for run in 1 2 3 4 5
do
	qsub -A PAS1495 -v G=100000,P=20000,E=0.15,M=0.15 proof_optimization.sh
done
