# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:51:55 2019

@author: Daniel Tuthill
"""

"""
PROOF class for running the algorithm. Call this to intialize the process
and arrays. Then call the four functions to continue through the PROOF
algorithm
"""


import numpy as np
import random
from Codes import initialization
from Codes import fitness
from Codes import classes
from Codes import reproduction
from Codes import mutation


class PROOF:
    def __init__(self,population_size,elite_factor,mutation_rate):
        
        """
        The inputs of this initializaiton are the population size, the
        percentage of each generation to clone exempt from mutation
        (elite_factor) and the percentage chance for any mutation to 
        occur (mutation_rate).
        
        Each subclasses callables explained in function where used
        """
        
        #extract data from subdirectory /inputDATA as data class
        #must be labeled intensity.txt and alpha.txt
        #callables: intensity, intensity_sqrt, and alpha
        self.data = classes.extract_data()
        
        #initialize parameters needed as PROOF class
        self.nHarm = len(self.data.intensity)+2     #number of harmonics     
        self.pop_size = population_size             #population size of each generation
        
        #intialize arrays needed as family_tree class for each generation
        #callables: parents, population, fitness, objective
        self.family_tree = classes.family_tree(self.pop_size,self.nHarm)
        
        #initialize arrays needed for fitness calculation and reproduction as roulette class
        #callables: alias, prob
        self.roulette = classes.roulette(self.pop_size,self.nHarm,self.family_tree.fitness)
        
        #initialize constants needed for algorithm as constants class
        #callables: elite_factor, mutation_rate, seed3, seed4
        self.constants = classes.constants(elite_factor,mutation_rate)
        
    def initialize_population(self):
        
        """
        Initially create the population using new polynomial of random order
        for each member. Input of polynomial is array of integers evenly
        spaced around 0 of length number of harmonics
        """
        
        x = np.arange(-self.nHarm/2,self.nHarm/2)   #intializaiton polynomial input
        seed1 = np.random.RandomState()             #seed for random polynomial order selection
        seed2 = np.random.RandomState()             #seed for random coefficient selection
        
        for chrom_num in range(self.pop_size):      #loops over each member in population, creating it
            self.family_tree.population[chrom_num] = initialization.randpoly(x,seed1,seed2)     #initial population saved here

                
    def calculate_fitness(self):
        
        alpha = fitness.calc_alpha(self.family_tree.population,self.data.intensity_sqrt)            #calculates alpha for each gene of each population member
        self.family_tree.fitness, self.family_tree.objective = fitness.calc_fitness(alpha,self.data.alpha,self.data.intensity)          #calcluates objective and fitness values for each population member
        
    def reproduce(self):
                        
        self.family_tree.parents = self.family_tree.population.copy()           #copy generation to parents so generation can be replaced
                
        self.roulette.prob, self.roulette.alias = reproduction.initialize_wheel(self.family_tree.fitness,self.pop_size)         #create alias and probability tables using Vose's Alias Method
        
        self.family_tree.population = self.family_tree.population[np.argsort(self.family_tree.fitness)]                         #sort population to allow for elite cloning
        
        for child in range(int(self.pop_size-round(self.pop_size*self.constants.elite_factor))):                                #loop over non-elite rows to produce new children
            parent1 = reproduction.alias_selection(self.pop_size,self.roulette.prob,self.roulette.alias)
            parent2 = reproduction.alias_selection(self.pop_size,self.roulette.prob,self.roulette.alias)
            random_splice = random.randrange(1,self.nHarm)
            self.family_tree.population[child,:random_splice] = self.family_tree.parents[parent1,:random_splice]
            self.family_tree.population[child,random_splice:] = self.family_tree.parents[parent2,random_splice:]
       
    def mutate(self):
        
        self.family_tree.population = mutation.mutation (self.family_tree.population,self.constants.mutation_rate,self.pop_size,self.constants.elite_factor,self.nHarm,self.constants.seed3,self.constants.seed4)
        self.family_tree.population = mutation.crossover (self.family_tree.population,self.constants.mutation_rate,self.pop_size,self.constants.elite_factor,self.nHarm)
        self.family_tree.population = mutation.rotation (self.family_tree.population,self.constants.mutation_rate,self.pop_size,self.constants.elite_factor,self.nHarm)

        
