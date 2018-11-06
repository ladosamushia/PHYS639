# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:57:34 2018

@author: Aus
"""

import numpy as np 
import matplotlib.pyplot as plt

nsteps = 1000
hbar = 1.0545718e-34
m = 1
x = np.linspace(-0.5,0.5,nsteps)
dx = x[1]-x[0]
v = np.zeros(nsteps)
A = np.zeros((nsteps, nsteps))

dx2inv = 1/(dx**2)

for i in range(nsteps - 1):
    for j in range(nsteps-1):
        if i == j:
            A[i][j] = dx2inv + v[j]
        if i == j - 1 or i == j + 1:
            A[i][j] = -dx2inv*0.5
            
E, psit = np.linalg.eigh(A)
psi = np.transpose(psit)

for i in range(5):
    plt.plot(psi[i], label=str(E[i]))
plt.show()

#having a hard time trying to figure out why the curve is flat from 0-1000..