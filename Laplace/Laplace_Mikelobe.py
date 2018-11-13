# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 17:11:05 2018

@author: mikelobe
"""

import numpy as np
import matplotlib.pyplot as plt


#Problem 1: Square in a Box

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

Niterations = 1000
for k in range(Niterations):
    for i in range(Ngrid):
        for j in range(Ngrid):
            if i >= 40 and i <=60 and j >=40 and j <=60:
                phi_new[i][j] = 100
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi_new[i][j] = 0
            else:
                phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
    phi = np.copy(phi_new)
plt.clf()
plt.figure(1)
plt.imshow(phi)
plt.title("Square in a Box")
plt.figure(2) #doesnt seem to want to work
plt.plot(phi)

#Problem 2: Parellel Plate Capacitor

phi2 = np.zeros((Ngrid,Ngrid))
phi_new2 = np.zeros((Ngrid,Ngrid))

for i in range(Ngrid):
    for j in range(Ngrid):
        if i >= 25 and i <=75 and j==30:
            phi2[i][j] = 100
        elif i>=25 and i<=75 and j==70:
            phi2[i][j] = -100
        elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
            phi2[i][j] = 0
        else:
            phi2[i][j] = 0

plt.imshow(phi2)

Niterations = 1000
for k in range(Niterations):
    for i in range(Ngrid):
        for j in range(Ngrid):
            if i >= 25 and i <=75 and j==30:
                phi_new2[i][j] = 100
            elif i>=25 and i<=75 and j==70:
                phi_new2[i][j] = -100
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi_new2[i][j] = 0
            else:
                phi_new2[i][j] = (phi2[i-1][j] + phi2[i+1][j] + phi2[i][j-1] + phi2[i][j+1])/4.0
    phi2 = np.copy(phi_new2)
plt.clf()
plt.figure(3)
plt.imshow(phi2)
plt.title("Parallel Plates")
plt.figure(4) #doesnt seem to want to work
plt.plot(phi2)

#Problem 3: Perpendicular Plates

phi3 = np.zeros((Ngrid,Ngrid))
phi_new3 = np.zeros((Ngrid,Ngrid))

for i in range(Ngrid):
    for j in range(Ngrid):
        if i >= 20 and i <=40 and j==30:
            phi3[i][j] = 100
        elif j>=60 and j<=80 and i==60:
            phi3[i][j] = -100
        elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
            phi3[i][j] = 0
        else:
            phi3[i][j] = 0

plt.imshow(phi)

Niterations = 1000
for k in range(Niterations):
    for i in range(Ngrid):
        for j in range(Ngrid):
            if i >= 20 and i <=40 and j==30:
                phi_new3[i][j] = 100
            elif j>=60 and j<=80 and i==60:
                phi_new3[i][j] = -100
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi_new3[i][j] = 0
            else:
                phi_new3[i][j] = (phi3[i-1][j] + phi3[i+1][j] + phi3[i][j-1] + phi3[i][j+1])/4.0
    phi3 = np.copy(phi_new3)
plt.clf()
plt.figure(5)
plt.imshow(phi3)
plt.title("Perpendicular Plates")
plt.figure(6)
plt.plot(phi3)
