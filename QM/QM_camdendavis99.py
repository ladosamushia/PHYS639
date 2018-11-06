# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:58:09 2018

@author: Camden
"""

import numpy as np
import matplotlib.pyplot as plt

# Initial Conditions - Always keep uncommented

solutionCount = 0
maxSolutions = 5
boxWidth = 1.0
steps = 10000
dx = boxWidth / steps
dE = 0.1
zeroTolerance = 0.005

m = 1
E = 0.5
# lastE keeps track of last recorded energy level to avoid duplicate energies
lastE = 0
Psi_0 = 0
dPsi_0 = 1
ddPsi_0 = 0
L = 1.0

#------------------------------------------------------------------------------

# Problem 1: Infinite Potential Well

# Arrays for solutions of Psi and Energy level
Psi_Solutions = [[] for n in range(maxSolutions)]
E_Solutions = np.zeros(maxSolutions)

# Changes a function by a given factor to make the graph better
def normalize_a_little(f, k):
    for i in range(steps):
        f[i] *= k
        
# Loops while all solutions are not found
while solutionCount < maxSolutions:
    
    # (Re)Initializes all arrays
    Psi = np.zeros(steps)
    dPsi = np.zeros(steps)
    ddPsi = np.zeros(steps)
    Psi[0] = Psi_0
    dPsi[0] = dPsi_0
    ddPsi[0] = ddPsi_0
    
    # Creates next value for each array
    for i in range(steps - 1):
        dPsi[i + 1] = dPsi[i] + ddPsi[i] * dx
        Psi[i + 1] = Psi[i] + dPsi[i] * dx
        ddPsi[i + 1] = -2 * m * E * Psi[i]
    
    # Runs if a nonduplicate solution is found
    if abs(Psi[steps - 1]) < zeroTolerance and abs(E - lastE) > 2:
        # Adds array/value to solutions
        Psi_Solutions[solutionCount] = Psi
        E_Solutions[solutionCount] = E
        solutionCount += 1
        
        # Increases precision for higher energy levels
        zeroTolerance -= 0.0006 / 5.0
        # Updates last recorded energy level
        lastE = E
    
    # Increments current energy level
    E += dE

# Defines x coordinates
xVals = np.linspace(-L/2, L/2, steps)
# Declares probablilities
P = [np.zeros(steps) for i in range(maxSolutions)]
# Loops through each solution
for i in range(solutionCount):
    # Loops through every value in the array
    for j in range(steps):
        # Squares the value to convert it to probability
        P[i][j] = Psi_Solutions[i][j] * Psi_Solutions[i][j]
    # Multiplies array by a certain value to make graph better
    normalize_a_little(P[i], 0.15 + 0.4 * i)
    plt.plot(xVals, P[i])
    
plt.title("Psi^2")
plt.axis([-L/2, L/2, 0, 0.016])
plt.legend()
plt.show()

print("Energy levels:", E_Solutions)

#------------------------------------------------------------------------------

# Problem 2: Wall Inside a Well
# My functions are not symmetric and I can't figure out why for the life of me.
# I've tried increasing the step count massively and cannot fix it.

## Defines wall conditions
#wallWidth = 0.1
#wallHeight = 30.0
#
## Arrays for solutions of Psi and Energy level
#Psi_Solutions = [[] for n in range(maxSolutions)]
#E_Solutions = np.zeros(maxSolutions)
#
## Energy potential function
#def V(x):
#    # Potential is only nonzero in certain interval
#    if x > -wallWidth / 2 and x < wallWidth < 2:
#        return wallHeight
#    return 0
#
## Changes a function by a given factor to make the graph better
#def normalize_a_little(f, k):
#    for i in range(steps):
#        f[i] *= k
#        
## Loops while all solutions are not found
#while solutionCount < maxSolutions:
#    
#    # (Re)Initializes all arrays
#    x = np.zeros(steps)
#    Psi = np.zeros(steps)
#    dPsi = np.zeros(steps)
#    ddPsi = np.zeros(steps)
#    x[0] = -L/2
#    Psi[0] = Psi_0
#    dPsi[0] = dPsi_0
#    ddPsi[0] = ddPsi_0
#    
#    # Creates next value for each array
#    for i in range(steps - 1):
#        dPsi[i + 1] = dPsi[i] + ddPsi[i] * dx
#        Psi[i + 1] = Psi[i] + dPsi[i] * dx
#        ddPsi[i + 1] = -2 * m * (E - V(x[i])) * Psi[i]
#        x[i + 1] = x[i] + dx
#    
#    # Runs if a nonduplicate solution is found
#    if abs(Psi[steps - 1]) < zeroTolerance and abs(E - lastE) > 2:
#        # Adds array/value to solutions
#        Psi_Solutions[solutionCount] = Psi
#        E_Solutions[solutionCount] = E
#        solutionCount += 1
#        
#        # Increases precision for higher energy levels
#        zeroTolerance -= 0.0006 / 5.0
#        # Updates last recorded energy level
#        lastE = E
#    
#    # Increments current energy level
#    E += dE
#
## Declares probablilities
#P = [np.zeros(steps) for i in range(maxSolutions)]
## Loops through each solution
#for i in range(solutionCount):
#    # Loops through every value in the array
#    for j in range(steps):
#        # Squares the value to convert it to probability
#        P[i][j] = Psi_Solutions[i][j] * Psi_Solutions[i][j]
#    # Multiplies array by a certain value to make graph better
#    normalize_a_little(P[i], 0.15 + 0.4 * i)
#    plt.plot(x, P[i])
#    
#plt.title("Psi^2")
#plt.axis([-L/2, L/2, 0, 0.016])
#plt.legend()
#plt.show()
#
#print("Energy levels:", E_Solutions)