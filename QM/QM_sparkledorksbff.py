# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:12:46 2018

@author: jessi
"""

#Jessica Pietrowski
#Modeling a particle in an infinite well
import numpy as np
import matplotlib.pyplot as plt
steps = 1000
h_bar = 1 # 6.582119514e-16 #reduced planks constant in eVs
Me = 1 # 510998.9461 # mass of an electron in eV/(C^2)
coop = ((h_bar)**2)/(2*Me) # Coefficent for the Hamiltonian Operator
E = [] #Blank set of energy values
Energylist = [] #Blank list for energy lists
psilist = [] #blank list for psi values
N = [] #Blank list for particle numbers
L = 1 #length of the box
n = 0  #energy state number
x = 0 #x position
aboutzero = 0.00000001
energy = 4.8 #expected energy for state number 1
ENERGY = 200 #energy cap to use
step = 1000 #step size

psi = np.zeros(step) #make an array of psi values
dpsi = np.zeros(step) #make an array of psi derivative values
ddpsi = np.zeros(step) #make an array of psi second derivative values
dx = L/step #x derivative value
dE = 0.01 #energy derivative
while energy < ENERGY: #while energy is below the energy cap level
    dpsi = 1 #define value for psi derivative
    ddpsi = 0.0 #define value for second derivative of psi
    for j in range(1,step):
        psi[j] = psi[j-1] + dpsi*dx #new value of psi
        ddpsi = -2*energy*psi[j-1]  #new value of psi derivative
        dpsi += ddpsi*dx #append psi second derivative values
    if psi[998] < aboutzero and psi[999] > -aboutzero or psi[998] > aboutzero and psi[999] < -aboutzero: #set boundaries for the psi value
        print(energy , "*****") #This shows that the energy level we found satisfies our conditions
        N.append(1) #Append our values of N
        psilist.append(psi) #Append psi
        Energylist.append(energy) #Append energy with the new values
        energy += (0.25)*energy #Append energy values again by a fourth of the energy
        #Now to plot our energy values
        plt.figure(1)
        plt.plot(psi)
        plt.xlabel("Position""L/Step")
        plt.ylabel("Psi")
        plt.title("Wavefunction")
        plt.figure(2)
        plt.plot(psi**2)
        plt.xlabel("Position""L/Step")
        plt.ylabel("Psi**2")
        plt.title("Probability")
    else:
        energy += dE #appendng energy if our conditions are not met
def Energy(n): #Defining the energy function
    return(((h_bar*n*np.pi)**2)/(2*Me*(L)**2)) #Real energy value that we expect
Nrange = len(N) #Setting the range of N values
for k in range(1,Nrange+1):
    Energy(k) #Energy in the range of k values
    E.append(Energy(k)) #Append energy
print("Analytical",E,",") #Here is the actual value of energy that we are supposed to find
print("Approximation",Energylist) #This is the approximate energy that we are calculating with our code
#Another plot
plt.figure(3)
plt.plot(E)
plt.plot(Energylist)
plt.xlabel("N-level")
plt.ylabel("Energy(n) (eV)")
plt.title("Energy Levels")

#I think the code makes sense, but I don't understand why I get zero for the wavefunction and probability graphs.
#The energy values calculated make sense and approximately match the analytic values, so something is good with the code
#I don't know if the graph for the energy levels is right.  I think we should be getting trigonometric plots for energy.  That is not what we see.
#I'm not entirely sure how to approach the rest of the problems.  This was the only one I was able to get a semi-functioning result for.