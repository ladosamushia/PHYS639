
"""
Created on Tue Oct 23 2018 by Philip Lucas
Solving a particle in a box with differential equations
Made with Python 2.7
"""

# This code appears to work, I think I might be able to narrow down to more accurate solutions in a shorter time. 
# I want to make a loop for two different dE. On to zero in close too quickly and once there 
# Finely dial into a solution. I haven't been able to make a loop that works just yet, that 
# doesn't break my code, yet. 

# Also this code take a long to run as is 

import numpy as np
import matplotlib.pyplot as plt
steps = 1000
h_bar = 1.0 # 6.582119514e-16 #reduced planks constant in eVs
Me = 1.0 # 510998.9461 # mass of an electron in eV/(C^2)
coop = ((h_bar)**2)/(2*Me) # Coefficent for the Hamiltonian Operator
E = []
Energylist = []
psilist = []
N=[]
L = 1.0
n = 0 
x = 0
aboutzero = 0.00000001
energy = 4.8
ENERGY = 200
step = 1000
psi = np.zeros(step)
dpsi = np.zeros(step)
ddpsi = np.zeros(step)
dx = L/step
dE = 0.01
while energy < ENERGY:
    dpsi = 1.0 
    ddpsi = 0.0
    for j in range(1,step):
        psi[j] = psi[j-1] + dpsi*dx
        ddpsi = -2*energy*psi[j-1] 
        dpsi += ddpsi*dx   
    if psi[998] < aboutzero and psi[999] > -aboutzero or psi[998] > aboutzero and psi[999] < -aboutzero:
        psilist.append(psi)
        N.append(1)
        Energylist.append(energy)
        energy += (0.25)*energy
        plt.figure(1)
        plt.plot(psi)
        plt.xlabel (" Position " " L/step " )
        plt.ylabel (" Psi ")
        plt.title (" Wavefunction ")
        plt.figure(2)
        plt.plot(psi**2)
        plt.xlabel (" Position " " L/step ")
        plt.ylabel (" P(x) = Psi**2 ")
        plt.title (" Probability")
    else:
        energy += dE      
# For comparision of  solutions to Test Code
def E_n(n): #to validate a simple box
    return((h_bar*n*np.pi)**2)/(2*Me*(L)**2)
Nrange = len(N)
for k in range( 1, Nrange + 1 ): # for comparison with approximate PDE solution for a 1D infinite well
   E_n(k) 
   E.append(E_n(k))
print "Analytical", E , ","
print "Approximation" ,  Energylist
plt.figure(3)
plt.plot(E)
plt.plot(Energylist)
plt.xlabel (" n-Level (Unitless integer) ")
plt.ylabel (" Energy(n) (eV) ")
plt.title (" Energy level ")
