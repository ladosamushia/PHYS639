# -*- coding: utf-8 -*-
"""
Created on Mon Oct 01 21:48:11 2018

@author: mikelobe
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as random

#Problem 1: 1D Random Walk

N=1000 #number of movements
def randwalk(steps,movements,p=[0.5,0.5]): #function for the random movement
    sum=0 #initial sum
    for i in range(movements):
        sum += np.abs(np.sum(random.choice([-1,1],steps,p=p))) #increasing the sum of position as particle moves
    return sum / movements
steps=range(1,250) #number of movements of the particle
fair_avg=np.zeros(len(steps)) #filling the array with the string of steps
for i in steps: #loop for fair movement of the particle 50/50
    fair_avg[i-1]=randwalk(i,N)
plt.plot(steps,fair_avg,'b-')

#Problem 2: 1D Biased Random Walk

def randwalk(steps,movements,p=[0.5,0.5]): #function for the random movement
    sum=0 #initial sum
    for i in range(movements): 
        sum += np.abs(np.sum(random.choice([-1,1],steps,p=p))) #increasing the sum of position as particle moves
    return sum / movements
steps=range(1,250) #number of steps made by the particle
biased_avg=np.zeros(len(steps))
for i in steps: #loop for biased movement of the particle 75/25
    biased_avg[i-1]=randwalk(i,N,p=[0.75,0.25])
plt.plot(steps,biased_avg,'g-')
plt.xlabel('steps')
plt.ylabel('absolute average')