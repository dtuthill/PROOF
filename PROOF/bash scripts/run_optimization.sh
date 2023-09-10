for elite_factor in 0.0 0.05 0.10 0.15 0.20
do
    for mutation_factor in 0.0 0.05 0.10 0.15 0.20
    do
        echo "Mutation factor: $mutation_factor"
	echo "Elite factor: $elite_factor"
        qsub -A PAS1495 -v G=100000,P=20000,E=$elite_factor,M=$mutation_factor proof_optimization.sh
    done
done
