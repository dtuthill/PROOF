# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:46:55 2019

@author: Daniel Tuthill
"""

import random
import numpy as np
from Codes import initialization
from math import pi

def mutation (population,mutation_rate,pop_size,elite_factor,nHarm,seed3,seed4):
    
    x = np.arange(-nHarm/2,nHarm/2)         #create x array for uniform mutation
    
    for child in range(int(pop_size-round(pop_size*elite_factor))):     #loop through non-elite members
        if random.random() < mutation_rate:                             #choose number between 0,1. if less than mutation rate then mutate
            gene = random.randrange(0,nHarm)                            #select gen to mutate
            population[child,gene] += random.uniform(-pi,pi)            #add random value
            
        if random.random() < mutation_rate:                             #decide mutation           
            splice1 = random.randrange(0,nHarm)                         #decide splice point 1
            splice2 = random.randrange(0,nHarm)                         #decide splice point 2
            splice_beginning = min(splice1,splice2)                     #order splice points
            splice_end = max(splice1,splice2)                           #order splice points
            population[child,splice_beginning:splice_end] += random.uniform(-pi,pi)     #add random value
            
        if random.random() < mutation_rate:                             #decide mutation
            population[child] += initialization.randpoly(x,seed3,seed4) #add random polynomial
            
    return population
    
def crossover (population,mutation_rate,pop_size,elite_factor,nHarm):
    
    cross_over_pairs = random.sample(range(int(pop_size-round(pop_size*elite_factor))),int((pop_size-round(pop_size*elite_factor))))        #selet crossover pairs randomly from non-elite members  

    for child in range(int((pop_size-round(pop_size*elite_factor))/2)):                 #loop over non-elite pairs
        if random.random() < mutation_rate:                                             #decide crossover
            gene = random.randrange(0,nHarm)                                            #select cross-over gene
            child_gene1 = population[cross_over_pairs[child],gene]                      #pull cross-over value 1
            child_gene2 = population[cross_over_pairs[-1*(child+1)],gene]               #pull cross-over value 2
            population[cross_over_pairs[child],gene] = child_gene2                      #swap value 1
            population[cross_over_pairs[-1*(child+1)],gene] = child_gene1               #swap value 2
            
        if random.random() < mutation_rate:                                             #decide mutation
            flip_genes = random.sample(range(nHarm),random.randrange(0,nHarm))          #decide genes to flip
            child_genes1 = population[cross_over_pairs[child],tuple(flip_genes)]        #pull values 1
            child_genes2 = population[cross_over_pairs[-1*(child+1)],tuple(flip_genes)] #pull values 2
            population[cross_over_pairs[child],tuple(flip_genes)] = child_genes2        #swap values 1
            population[cross_over_pairs[-1*(child+1)],tuple(flip_genes)] = child_genes1 #swap values 2
            
    return population

def rotation (population,mutation_rate,pop_size,elite_factor,nHarm):
    
    for child in range(int(pop_size-round(pop_size*elite_factor))):                     #loop over non-elite population
        if random.random() < mutation_rate:                                             #deicde mutation
            rotation_length = random.randrange(0,nHarm)                                 #decide rotation_length
            population[child] = np.roll(population[child],rotation_length)              #rotate
            
    return population
