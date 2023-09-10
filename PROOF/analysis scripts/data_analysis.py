# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:32:22 2019

@author: Daniel Tuthill
"""
from os import getcwd
import numpy as np
import math
import matplotlib.pyplot as plt

load = False

data_type = ["rand","cont","pi2_gradual","pi2","real"]


if load:
    
    data = {}
    phases = {}
    intensity = {}
        
    for j in data_type:
        path = getcwd() + "/outputDATA/" + j +".csv"
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
        if j != "real":
            
            pPath = getcwd() + "/inputDATA/phase_"+ j +".txt"
            
            phases[key] = np.empty(0)
            with open(pPath) as text:
                for line in text:
                    phases[key] = np.append(phases[key], float(line))
            phases[key] -= np.mean(phases[key])
        
        iPath = getcwd() + "/inputDATA/intensity_"+ j +".txt"
        
        intensity[key] = np.empty(0)
        with open(iPath) as text:
            for line in text:
                intensity[key] = np.append(intensity[key], float(line))

# phase plots

for i in range (5):
    key = 'real' + str(i)
    column = len(data[key][-1,4:])
    final_phase = data[key][-1,4:] - data[key][-1,4]
    for l in range(1,column):
        while np.abs(final_phase[l]-final_phase[l-1]) > math.pi:
            if final_phase[l]-final_phase[l-1] > math.pi:
                final_phase[l] -= 2*math.pi
            if final_phase[l]-final_phase[l-1] < -math.pi:
                final_phase[l] += 2*math.pi
    final_phase -= np.mean(final_phase[1:-1])
    for l in range(column):
        if final_phase[l] < -math.pi:
            final_phase[l] += 2*math.pi
        if final_phase[l] > math.pi:
            final_phase[l] -= 2*math.pi
    key_label = str(i)
    ax = plt.plot(final_phase,label=key_label)

#plt.plot(phases["real"],"y",label="Actual Phases")
plt.rcParams.update({'font.size': 12})
plt.suptitle("Phase using all mutations", fontsize=18)
plt.xlabel("Harmonic",fontsize=18)
plt.ylabel("Phase [rad]",fontsize=18)
plt.legend(bbox_to_anchor=(1.01,0.5),loc="center left")

## average values
##dphi average
#
#final_phases = np.zeros((5,20))
#
#d_type = "rand"
#
#for i in range (5):
#    key = d_type + str(i)
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
#diff = np.abs(average_phase-phases[d_type])
#final_diff = np.average(np.abs(diff[1:-1] - np.mean(diff[1:-1])),weights=intensity[d_type][1:-1]/np.amax(intensity[d_type][1:-1]))
#print(dtype)
#print(final_diff)

#convergence generation

#final_generation = 0
#
#dtype = "real"
#
#for i in range (5):
#    key = dtype + str(i)
#    final_generation += data[key][-1,0]
#    
#final_generation /= 5
#print(dtype)
#print(final_generation)

#final objective
  
#dtype = "real"
#          
#final_objective = 0
#
#for i in range (5):
#    key = dtype + str(i)
#    print(data[key][-1,2])
#    final_objective += data[key][-1,2]
#    
#final_objective /= 5
#print(dtype)
#print(final_objective)