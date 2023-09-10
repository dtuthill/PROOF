#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:10:36 2019

@author: Daniel Tuthill
"""

import numpy as np
import random

def initialize_wheel (fitness,pop_size):
    
    alias = np.empty(pop_size)                              #intialize alias
    prob = np.empty(pop_size)                               #initialize probability
    probability = fitness/np.sum(fitness) * pop_size        #produce probabilities from fitness
    large = 0                                               #current large element
    small = 0                                               #current small element
            
    while (large < pop_size and probability[large] < 1):    #find first large element
        large += 1
    while (small < pop_size and probability[small] >= 1):   #find first small element
        small += 1
    next_small = small + 1
    
    while (large < pop_size and small < pop_size):
        prob[small] = probability[small]                    #place first small element in probability array
        alias[small] = large                                #place first large alias in alias array
        probability[large] = (probability[large] + probability[small]) - 1     #adjust alias probability
        if (probability[large] >= 1 or next_small <= large):            #if current large element is still greater than one or next small element is small
            small = next_small                              #advance small marker
            while (small < pop_size and probability[small] >= 1):       #continue advancing small marker until finds a small element
                small += 1
            next_small = small + 1
        else:
            small = large                                   #small marker has reached large
        while (large < pop_size and probability[large] < 1):    #advance large marker to next large
            large += 1

    
    while (large < pop_size):                               #in case large elements left equal one and small is exhasuted, add all to alias
        if (probability[large] < 1):
            large += 1
            continue
        prob[large] = 1
        alias[large] = large
        large += 1   
    
    if (small < pop_size):                                  #in case small elements left equal one
        prob[small] = 1
        alias[small] = small
        small = next_small
        while (small < pop_size):
            if (probability[small] > 1):
                small += 1
                continue
            prob[small] = 1
            alias[small] = small
            small += 1
    
    return prob, alias.astype(int)

def alias_selection(pop_size,prob,alias):
    side = random.randrange(0,pop_size)                     #choose column randomly
    if random.random() < prob[side]:                        #choose value between 0 and 1 and select alias accordingly
        return side
    else:
        return alias[side]