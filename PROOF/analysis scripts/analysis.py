# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:10:17 2019

@author: Daniel Tuthill
"""

from os import getcwd
import numpy as np
import matplotlib.pyplot as plt
import time
import math

load = False

if load:       
    
    data = {}
    elite_factor = [0.0, 0.05, 0.10, 0.15, 0.20]
    mutation_factor = [0.0, 0.05, 0.10, 0.15, 0.20]
    
    for i in elite_factor:
        for j in mutation_factor:
            path = getcwd() + "\outputDATA\g100000_p20000_e"+str(i)+"_m"+str(j)+".csv"
            key = "e"+str(i)+"_m"+str(j)
            data[key] = np.loadtxt(path,delimiter=",")
    
    average = {}
    phi = {}
    average_phi = {}
            
    for i in elite_factor:
        for j in mutation_factor:
            key = "e"+str(i)+"_m"+str(j)
            if key != "e0.0_m0.2":
                average_np = np.zeros((1000,4))
                phi_np = np.zeros((5,20))
                for k in range(1,1001):
                    average_np[(k-1),0] = k*100
                    for l in range(5):
                        average_np[(k-1),1:4] += data[key][k+l*1001,1:4]
                        phi_np[l] = data[key][(l+1)*1000,4:]
                average_np[:,1:4] /= 5
                print(key)
                print(average_np.shape)
                average[key] = average_np
                phi[key] = phi_np
            else:
                print(key)
                print(data[key].shape)
                average[key] = data[key][1:,0:4]
                phi[key] = data[key][-1,4:]    
            
    for i in elite_factor:
        for j in mutation_factor:
            key = "e"+str(i)+"_m"+str(j)
            phi[key] -= np.mean(phi[key])
            print(key)
            if key == "e0.0_m0.2":
                column = len(phi[key])
                phi[key] -= phi[key][0]
                for l in range(1,column):
                    while np.abs(phi[key][l]-phi[key][l-1]) > math.pi:
                        if phi[key][l]-phi[key][l-1] > math.pi:
                            phi[key][l] -= 2*math.pi
                        if phi[key][l]-phi[key][l-1] < -math.pi:
                            phi[key][l] += 2*math.pi
                phi[key] -= np.mean(phi[key])
                average_phi[key] = phi[key]
            else:
                row, column = phi[key].shape
                for k in range(row):
                    phi[key][k] -= phi[key][k,0]
                    for l in range(1,column):
                        while np.abs(phi[key][k,l]-phi[key][k,l-1]) > math.pi:
                            if phi[key][k,l]-phi[key][k,l-1] > math.pi:
                                phi[key][k,l] -= 2*math.pi
                            if phi[key][k,l]-phi[key][k,l-1] < -math.pi:
                                phi[key][k,l] += 2*math.pi
                    phi[key][k] -= np.mean(phi[key][k])
                average_phi[key] = np.average(phi[key],axis=0)
                average_phi[key] -= np.mean(average_phi[key])

    pPath = getcwd() + "/inputDATA/phase.txt"

    phases = np.empty(0)
    with open(pPath) as text:
        for line in text:
            phases = np.append(phases, float(line))
    phases -= np.mean(phases)
    
    iPath = getcwd() + "/inputDATA/intensity.txt"

    intensity = np.empty(0)
    with open(iPath) as text:
        for line in text:
            intensity = np.append(intensity, float(line))

##HEAT MAPS
##Final objective
                
#mutation_factor = [0.0, 0.05, 0.10, 0.15, 0.20]
#elite_factor = [0.0, 0.05, 0.10, 0.15, 0.20]
#                
#final_objective = np.empty((len(elite_factor),len(mutation_factor)))
#
#fig, ax = plt.subplots()
#ax.set_xticks(np.arange(len(elite_factor)))
#ax.set_yticks(np.arange(len(mutation_factor)))
#
#ax.set_xticklabels(elite_factor)
#ax.set_yticklabels(mutation_factor) 
#
#ax.set_xlabel("Mutation Factor",fontsize=18)
#ax.set_ylabel("Elite Factor",fontsize=18)
#ax.set_title("Final Objective for Elite and Mutation Factors", fontsize=18)
#                
#for k,i in enumerate(elite_factor):
#    for l,j in enumerate(mutation_factor):
#        key = "e"+str(i)+"_m"+str(j)
#        final_objective[k,l] = average[key][-1:,2]
#        test = ax.text(l,k,('%.6f' % (math.log(final_objective[k,l]))),ha="center",va="center",color="w")
#
#im = ax.imshow(np.log(final_objective),origin='lower',interpolation='nearest')
#cbar = ax.figure.colorbar(im,ax=ax)
#cbar.set_label("log(Objective)",size=18)
#plt.show()

#Final phase Graph
    
#elite_format = ['b','g','r','c','m']
#mutation_format = ['o','^','s','x','*']
#                
#for k,i in enumerate(elite_factor):
#    for l,j in enumerate(mutation_factor):
#        key = "e"+str(i)+"_m"+str(j)
#        key_label = "Elite: "+str(i)+" Mutation: "+str(j)
#        plt_format = elite_format[k] + mutation_format[l]+str("-")
#        ax = plt.plot(average_phi[key],plt_format,markevery=3,label=key_label)
#
#plt.plot(phases,"y",label="Actual Phases")
#plt.rcParams.update({'font.size': 12})
#plt.suptitle("Phase for Elite and Mutation Factors", fontsize=18)
#plt.xlabel("Harmonic",fontsize=18)
#plt.ylabel("Phase [rad]",fontsize=18)
#plt.legend(bbox_to_anchor=(1.01,0.5),loc="center left")

##Final phase Heat Map
    
#mutation_factor = [0.0, 0.05, 0.10, 0.15, 0.20]
#elite_factor = [0.0, 0.05, 0.10, 0.15, 0.20]
#                
#final_phase = np.empty((len(elite_factor),len(mutation_factor)))
#
#fig, ax = plt.subplots()
#ax.set_xticks(np.arange(len(elite_factor)))
#ax.set_yticks(np.arange(len(mutation_factor)))
#
#ax.set_xticklabels(elite_factor)
#ax.set_yticklabels(mutation_factor) 
#
#ax.set_xlabel("Mutation Factor",fontsize=18)
#ax.set_ylabel("Elite Factor",fontsize=18)
#ax.set_title("Average Phase Error for Elite and Mutation Factors", fontsize=18)
#                
#for k,i in enumerate(elite_factor):
#    for l,j in enumerate(mutation_factor):
#        key = "e"+str(i)+"_m"+str(j)
#        diff = np.abs(average_phi[key]-phases)
#        final_phase[k,l] = np.average(np.abs(diff[1:-1] - np.mean(diff[1:-1])),weights=intensity[1:-1]/np.amax(intensity[1:-1]))
#        test = ax.text(l,k,('%.6f' % final_phase[k,l]),ha="center",va="center",color="w")
#
#im = ax.imshow(final_phase,origin='lower',interpolation='nearest')
#cbar = ax.figure.colorbar(im,ax=ax)
#cbar.set_label("error [rad]",size=18)
#plt.show()
            
##Convergence generation Heat Map
            
mutation_factor = [0.0, 0.05, 0.10, 0.15, 0.20]
elite_factor = [0.0, 0.05, 0.10, 0.15, 0.20]
            
convergence = {}

for k,i in enumerate(elite_factor):
    for l,j in enumerate(mutation_factor):
        key = "e"+str(i)+"_m"+str(j)
        generations = len(average[key][:,2])
        patience = 0
        for generation in range(200,generations):
            if abs(average[key][generation,2] - average[key][generation-10,2]) < 0.0000001:
                convergence[key] = generation
                patience += 1
            else:
                patience = 0
            if patience == 10:
                break
            if generations - 1 == generation:
                convergence[key] = generation
                patience = 10
                break
                
convergence_gen = np.empty((len(elite_factor),len(mutation_factor)))

fig, ax = plt.subplots()
ax.set_xticks(np.arange(len(elite_factor)))
ax.set_yticks(np.arange(len(mutation_factor)))

ax.set_xticklabels(elite_factor)
ax.set_yticklabels(mutation_factor) 

ax.set_xlabel("Mutation Factor",fontsize=18)
ax.set_ylabel("Elite Factor",fontsize=18)
ax.set_title("Convergence Generation for Elite and Mutation Factors", fontsize=18)
                
for k,i in enumerate(elite_factor):
    for l,j in enumerate(mutation_factor):
        key = "e"+str(i)+"_m"+str(j)
        convergence_gen[k,l] = convergence[key]
        test = ax.text(l,k,('%.3f' % convergence_gen[k,l]),ha="center",va="center",color="w")

im = ax.imshow(convergence_gen,origin='lower',interpolation='nearest')
cbar = ax.figure.colorbar(im,ax=ax)
cbar.set_label("generation",size=18)
plt.show()

##Generation vs "__" plots

#elite_format = ['b','g','r','c','m']
#mutation_format = ['o','^','s','x','*']
#
#            
#for k,i in enumerate(elite_factor):
#    for l,j in enumerate([0.0, 0.05, 0.10, 0.15, 0.20]):
#        key = "e"+str(i)+"_m"+str(j)
#        key_label = "Elite: "+str(i)+" Mutation: "+str(j)
##        print(key)
#        plt_format = elite_format[k] + mutation_format[l]+str("-")
#        ax = plt.plot(average[key][:,0],average[key][:,3],plt_format,markevery=100,label=key_label)
#
#plt.rcParams.update({'font.size': 12})
#plt.suptitle("Run Time for Elite and Mutation Factors", fontsize=18)
#plt.xlabel("Time [s]",fontsize=18)
#plt.ylabel("Objective",fontsize=18)
#plt.legend(bbox_to_anchor=(1.01,0.5),loc="center left")