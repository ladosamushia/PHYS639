# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 23:29:06 2018

@author: Angela
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate 

steps = 100

A = np.loadtxt('DataAnalysis.txt')

Ei = A[:,0] #Makes E column 1 of the text file
Ni = A[:,1]
Nd = A[:,2]

kai = np.zeros((steps,steps))
E0 = np.linspace(0,20,steps)

#We used A as the data file variable so let D repersent A in the equation.
for i in range(steps):
    D = np.linspace(0,1,steps) 
    for j in range(steps):  # N = B + A*exp(-[E-E0]**2)
        N = 1 + D[j] * np.exp(-(Ei-E0[i])**2)
        kai[i][j] = np.sum((N-Ni)**2/Nd**2)

imin, jmin = np.where(kai == np.min(kai))

E0min = E0[imin[0]]
Dmin = D[jmin[0]]
kaimin = np.min(kai)
Nmin = 1 + Dmin * np.exp(-(Ei-E0min)**2)

plt.errorbar(Ei, Ni, Nd, fmt = 'o')
plt.plot(Ei,Nmin)
plt.xlabel('Energy')
plt.ylabel('Number of Photons')
plt.show()

#Here we print the best fit values
print('A =', Dmin)
print('E0 =', E0min)
print('kai =', kaimin)

#########################################################################################

#Part II: Error Bars
#Just a note here: Mich is actually 'Hast' I did this to make a joke later on.
Du = (kai[imin, jmin + 1] + kai[imin, jmin - 1] - 2 * kai[imin, jmin]) / (D[jmin + 1] - D[jmin])**2
Mich = (kai[imin + 1, jmin] + kai[imin - 1, jmin] - 2 * kai[imin, jmin]) / (E0[imin + 1] - E0[imin])**2
DuHast = (kai[imin - 1, jmin - 1] + kai[imin + 1, jmin + 1] - kai[imin - 1, jmin + 1] - kai[imin + 1, jmin - 1]) / (4*(D[jmin + 1] - D[jmin])*(E0[imin + 1] - E0[imin]))

Hess = np.zeros((2,2))
Hess[0][0], Hess[0][1], Hess[1][0], Hess[1][1] = Du/2, DuHast/2, DuHast/2, Mich/2
#In the above I referenced a German phrase, "Du hast mich - You have me".

C = np.absolute(np.linalg.inv(Hess))
sigmas = np.sqrt(C.diagonal())

print('\nError:', sigmas)
