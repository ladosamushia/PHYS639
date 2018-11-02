# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 13:46:37 2018

@author: Lado
"""
import numpy as np
import matplotlib.pyplot as plt

Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))

for i in range(Ngrid):
    for j in range(Ngrid):
        if i >= 40 and i <=60 and j >=40 and j <=60:
            phi[i][j] = 100
        elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
            phi[i][j] = 0
        else:
            phi[i][j] = 0

plt.imshow(phi)

Niterations = 10000
for k in range(Niterations):
    print(k)
    for i in range(Ngrid):
        for j in range(Ngrid):
            if i >= 40 and i <=60 and j >=40 and j <=60:
                phi_new[i][j] = 100
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi_new[i][j] = 0
            else:
                phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
    plt.pause(0.001)
    phi = np.copy(phi_new)
    plt.clf()
    plt.imshow(phi)