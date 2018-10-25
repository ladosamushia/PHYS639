
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

aboutzero = 0.0000001

energy = 4.8

step = 1000



psi = np.zeros(step)

dpsi = np.zeros(step)

ddpsi = np.zeros(step)



dx = L/step
dE = 0.1
while energy < 5:
    dpsi = 1 

    ddpsi = 0.0
    for j in range(1,step):

        psi[j] = psi[j-1] + dpsi*dx

        ddpsi = -2*energy*psi[j-1] 

        dpsi += ddpsi*dx
        
    plt.plot(psi)
       # print (ddpsi , dpsi)

    if psi[998] < aboutzero and psi[999] > -aboutzero or psi[998] > aboutzero and psi[999] < -aboutzero:
        print(energy , "*****")
        psilist.append(psi)

        Energylist.append(energy)

        energy += energy

    else:

        energy += dE
