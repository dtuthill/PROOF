# -*- coding: utf-8 -*-
"""
fakeDATA.py
Created on Sun Apr  7 14:55:50 2019

@author: Daniel Tuthill

Creates fake intensities, phase, and alpha data for usage in PROOF algorithm
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from math import pi, sqrt, atan2, sin, cos, exp
from os import getcwd

#Initial parameters

nHarm = 20 + 2              #Number of harmonics + 2 (2 extra end points needed for alpha calculation)

#Create fake intensities

intensity = np.zeros(nHarm)

for i in range(0,nHarm):
    #   intensity[i] = (i)**(2/3)
    #   intensity[i] = 10*exp(-(i-nHarm/2.5)**2/20)+4*exp(-(i-nHarm/1.2)**2/10)
        intensity[i] = 6*exp(-(i-nHarm/8)**2/3)+10*exp(-(i-nHarm/2.5)**2/15)+5*exp(-(i-nHarm/1.5)**2/10)
for i in range(1,nHarm,2):
    intensity[i] *= 0.3
    


#Create fake phases

phases = np.zeros(nHarm)
for i in range(0,nHarm):
#    phases[i] = 0.02*nHarm/3+0.03*(i-nHarm/12)**2+0.0006*(i-nHarm/24)**3+0.00008*(i-nHarm)**4
#    phases[i] =  0.01*(i-nHarm/2)**2
    phases[i] = 0.01*(i-nHarm/5)**2
    if i % 2 == 1:
        phases[i] += (i/nHarm)*pi/2

#for i in range(0,nHarm,2):
#    phases[i] = pi/3
#    
#for i in range(0,nHarm):
#    phases[i] += 0.1*i
    
#create alphas based on intensities and phases

alphas = np.zeros(nHarm-2)

for i in range(1,nHarm-1):
    y = sqrt( intensity[i+1] ) * sin(phases[i] - phases[i+1] ) + sqrt( intensity[i-1] ) * sin(phases[i] - phases[i-1] )
    x = sqrt( intensity[i+1] ) * cos(phases[i] - phases[i+1] ) - sqrt( intensity[i-1] ) * cos(phases[i] - phases[i-1] )
    alphas[i-1] = atan2(y,x)
    
#write values to files
    
iPath = getcwd() + "/inputDATA/intensity_pi2_actual_grad.txt"
pPath = getcwd() + "/inputDATA/phase_pi2_actual_grad.txt"
aPath = getcwd() + "/inputDATA/alpha_pi2_actual_grad.txt"

with (open(iPath, 'w')) as text:
    for i in range(1, nHarm - 1):
        text.write(str("%.6f" %  intensity[i]))
        if i < nHarm - 2:
            text.write("\n")
            
with (open(pPath, 'w')) as text:
    for i in range(1, nHarm - 1):
        text.write(str("%.6f" %  phases[i]))
        if i < nHarm - 2:
            text.write("\n")

with (open(aPath, 'w')) as text:
    for i in range(0, nHarm-2):
        text.write(str("%.6f" %  alphas[i]))
        if i < nHarm - 2:
            text.write("\n")
            
plt.plot(phases)
plt.plot(intensity)