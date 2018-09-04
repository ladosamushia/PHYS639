# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:39:35 2018

@author: Jared
"""

# Warmup Homework Problem 2
# dN/dt = aN - BN^2

# Step 1: Import libraries
import numpy as np
import matplotlib.pyplot as plt

#Step 2: Indiciate global variables and initial conditions (if applicable)
N0 = 100
a = .95
B = .01
tini = 0.0                           # Initial time
tfin = 15.0                        # Final time
Nsteps = 10000

t = np.linspace(tini, tfin, Nsteps+1)
N = np.zeros(Nsteps+1)
N[0]=N0
dt = (tfin-tini)/Nsteps

for i in range(1, Nsteps+1):
    dN = a * N[i-1] - B * (N[i-1]**2)
    N[i] = N[i-1] + dN * dt
    #print(i,dN,a,B,dt,N[i],N[i-1])
    
    
plt.plot(t,N,'r-')
plt.xlabel('Time in years')
plt.ylabel('Population')



