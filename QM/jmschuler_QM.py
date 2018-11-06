# -*- coding: utf-8 -*-
"""
Created on Sat Nov 03 23:29:16 2018

@author: Jared
"""

import numpy as np
import matplotlib.pyplot as plt

# The correction bit comes from Mike Lobe, as I couldn't manage to get something that I found was accurate
# Even with the correction, cannot find what doesn't make the 

h = 1               # Reduced Planck's Constant but we are going to set it equal to 1 for this exercise.
m = 1               # mass of particle
L = 1               # Length of the well

steps = 1000

psi = 0             # Initial wavefunction value 
dpsi = 1            # Initial value of derivative of wavefunction
d2psi = 0           # Initial value of second derivative of wavefunction

n_i = 0             # Initial energy level
x_i = 0             # Initial position

correction = .000001# helps determine the energy levels 
U = 0               # potential of well
E = 4.8           # Initial energy
E_final = 300         # Maximum, final energy

dx = L/steps        # our incremental position
dE = .01            # our incremental change in energy

# Going to define the schrodinger equation immediately so I don't have to write it down every time I want to use it

def cat_equation(psi, E, m, U):
    d2psi = -((E-U)*psi)*((2*m)/(h**2))
    return d2psi

def solution_brute(n,m,l):           # Brute forces the calculation by just plugging in numbers and solving for schrodinger's equation
    E = ((n*np.pi*h)**2)/(2*m*(1**2))
    return E

Real_E =[]                           # Array of the real energy values from the solution
cat_E = []                           # Array of energy values derived from the Schrodinger equation
N = []                               # Energy level values
psi_l = []                           # Psi values
psi_arr = np.zeros(steps)            # Psi array
dpsi_arr = np.zeros(steps)           # Array for derivative of psi

while E < E_final:                   # This loop will determine the initial boundaries for the energy levels
    psi = 0 
    dpsi = 1        # from above
    for i in range(steps):
        psi = psi + psi*dx
        dpsi = dpsi + d2psi*dx
        d2psi = cat_equation(psi,E,m,U)
        psi_arr[i] = psi
        dpsi_arr[i] = dpsi
    
    before = steps-2
    after = steps-1
    if (psi_arr[before] < correction and psi_arr[after] >- correction or psi_arr[before] > correction and psi_arr[after] <- correction):
        psi_l.append(psi)
        cat_E.append(E)
        N.append(1)
        E = E + (.25*E)                     # From Zane
        plt.figure(1)
        plt.plot(psi_arr)
        plt.xlabel("Position from Nucleus")
        plt.ylabel("Wave function")
        plt.title("Wave Function")
        plt.figure(2)
        plt.plot((psi_arr)**2)
        plt.xlabel("Position from nucleus")
        plt.ylabel("d2psi/prob")
        plt.title("probability")
    else:
        E = E + dE

width = len(N)
for i in range(width):
    En = solution_brute((i+1), m, L)
    Real_E.append(En)

plt.figure(3)
plt.plot(Real_E, 'r-')
plt.plot(cat_E, 'g-')
plt.xlabel("Energy Level")
plt.ylabel("Energy")
plt.title("Actual Energy vs. Approximated Energy")
