#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:40:49 2019

@author: danieltuthill
"""

from Codes import classPROOF
import time
from os import getcwd
import numpy as np
import sys

print_factor = 100                          #how often to print resutls

generation_size = int(sys.argv[1])
population_size = int(sys.argv[2])
elite_factor = float(sys.argv[3])
mutation_factor = float(sys.argv[4])

print("Generation size: ",generation_size)
print("Population size: ",population_size)
print("Elite factor: ",elite_factor)
print("Mutation factor: ",mutation_factor)

proof = classPROOF.PROOF(population_size,elite_factor,mutation_factor)          #initialize PROOF class

save_data = np.empty((int(generation_size/print_factor)+1,proof.nHarm+4))       #initialize output data array

time_init = time.time()                                                         #time tracker

proof.initialize_population()                                                   #initialize population

i = 0                                                                           #saved data array index
patience = 0                                                                    #convergence patience

for generation in range(generation_size+1):                                     #loop oer generations
    if generation % print_factor == 0:                                          #loop over generations and check convergence conditions
        print(generation)
        print("Time: ",time.time()-time_init)
        print("Max Fitness: ",np.amax(proof.family_tree.fitness))
        print("Max Objective: ",np.amin(proof.family_tree.objective))
        save_data[i,0] = generation
        save_data[i,1] = np.amax(proof.family_tree.fitness)
        save_data[i,2] = np.amin(proof.family_tree.objective)
        save_data[i,3] = time.time()-time_init
        save_data[i,4:] = proof.family_tree.population[-1]
        if (np.abs(save_data[i,2] - save_data[i-10,2]) < 0.0000001 and generation > 20000):     #check convergence conditions
            patience += 1                                                       #add patience
        else:
            patience = 0
        if patience == 10:                                                      #if met 10 times, end PROOF
            break
        i += 1
    proof.calculate_fitness()
    proof.reproduce()
    proof.mutate()
 
phase_data = open(getcwd() + "/outputDATA/real.csv",'ab')                       #save data
    
np.savetxt(phase_data,save_data,delimiter=",",header="generation     fitness     objective     time     phase")

phase_data.close()
    
print("done")
