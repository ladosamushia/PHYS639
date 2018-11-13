# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 19:46:32 2018

@author: Angela
"""

#NOTE: I block commented out problem II and III so that the user doesn't wait a long time
#for the calulations to run. Delete the block comment ''' to run them.

import numpy as np
import matplotlib.pyplot as plt

#Problem I: Square in a Box

Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))

runs = 1000
for x in range(runs):
    for y in range(Ngrid):
        for z in range(Ngrid):
            if 40 <= y <= 60 and 40 <= z <= 60:
                phi_new[y][z] = 1
            elif y == 0 or z == 0 or y == Ngrid - 1 or z == Ngrid - 1:
                phi_new[y][z] = 0
            else:
                phi_new[y][z] = (phi[y - 1][z] + phi[y + 1][z] + phi[y][z - 1] + phi[y][z + 1]) / 4.0
    phi = np.copy(phi_new)

plt.figure()
plt.title("Square in a Box")
plt.imshow(phi)
plt.show()

##############################################################################################

#Problem II: Parallel Plate Capacitor 
#Remove the block comment '''  to see this section (Did this so user doesn't wait forever)

'''
Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))

runs = 1000
for x in range(runs):
    for y in range(Ngrid):
        for z in range(Ngrid):
            if y == 45 and 30 <= z <= 70:
                phi_new[y][z] = 1
            elif y == 55 and 30 <= z <= 70:
                phi_new[y][z] = -1
            elif y == 0 or z == 0 or y == Ngrid - 1 or z == Ngrid - 1:
                phi_new[y][z] = 0
            else:
                phi_new[y][z] = (phi[y - 1][z] + phi[y + 1][z] + phi[y][z - 1] + phi[y][z + 1]) / 4.0
    phi = np.copy(phi_new)

plt.figure()
plt.title("Parallel Plate Capacitor")
plt.imshow(phi)
plt.show()
'''

############################################################################################

#Problem III: Perpendicular Plates
#Remove the block comment ''' to see this section (Did this so user doesn't wait forever)

'''
Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))

runs = 1000
for x in range(runs):
    for y in range(Ngrid):
        for z in range(Ngrid):
            if y == 50 and 25 <= z <= 65:
                phi_new[y][z] = 1
            elif 30 <= y <= 70 and z == 75:
                phi_new[y][z] = -1
            elif y == 0 or z == 0 or y == Ngrid - 1 or z == Ngrid - 1:
                phi_new[y][z] = 0
            else:
                phi_new[y][z] = (phi[y - 1][z] + phi[y + 1][z] + phi[y][z - 1] + phi[y][z + 1]) / 4.0
    phi = np.copy(phi_new)

plt.figure()
plt.title("Perpendicular Plates")
plt.imshow(phi)
plt.show()
'''
