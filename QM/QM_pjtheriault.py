# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 13:33:31 2018

@author: Angela
"""

#Infinite Square Well

# -h**2/2m * A**2 = E*A Schrodinger's Equation

#Infintie Square well goes from 0 to L
#V=0 inside 0 to a and infinity outside these bounds


import numpy as np
import matplotlib.pyplot as plt

N=5 #Controls energy levels

#inital setup
steps = 1000
L=1
dx = L/steps
dE = 0.1
E=dE
n=1

x=np.linspace(0, 1, int(steps) + 1)
finalpsi = [1, 2, 3]

while n <= N:
    
    p = np.zeros(int(steps) + 1)
    dp = 1
    
    for i in range(int(steps)):
        p[i + 1] = p[i] + dp*dx
        dp -= 2*E*p[i + 1]*dx
    
    finalpsi.append(np.abs(p[-1]))
    
    if finalpsi[-3] >= finalpsi[-2] <= finalpsi[-1]:
        print('Energy', n, E - dE)
        plt.plot(x,p)
        plt.xlabel('X')
        plt.ylabel('Psi')
        plt.title('Modulus Square')
        n += 1
    
    E += dE





