# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 13:47:44 2018

@author: Aus
"""
#Objective was to create a program that calculates to potential fluctuation
#as a point charge is moved farther away from the boundary. 

import numpy as np
import matplotlib.pyplot as plt

ngrid = 500
phi = np.zeros((ngrid,ngrid))
phi_new = np.zeros((ngrid,ngrid))
sig = np.zeros((ngrid,ngrid))
dx = 1

#Potential 
for i in range(ngrid):
    for j in range(ngrid):
        if i >= 40 and i<=60 and j >= 40 and j<=60:
            phi[i][j] = 100
        elif i == 0 or j == 0 or i == ngrid-1 or j == ngrid-1:
            phi[i][j] = 0
        else:
            phi[i][j] = (2500 - ((i-50)**2+ (j-50)**2))*100/2500
            
        

niterations = 100

#Poisson's equation for potential
phi = np.zeros((500,500))
r = np.zeros((500,500))
for k in range(niterations):
    for i in range(ngrid):
        for j in range(ngrid):
            if i == 100 and j == 100:
                phi_new[i][j] = 100
            elif i == 0 or j == 0 or i == ngrid-1 or j == ngrid-1:
                phi_new[i][j]= 0 
            else:
                phi_new[i][j] = ((phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4)+((sig[i][j]*dx**2)/4)
#Calculates the r value in order to visualize potential decrease as point charge moves away from potential.
    for i in range (500):
        for j in range (500):
            r[i][j] =  np.sqrt((i-100)**2 + (j-100)**2) 
    phi = np.copy(phi_new)
plt.title('r vs Potential')
plt.xlabel('Distance (r)')
plt.ylabel('Potential (phi)')
plt.plot(r,phi,'g')
plt.plot(r,100/r,'r')
#The graphs seemed to line up after tweaking some values. Used relaxation method
#and poisson's equation, and added a charge distance.



            