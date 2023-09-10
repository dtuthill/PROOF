#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:07:22 2019

@author: Daniel Tuthill
"""

import numpy as np
from os import getcwd

#imports data

class extract_data:
    def __init__(self):
        
        '''
        class where experimental data is saved
        '''
            
        iPath = getcwd() + "/inputDATA/real_intensity.txt"        #path where intensity data is saved
        aPath = getcwd() + "/inputDATA/real_phase.txt"            #path where alpha data is saved
        
        #input intensity data by looping through lines of file
        intensity_import = np.empty(0)
        with open(iPath) as text:
            for line in text:
                intensity_import = np.append(intensity_import, float(line))
        self.intensity_sqrt = np.sqrt(intensity_import)     #sqrt also saved in order to save computation time
        self.intensity = intensity_import[1:-1]             #endpoints removed in order to save computation time on future calls in reproduction
        
        #input alpha data by looping through lines of file        
        alpha_import = np.empty(0)
        with open(aPath) as text:
            for line in text:
                alpha_import = np.append(alpha_import, float(line))
        self.alpha = alpha_import[1:-1,None].transpose()    #endpoints and transpose removed in order to save computation time on future calls in fitness calculation
        
class family_tree:
    def __init__(self,pop_size,nHarm):
        self.parents = np.empty((pop_size,nHarm))           #parent population to current population being produced. using in reproduction
        self.population = np.empty((pop_size,nHarm))        #current population used for that generation
        self.fitness = np.empty(pop_size)                   #fitness for current population
        self.objective = np.empty(pop_size)                 #objective for current population
        
class roulette:
    def __init__(self,pop_size,nHarm,fitness):
        self.alias = np.empty(pop_size)                     #alias array used for reproduction. see reproduction.py for more information
        self.prob = np.empty(pop_size)                      #probability array used for reproduction. see reproduction.py for more information

class constants:
    def __init__(self,elite_factor,mutation_rate):
        self.elite_factor = elite_factor                    #elite_factor used for cloning population
        self.mutation_rate = mutation_rate                  #chance of population member being mutated
        self.seed3 = np.random.RandomState()                #used for mutation. see mutation.py
        self.seed4 = np.random.RandomState()                #used for mutation. see mutation.py
