# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 17:53:44 2018

@author: Mikelobe
"""

import numpy as np
import matplotlib.pyplot as plt

#Problem 1 Radioactive Decay
N0=10 #initial number of atoms
tau=703.8 #half life of the atom
t0=0 #initial time
tfin=10*tau #final time
Nsteps=10000
t=np.linspace(t0,tfin,Nsteps+1)
N=np.zeros(Nsteps+1)
N[0]=N0
dt=(tfin-t0)/Nsteps
for i in range(1,Nsteps): #loop for ODE
    dN=-N[i-1]/tau
    N[i]=N[i-1]+dN*dt
#plotting the loop
plt.subplot(221)
plt.plot(t,N,'go')
plt.plot(t,N0*np.exp(-t/tau),'y-') #solution to ODE
plt.xlabel('time in years')
plt.ylabel('number of atoms in N_A')

#The looped plot seems to follow the actual solution's graph almost exactly,
#and it reaches zero after a long amount of time.


#Problem 2 Population Growth/Decay
alpha=6000 #birth coefficient
beta=0.6 #death coefficient
N01=10 #initial pop
Nsteps=10000
t01=0 #initial time
tfin1=1 #final time
t1=np.linspace(t01,tfin1,Nsteps+1)
N1=np.zeros(Nsteps+1)
N1[0]=N01
dt1=(tfin1-t01)/Nsteps
for i in range(1,Nsteps+1): #loop for ODE
    dN1=alpha*N1[i-1]-beta*N1[i-1]**2
    N1[i]=N1[i-1]+dN1*dt1
#plotting the loop
plt.subplot(222)
plt.plot(t1,N1,'b-')
plt.xlabel('time in years')
plt.ylabel('population of rodents')

#By looking at the ODE it can be noticed that at some population of rodents for
#any alpha/beta numbers there will be no more change, some kind of equilibrium.
#Based on the initial population of rodents the population will either rise to
#equilibrium or fall to it. But if there is no alpha value then there will only
#be a decrease in population until 0 and if there is no beta value then there 
#will only be an increase of population to infinity. A change in initial pop
#does not change where the final population will end up unless the initial is 0.