# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 00:10:56 2018

@author: milo
"""

import numpy as np 
import matplotlib.pyplot as plt
%matplotlib inline

#initialize
N = 1000 # DEFINE number of particles
tau = 1000 # halflife
t0 = 0 # DEFINE start time
tfin = 1000 # DEFINE final time
dt = (tfin - t0)/1000 # stepsize

num = np.array([]) # make storage array for number N at time t
time = np.array([])

#loop t from t0 to tfin
for t in range(t0, tfin):
    DNDT = -N/tau
    N = N + (DNDT*dt)
    num = np.append(num, N)
    time = np.append(time, t)
    #print(t,N,tau,DNDT,dt)
plt.plot(time,num,'.')
plt.plot(time,1000*np.exp(-time/tau),'r')
