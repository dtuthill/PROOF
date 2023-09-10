#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:33:10 2019

@author: Daniel Tuthill
"""

import numpy as np

#see jupyter_notebook for alpha formula used in calc_alpha

def calc_alpha (population,intensity_sqrt):
    y = intensity_sqrt[2:]*np.sin(population[:,1:-1]-population[:,2:]) + intensity_sqrt[:-2]*np.sin(population[:,1:-1]-population[:,:-2])
    x = intensity_sqrt[2:]*np.cos(population[:,1:-1]-population[:,2:]) - intensity_sqrt[:-2]*np.cos(population[:,1:-1]-population[:,:-2])
    return np.arctan2(y,x)

def calc_fitness (alpha,alpha_exp,intensity):
    reciprocal_objective = np.reciprocal(np.dot(np.square(alpha-alpha_exp),intensity))
    objective = np.dot(np.square(alpha-alpha_exp),intensity)
    return reciprocal_objective*np.max(reciprocal_objective), objective