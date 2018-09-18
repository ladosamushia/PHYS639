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
for i in range(1,Nsteps+1): #loop for ODE
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
alpha=10 #birth coefficient
beta=0.03 #death coefficient
N01=100 #initial pop
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

#Problem 3 Coupled Radioactive Decay 1
NA0=30000 #initial number of atoms A
tauA=6 #half life of the atom A
NB0=5000 #initial number of atoms B
tauB=30 #half life of the atom B
t02=0 #initial time
tfin2=10*tauA #final time
Nsteps=10000
t2=np.linspace(t02,tfin2,Nsteps+1)
NA=np.zeros(Nsteps+1)
NA[0]=NA0
NB=np.zeros(Nsteps+1)
NB[0]=NB0
dt2=(tfin2-t02)/Nsteps
for i in range(1,Nsteps+1): #loop for Coupled ODE
    dNA=-NA[i-1]/tauA
    NA[i]=NA[i-1]+dNA*dt2
    dNB=(NA[i-1]/tauA)-(NB[i-1]/tauB)
    NB[i]=NB[i-1]+dNB*dt2
#graph both atom A and atom B versus time
plt.subplot(223)
plt.plot(t2,NA,'r-')
plt.plot(t2,NB,'b-')
plt.xlabel('time in years')
plt.ylabel('number of atoms')

#You can tell that the number of atoms of A will decrease until there is 0 no
#no matter the amount of initial B atoms or no matter how large or small tau A
#or tau B are. But number of atoms for B can increase if the value of tau A
#divided by tau b all times initial number of B atoms is less than the number
#of A atoms, but after it reaches the point where they equal then the number
#of B atoms will start to decrease until it reaches 0.

#Problem 4 Coupled Radioactive Decay 2
NA01=50000 #initial number of atoms A
NB01=3000 #initial number of atoms B
tau2=60 #half life of the atom
t03=0 #initial time
tfin3=10*tau2 #final time
Nsteps=10000
t3=np.linspace(t03,tfin3,Nsteps+1)
NA1=np.zeros(Nsteps+1)
NA1[0]=NA01
NB1=np.zeros(Nsteps+1)
NB1[0]=NB01
dt3=(tfin3-t03)/Nsteps
for i in range(1,Nsteps+1): #loop for Coupled ODE
    dNA1=(NB1[i-1]/tau2)-(NA1[i-1]/tau2)
    NA1[i]=NA1[i-1]+dNA1*dt3
    dNB1=(NA1[i-1]/tau2)-(NB1[i-1]/tau2)
    NB1[i]=NB1[i-1]+dNB1*dt3
#graph both atom A and atom B versus time
plt.subplot(224)
plt.plot(t3,NA1,'y-')
plt.plot(t3,NB1,'b-')
plt.xlabel('time in years')
plt.ylabel('atoms')

#It can be inferred from the coupled ODE that the number of atoms of A and the
#number of atoms of B will eventually equal the same value as time reaches
#infinity. If A atoms is bigger than B atoms, then B atoms will increase as A
#atoms will decrease and vice versa.