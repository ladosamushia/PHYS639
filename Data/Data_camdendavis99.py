# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:43:41 2018

@author: Camden
"""

# All code should be left uncommented

import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------

# Loads data from text file
Data = np.loadtxt("DataAnalysis.txt")

# Gets values of E, N, and SN from data
E = Data[:,0]
N = Data[:,1]
SN = Data[:,2]

# Initial Conditions and initial arrays
trials = 100
Aincrement = 0.01
Eincrement = 0.2
X2 = np.zeros((trials, trials))
A = np.linspace(0, trials * Aincrement, trials, endpoint = False)
E0 = np.linspace(0, trials * Eincrement, trials, endpoint = False)

# More initial conditions
B = 1
minX2 = 999999
bestA = 0
bestE0 = 0
mini = 0
minj = 0
# Tracks x index
i = 0

# Loops through values of E0 to test
for curE0 in E0:
    # Tracks y index
    j = 0
    
    # Loops through values of A to test
    for curA in A:
        curX2 = 0
        
        # Sum of values to calculate Chi^2 (X2)
        for k in range(len(E)):
            curNth = B + curA*np.exp(-(E[k] - curE0)**2)
            curX2 += ((curNth - N[k])**2 / (SN[k] * SN[k]))
        # Stores current value of X2 in array
        X2[i][j] = curX2
        
        # Updates best values if X2 is a minimum
        if curX2 < minX2:
            minX2 = curX2
            bestA = curA
            bestE0 = curE0
            mini = i
            minj = j
            
        # Increments y index
        j += 1
        
    # Increments x index
    i += 1
    
# Prints best values
print("Best Fit Values:")
print("\tX^2: {:.2f}\n\tA:   {:.2f}\n\tE0:  {:.2f}".format(minX2, bestA, bestE0))

# Some nice plots
plt.figure(1)
plt.errorbar(E, N, SN, fmt='o')
plt.plot(E, B + bestA*np.exp(-(E - bestE0)**2))
plt.figure(2)
plt.imshow(X2)

#---------------------------------------

# Problem 2: Error Bars

Hessian = np.zeros((2, 2))

# Calculates didi, didj, and djdj
didi = X2[mini + 1][minj] + X2[mini - 1][minj] - ((2 * X2[mini][minj]) / (E0[mini + 1] - E0[mini]))
didj = (X2[mini - 1][minj - 1] + X2[mini + 1][minj + 1] - X2[mini - 1][minj + 1] - X2[mini + 1][minj - 1]) / (4 * (A[minj + 1] - A[minj]) * (E0[mini + 1] - E0[mini]))
djdj = X2[mini][minj + 1] + X2[mini][minj - 1] - ((2 * X2[mini][minj]) / (A[minj + 1] - A[minj]))

# Assigns calculated values to the Hessian
Hessian[0][0] = -0.5 * didi
Hessian[1][0] = -0.5 * didj
Hessian[0][1] = Hessian[1][0]
Hessian[1][1] = -0.5 * djdj

# Finds inverse of Hessain, then inverse, and prints
C = np.linalg.inv(Hessian)
Sigmas = np.sqrt(C.diagonal())
print("\nError bars:\n\t" + str(Sigmas[0]) + "\n\t" + str(Sigmas[1]))

            
    


