# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 2018 by Philip Lucas
#10.3
Solving a particle in a box with differential equations 
"""

import numpy as np
import matplotlib.pyplot as plt
steps = 10000000
h_bar = 1 # 6.582119514e-16 #reduced planks constant in eVs
Me = 1 # 510998.9461 # mass of an electron in eV/(C^2)
coop = ((h_bar)**2)/(2*Me) # Coefficent for the Hamiltonian Operator
E = []
Energylist = []
psilist = []
L = 1
n = 0 
x = 0
aboutzero = 1e-20
energy = 1
step = 1000

psi = np.zeros(step)
dpsi = np.zeros(step)
ddpsi = np.zeros(step)
dpsi = 1 
ddpsi = 0.0
dx = L/step
dE = 0.1
for j in range(step):
    psi[j] = psi[j-1] + dpsi*dx
    ddpsi = -2*energy*psi[j-1] 
    dpsi += ddpsi*dx
    print ddpsi , dpsi
    while energy < 600:
        if psi[998] < aboutzero and psi[999] > -aboutzero or psi[998] > aboutzero and psi[999] < -aboutzero:
            psilist.append(psi)
            Energylist.append(energy)
            energy += energy
        else:
            energy += dE
print Energylist 
def E_n(n): #to validate a simple box
    return((h_bar*n*np.pi)**2)/(2*Me*(L)**2)
def Psi_sol(x , A, k ): #wave function solution
    return  A*np.sin(k*x)
for i in range(10): # for comparison with approximate PDE solution for a 1D infinite well
   E_n(i) 
   E.append(E_n(i))
print E
plt.figure(1)
plt.plot(E)
plt.plot(Energylist)
plt.xlabel (" n-Level (Unitless integer) ")
plt.ylabel (" Energy(n) (eV) ")
plt.title (" Energy level ")
plt.figure(2)
