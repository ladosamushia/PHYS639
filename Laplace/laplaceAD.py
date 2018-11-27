# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 13:47:44 2018

@author: Aus
"""

import numpy as np
import matplotlib.pyplot as plt

ngrid = 100 
phi = np.zeros((ngrid,ngrid))
phi_new = np.zeros((ngrid,ngrid))

for i in range(ngrid):
    for j in range(ngrid):
        if i >= 40 and i<=60 and j >= 40 and j<=60:
            phi[i][j] = 100
        elif i == 0 or j == 0 or i == ngrid-1 or j == ngrid-1:
            phi[i][j] = 0
        else:
            phi[i][j] = (2500 - ((i-50)**2+ (j-50)**2))*100/2500
            
            
plt.imshow(phi)
    
niterations = 100
for k in range(niterations):
    for i in range(ngrid):
        for j in range(ngrid):
            if i >= 40 and i <= 60 and j >= 40 and j <=60:
                phi_new[i][j] = 100
            elif i == 0 or j == 0 or i == ngrid-1 or j == ngrid-1:
                phi_new[i][j]= 0
            else:
                phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4
    phi = np.copy(phi_new)
plt.imshow(phi)


#2 Parallel Capacitors 

for k in range(niterations):
    for i in range(ngrid):
        for j in range(ngrid):
            if i >= 40 and i <= 45 and j >= 20 and j <=80:
                phi_new[i][j] = 100
            elif i >= 70 and i <= 75 and j >= 20 and j<=80:
                phi_new[i][j]= -100
            elif i == 0 or j == 0 or i == ngrid-1 or j == ngrid-1:
                phi_new[i][j]= 0
            else:
                phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4
    phi = np.copy(phi_new)
plt.figure(2)
plt.imshow(phi)

# Perpendicular Capacitors

for k in range(niterations):
    for i in range(ngrid):
        for j in range(ngrid):
            if i >= 20 and i <= 25 and j >= 20 and j <=80:
                phi_new[i][j] = 100
            elif i >= 35 and i <= 75 and j >= 45 and j<=50:
                phi_new[i][j]= -100
            elif i == 0 or j == 0 or i == ngrid-1 or j == ngrid-1:
                phi_new[i][j]= 0
            else:
                phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4
    phi = np.copy(phi_new)
plt.figure(3)
plt.imshow(phi)


#Turned in on time, forgot that the perpendicular capacitor problem was on a different file.
