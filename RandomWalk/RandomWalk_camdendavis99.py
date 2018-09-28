# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:01:23 2018

@author: Camden
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#------------------------------------------------------------------------------

# Problem 1: 1D Random Walk

# Creates bounds and step arrays
trials = 100
stepLimit = 10000
steps = np.zeros(stepLimit)
stepSums = np.zeros(trials)

for i in range(trials):
    for j in range(stepLimit):
        # Creates random choice between -1 and 1
        steps[j] = np.random.choice([-1, 1])
        stepSums[i] += steps[j]
    stepSums[i] = abs(stepSums[i])

# Graph of distance from origin 
plt.plot(stepSums, 'ro')
plt.xlabel("Trial")
plt.ylabel("Distance from 0")
plt.title("Step sums")

#------------------------------------------------------------------------------

# Problem 2: 1D Biased Random Walk

## Creates bounds and step arrays
#trials = 100
#stepLimit = 10000
#steps = np.zeros(stepLimit)
#stepSums = np.zeros(trials)
#
#for i in range(trials):
#    for j in range(stepLimit):
#        # Creates random choice between -1 and 1
#        steps[j] = np.random.choice([-1, 1, 1, 1])
#        stepSums[i] += steps[j]
#    stepSums[i] = abs(stepSums[i])
#
## Graph of distance from origin
#plt.plot(stepSums, 'ro')
#plt.xlabel("Trial")
#plt.ylabel("Distance from 0")
#plt.title("Step sums")

#------------------------------------------------------------------------------

# Problem 3: 3D Random Walk

#bound = 500
#distance = np.zeros(bound)
#
#for i in range(1, bound):
#    # Initializes step limit, coordinate arrays, and step arrays
#    stepLimit = i
#    X = np.zeros(stepLimit)
#    Y = np.zeros(stepLimit)
#    Z = np.zeros(stepLimit)
#    xSteps = np.zeros(stepLimit)
#    ySteps = np.zeros(stepLimit)
#    zSteps = np.zeros(stepLimit)
#    
#    for j in range(1, stepLimit):
#        # Creates random choice between 1 and 6
#        step = np.random.randint(1, 7)
#        
#        # Assigns each choice to a positive or negative increment on one axis
#        if step == 1:
#            xSteps[j] = -1
#        elif step == 2:
#            xSteps[j] = 1
#        elif step == 3:
#            ySteps[j] = -1
#        elif step == 4:
#            ySteps[j] = 1
#        elif step == 5:
#            zSteps[j] = -1
#        elif step == 6:
#            zSteps[j] = 1
#    
#        # Updates coordinates
#        if j == 0:
#            X[j] = xSteps[j]
#            Y[j] = ySteps[j]
#            Z[j] = zSteps[j]
#        else:
#            X[j] = X[j - 1] + xSteps[j]
#            Y[j] = Y[j - 1] + ySteps[j]
#            Z[j] = Z[j - 1] + zSteps[j]
#    
#    # Calculates distance from origin
#    Xf = X[stepLimit - 1]
#    Yf = Y[stepLimit - 1]
#    Zf = Z[stepLimit - 1]
#    distance[i] = np.sqrt(Xf*Xf + Yf*Yf + Zf*Zf)
#
## Graph of distance after a given number of steps
#plt.plot(distance, 'r')
#plt.xlabel("Number of steps")
#plt.ylabel("Distance from origin")
#plt.title("Distance from origin per number of steps")
#
## 3D graph of path taken
#fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax.scatter3D(X, Y, Z, c=Z, cmap='Greens');
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')
#axLim = bound / 20
#ax.set_xlim(-axLim, axLim)
#ax.set_ylim(-axLim, axLim)
#ax.set_zlim(-axLim, axLim)

#------------------------------------------------------------------------------

# Problem 4: 3D Random Walk with Random Direction

#bound = 500
#distance = np.zeros(bound)
#
#for i in range(1, bound):
#    # Initializes step limit, coordinate arrays, and step arrays
#    stepLimit = i
#    X = np.zeros(stepLimit)
#    Y = np.zeros(stepLimit)
#    Z = np.zeros(stepLimit)
#    xSteps = np.zeros(stepLimit)
#    ySteps = np.zeros(stepLimit)
#    zSteps = np.zeros(stepLimit)
#    
#    for j in range(1, stepLimit):
#        # Creates random choice between 1 and 6
#        theta = 2 * np.pi * np.random.random()
#        phi = np.arccos(2 * np.random.random() - 1)
#        
#        # yeah
#        xSteps[j] = np.sin(theta) * np.cos(phi)
#        ySteps[j] = np.sin(theta) * np.sin(phi)
#        zSteps[j] = np.cos(theta)
#    
#        # Updates coordinates
#        if j == 0:
#            X[j] = xSteps[j]
#            Y[j] = ySteps[j]
#            Z[j] = zSteps[j]
#        else:
#            X[j] = X[j - 1] + xSteps[j]
#            Y[j] = Y[j - 1] + ySteps[j]
#            Z[j] = Z[j - 1] + zSteps[j]
#    
#    # Calculates distance from origin
#    Xf = X[stepLimit - 1]
#    Yf = Y[stepLimit - 1]
#    Zf = Z[stepLimit - 1]
#    distance[i] = np.sqrt(Xf*Xf + Yf*Yf + Zf*Zf)
#
## Graph of distance after a given number of steps
#plt.plot(distance, 'r')
#plt.xlabel("Number of steps")
#plt.ylabel("Distance from origin")
#plt.title("Distance from origin per number of steps")
#
## 3D graph of path taken
#fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax.scatter3D(X, Y, Z, c=Z, cmap='Greens');
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')
#axLim = bound / 20
#ax.set_xlim(-axLim, axLim)
#ax.set_ylim(-axLim, axLim)
#ax.set_zlim(-axLim, axLim)








