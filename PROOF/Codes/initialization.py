#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:45:11 2019

@author: Daniel Tuthill
"""

import numpy as np
from math import pi
    
def randpoly(x,seed1,seed2):
    n = seed1.randint(1,10)               #randomly select polynomial order between 1 and 10
    coefficients = np.empty(n)            #initialize coefficient array
    for order in range(n):
        coefficients[n-order-1] = seed2.uniform(-pi,pi) / (10**order)           #randomly produce coefficients
    poly = np.poly1d(coefficients)       #create polynomial function from coefficients with numpy.array input
    return poly(x)                       #act polynomial element-wise on x. x defined in classPROOF
