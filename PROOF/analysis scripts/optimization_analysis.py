# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:32:22 2019

@author: Daniel Tuthill
"""
from os import getcwd
import numpy as np
import math
import matplotlib.pyplot as plt

load = True

if load:
    
    data = {}
    
    mutation = ["allm","conly","monly","ronly"]
    
    for j in mutation:
        path = getcwd() + "/outputDATA/g100000_p20000_e0.15_m0.15"+j+".csv"
        key = j
        full_data = np.loadtxt(path,delimiter=",")
        row, column = full_data.shape
        k=0
        for i in range(1,row):
            if (full_data[i,0] != 0 and full_data[i-1,0] == 0):
                data_set = full_data[i-1].reshape((1,len(full_data[0])))
                data_set = np.append(data_set,full_data[i].reshape((1,len(full_data[0]))),axis=0)
            elif (full_data[i,0] != 0):
                data_set = np.append(data_set,full_data[i].reshape((1,len(full_data[0]))),axis=0)
            if (full_data[i,0] == 0 and full_data[i-1,0] != 0):
                data[key+str(k)] = data_set
                k += 1

    pPath = getcwd() + "/inputDATA/phase_pi2_actual_grad.txt"

    phases = np.empty(0)
    with open(pPath) as text:
        for line in text:
            phases = np.append(phases, float(line))
    phases -= np.mean(phases)
    
    iPath = getcwd() + "/inputDATA/intensity_pi2_actual_grad.txt"

    intensity = np.empty(0)
    with open(iPath) as text:
        for line in text:
            intensity = np.append(intensity, float(line))

# phase plots

for i in range (8):
    key = 'conly' + str(i)
    column = len(data[key][-1,4:])
    final_phase = data[key][-1,4:] - data[key][-1,4]
    for l in range(1,column):
        while np.abs(final_phase[l]-final_phase[l-1]) > math.pi:
            if final_phase[l]-final_phase[l-1] > math.pi:
                final_phase[l] -= 2*math.pi
            if final_phase[l]-final_phase[l-1] < -math.pi:
                final_phase[l] += 2*math.pi
    final_phase -= np.mean(final_phase[1:-1])
    key_label = str(i)
    ax = plt.plot(final_phase,label=key_label)

plt.plot(phases,"y",label="Actual Phases")
plt.rcParams.update({'font.size': 12})
plt.suptitle("Phase using all mutations", fontsize=18)
plt.xlabel("Harmonic",fontsize=18)
plt.ylabel("Phase [rad]",fontsize=18)
plt.legend(bbox_to_anchor=(1.01,0.5),loc="center left")

## average values
#dphi average

#final_phases = np.zeros((5,20))
#
#for i in range (5):
#    key = 'allm' + str(i)
#    column = len(data[key][-1,4:])
#    final_phase = data[key][-1,4:] - data[key][-1,4]
#    for l in range(1,column):
#        while np.abs(final_phase[l]-final_phase[l-1]) > math.pi:
#            if final_phase[l]-final_phase[l-1] > math.pi:
#                final_phase[l] -= 2*math.pi
#            if final_phase[l]-final_phase[l-1] < -math.pi:
#                final_phase[l] += 2*math.pi
#    final_phase -= np.mean(final_phase[1:-1])
#    final_phases[i] = final_phase
#    
#average_phase = np.mean(final_phases,axis=0)
#average_phase -= np.mean(average_phase)
#
#diff = np.abs(average_phase-phases)
#final_diff = np.average(np.abs(diff[1:-1] - np.mean(diff[1:-1])),weights=intensity[1:-1]/np.amax(intensity[1:-1]))
#print(final_diff)

#print(key)
#convergence generation

#final_generation = 0
#
#for i in range (8):
#    key = 'conly' + str(i)
#    print(data[key][-1,0])
#    final_generation += data[key][-1,0]
#    
#final_generation /= 8
#print(key)
#print(final_generation)

#final objective
            
#final_objective = 0
#
#for i in range (8):
#    key = 'conly' + str(i)
#    print(data[key][-1,2])
#    final_objective += data[key][-1,2]
#    
#final_objective /= 8
#print(key)
#print(final_objective)