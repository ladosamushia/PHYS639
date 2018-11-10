# -*- coding: utf-8 -*-
"""
Created on Tue Nov 06 13:05:59 2018

@author: Blaine Fry
"""
# Phys 639
# Laplace Equation

from matplotlib import pyplot as plt
from matplotlib import quiver
import numpy as np
from numpy import random
import itertools

# make something to clean up E-field arrows for the quiver function
def clean_arrows(input_array,scale_factor,every_other):
    # flatten stuff so it's easier to work with the indexes
    old_list = input_array.tolist()
    flat_list = list(itertools.chain(*old_list))
    # go through and scale stuff
    new_list = []
    for i in range(len(flat_list)):
        if i%every_other == 0 :
            new_list.append(flat_list[i]/float(scale_factor))
        else:
            new_list.append(0)
    # put it back in an array
    new_array = np.asarray(new_list)
    newer_array = np.reshape(new_array,(-1,100))
    return newer_array

plot_E = True # turn on or off the plot of Electric Field
pause_time = 4

"""
Problem: Square in a box (lvl*)
Solve for the potentials in a grounded box with a square in the middle
at a higher potential
"""

# make a 2D grid
Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
# set boundary/region solutions
# square in middle @ 100 V
for i in range(Ngrid):
    for j in range(Ngrid):
        if i >= 40 and i <=60 and j >= 40 and j <=60:
            phi[i][j] = 1
        elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
            phi[i][j] = 0
        else:
            phi[i][j] = random.rand()*1

# 'relax' the solutions
Nsteps = 100
for k in range(Nsteps):
    new_phi = np.copy(phi)
    for i in range(Ngrid-1):
        for j in range(Ngrid-1):
            if i >= 40 and i <=60 and j >= 40 and j <=60:
                new_phi[i][j] = 1
            elif i == 0 or j == 0 or j == Ngrid-1 or j == Ngrid-1:
                new_phi[i][j] = 0
            else: # including more neighbors makes it converge more quickly...
                new_phi[i][j] = ((2./3.)*(phi[i-1][j]+phi[i+1][j]+phi[i][j+1]+phi[i][j-1])+(1./3.)*(phi[i+1][j+1]+phi[i+1][j-1]+phi[i-1][j+1]+phi[i-1][j-1]))/4.0
    phi = np.copy(new_phi)
    phi1 = np.copy(new_phi)
Ex1,Ey1 = np.gradient(phi1)
plt.imshow(phi1)
if plot_E:
    plt.quiver(-clean_arrows(Ey1,2,5),clean_arrows(Ex1,2,5),scale=1)
     
"""
Problem: Parallel Plates (lvl*)
"""

# set boundary/region solutions
for i in range(Ngrid):
    for j in range(Ngrid):
        if i >= 45 and i <= 46 and j >= 20 and j <=80:
            phi[i][j] = 1
        elif i >= 54 and i <= 55 and j >= 20 and j <=80:
            phi[i][j] = -1
        elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
            phi[i][j] = 0
        else:
            phi[i][j] = random.rand()*0.5

# 'relax' the solutions
Nsteps = 100
for k in range(Nsteps):
    new_phi = np.copy(phi)
    for i in range(Ngrid-1):
        for j in range(Ngrid-1):
            if i >= 45 and i <= 46 and j >= 20 and j <=80:
                new_phi[i][j] = 1
            elif i >= 54 and i <= 55 and j >= 20 and j <=80:
                new_phi[i][j] = -1
            elif i == 0 or j == 0 or j == Ngrid-1 or j == Ngrid-1:
                new_phi[i][j] = 0
            else:
                new_phi[i][j] = ((2./3.)*(phi[i-1][j]+phi[i+1][j]+phi[i][j+1]+phi[i][j-1])+(1./3.)*(phi[i+1][j+1]+phi[i+1][j-1]+phi[i-1][j+1]+phi[i-1][j-1]))/4.0
    phi = np.copy(new_phi)
    phi2 = np.copy(new_phi)
plt.pause(pause_time)
plt.clf()
Ex2,Ey2 = np.gradient(phi2)
plt.imshow(phi2)
if plot_E:
    plt.quiver(-clean_arrows(Ey2,4,5),clean_arrows(Ex2,4,5),scale=1)

"""
Problem: Perpindicular Plates (lvl*)
"""

# set boundary/region solutions
for i in range(Ngrid):
    for j in range(Ngrid):
        if i >= 10 and i <= 11 and j >= 20 and j <=80:
            phi[i][j] = 1
        elif i >= 20 and i <= 80 and j >= 49 and j <=51:
            phi[i][j] = -1
        elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
            phi[i][j] = 0
        else:
            phi[i][j] = random.rand()*0.5

# 'relax' the solutions
Nsteps = 100
for k in range(Nsteps):
    new_phi = np.copy(phi)
    for i in range(Ngrid-1):
        for j in range(Ngrid-1):
            if i >= 10 and i <= 11 and j >= 20 and j <=80:
                phi[i][j] = 1
            elif i >= 20 and i <= 80 and j >= 49 and j <=51:
                phi[i][j] = -1 
            elif i == 0 or j == 0 or j == Ngrid-1 or j == Ngrid-1:
                new_phi[i][j] = 0
            else:
                new_phi[i][j] = ((2./3.)*(phi[i-1][j]+phi[i+1][j]+phi[i][j+1]+phi[i][j-1])+(1./3.)*(phi[i+1][j+1]+phi[i+1][j-1]+phi[i-1][j+1]+phi[i-1][j-1]))/4.0
    phi = np.copy(new_phi)
    phi2 = np.copy(new_phi)
plt.pause(pause_time)
plt.clf()
Ex2,Ey2 = np.gradient(phi2)
plt.imshow(phi2)
if plot_E:
    plt.quiver(-clean_arrows(Ey2,4,5),clean_arrows(Ex2,4,5),scale=1)


