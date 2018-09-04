# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:11:57 2018

@author: Jared
"""
# Warmup Homework Problem 1
# dN/dt = -N/T    where T is tau
# Solving the differential equation gives us...
# N(t) = No*(e^(-t/T))

# No = Original number of isotope
# This gives us an exponential decay, which is what we expected and want.
# Small Tau means the graph decays extremely fast, while large Tau means the graph decays slowly. Also what we want.
# To numerically solve, let's set our boundary conditions.
# Only have one boundary condition because first order ODE, which is No. Let's also set dt to 10000 steps.
# dNo = -No/T
# Number of isotopes at step 1


# To solve this in PYTHON...

# Step 1: Import libraries
import numpy as np
import matplotlib.pyplot as plt
#%mathplotlib inline                # ONLY NEED THIS IF YOU ARE IN JUPYTER, NOT SPYDER
#

# Step 2: indicate global variables/initial conditions and steps
N0 = 10
tau = 703.8
tini = 0
tfin = 10*tau
Nsteps = 10000
t = np.linspace(tini,tfin,Nsteps+1)    # Start, Stop, Increments
N = np.zeros(Nsteps+1)
N[0]=N0
#

#Step 3: Set up derivatives and values
dt = (tfin-tini)/Nsteps
#

# Step 4:Set up the loop
for i in range(1,Nsteps):
    dN = -N[i-1]/tau
    N[i] = N[i-1] + dN*dt
#
    
# Step 5: Plot the results
plt.plot(t,N,'go')
plt.plot(t,N0*np.exp(-t/tau),'y-')
plt.xlabel('Time in years')
plt.ylabel('Number of atoms in N_A')



