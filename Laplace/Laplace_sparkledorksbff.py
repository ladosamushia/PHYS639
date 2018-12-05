# -*- coding: utf-8 -*-
"""
Created on Thu Nov 01 13:45:45 2018

@author: jessi
"""

#Jessica Pietrowski
#Square in a box

import numpy as np
import matplotlib.pyplot as plt

Ngrid = 100 #Grid size
phi = np.zeros((Ngrid,Ngrid)) #Define our box size
new_phi = np.zeros((Ngrid,Ngrid)) #Define the potential size
delta = 0.001 #size of our tiny increment

#Square Box
for i in range(Ngrid):
    for j in range(Ngrid):
        if i >= 40 and i <= 60 and j >= 40 and j <= 60: #define dimensions of box within box
            phi[i][j] = 100 #potential of said box
        elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1: #if the sides of the box are zero or barely smaller than the grid size
            phi[i][j] = 0
        else:
            phi[i][j] = 0
#Basically, our potential is zero unless the box is in the specified range
#Now to plot the box
plt.figure(1)
plt.imshow(phi)
#We see a plain square.  This is to be expected

#Now to look at the potential
N = 100
for k in range(N):
    print(k) #We'll evolve the system over 100 steps and see what the potential looks like
    for i in range(Ngrid):
        for j in range(Ngrid):
            if i >= 40 and i <= 60 and j >= 40 and j <= 60: #Same bounds
                new_phi[i][j] = 100
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                new_phi[i][j] = 0
            else:
                new_phi[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4 #This is the solution for our Laplace equation
    plt.figure(2)
    plt.pause(0.001) #We want to wait a bit between plots
    phi = np.copy(new_phi)
    plt.clf()
    plt.imshow(phi)
    
    #We see the potential radiating out from the box.  This is what we expect.
#Parallel Plate Capacitor
laplacian = delta*phi

for i in range(Ngrid):
    for j in range(Ngrid):
        if i >= 40 and i <= 60 and j >= 60 and j <= 62: #Plate 1 bounds
            phi[i][j] = 100 #Plate one potential
        elif i >= 40 and i <= 60 and j >= 60 and j <= 62: #Plate two bounds
            phi[i][j] = -100 #Plate two potential
        elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
            phi[i][j] = 0
        else:
            phi[i][j] = 0

plt.figure(3)
plt.imshow(phi)

#We see the parallel plates without potential.  They look nice.

for k in range(N):
    for i in range(Ngrid):
        for j in range(Ngrid):
            if i >= 40 and i <= 60 and j >= 40 and j <= 42:
                new_phi[i][j] = 100
            elif i >= 40 and i <= 60 and j >= 60 and j <= 62:
                new_phi[i][j] = -100
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                new_phi[i][j] = 0
            else:
                new_phi[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4 #Our solution to the Laplace equation remains the same
    plt.figure(4)
    plt.pause(0.001)
    phi = np.copy(new_phi)
    plt.clf()
    plt.imshow(phi)
    
    #The potential moves out and around each plate, but the potentials from each plate do not touch.  This makes sense.
    
#Perpendicular Plate Capacitor
#We don't want our plates to touch each other
for i in range(Ngrid):
    for j in range(Ngrid):
        if i >= 40 and i <= 60 and j >= 60 and j <= 62:
            phi[i][j] = 100
        elif i >= 20 and i <= 22 and j >= 70 and j <= 90:
            phi[i][j] = -100
        elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
            phi[i][j] = 0
        else:
            phi[i][j] = 0

plt.figure(5)
plt.imshow(phi)

for k in range(N):
    for i in range(Ngrid):
        for j in range(Ngrid):
            if i >= 40 and i <= 60 and j >= 60 and j <= 62:
                new_phi[i][j] = 100
            elif i >= 20 and i <= 22 and j >= 70 and j <= 90:
                new_phi[i][j] = -100
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                new_phi[i][j] = 0
            else:
                new_phi[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4
    plt.figure(6)
    plt.pause(0.001)
    phi = np.copy(new_phi)
    plt.clf()
    plt.imshow(phi)
    
    #Once again, the potential comes out and around the plates and does not touch.  It's the same as the parallel plate, except the plates are perpendicular.
    
#Now let's try to put a charge in a grounded box.  This requires a Poisson equation
#I'm not sure I understand how to do the Poisson equation, but we're going to try it out!

Q = 1 #Define charge in coulombs - we'll choose 1 for simplicity's sake
delta = 0.001 #size of our tiny increment

for i in range(Ngrid):
    for j in range(Ngrid):
        if i == 50 and j == 50:
            phi[i][j] = Q
        elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
            phi[i][j] = 0
        else:
            phi[i][j] = 0

plt.figure(7)
plt.imshow(phi)

for k in range(N):
    for i in range(Ngrid):
        for j in range(Ngrid):
            p = Q/(delta**2)
            if i == 50 and j == 50: #place the charge in the middle
                new_phi[i][j] = Q
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                new_phi[i][j] = 0
            else:
                new_phi[i][j] = (-p*(delta**2)/4) + (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4 #This is the solution to our Poisson equation
    plt.figure(8)
    plt.pause(0.001)
    phi = np.copy(new_phi)
    plt.clf()
    plt.imshow(phi)
    
    #I'm not sure if the plot is right, but it looks cool!
    
for i in range(Ngrid):
    for j in range(Ngrid):
        if i == 50 and j == 90: #The particle is now closer to one wall than the other
            phi[i][j] = Q
        elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
            phi[i][j] = 0
        else:
            phi[i][j] = 0

plt.figure(9)
plt.imshow(phi)

#Now the particle is closer to one wall
#We want to see how the presence of a grounded wall affects the potential distribution
for k in range(N):
    for i in range(Ngrid):
        for j in range(Ngrid):
            p = Q/(delta**2)
            if i == 50 and j == 90:
                new_phi[i][j] = Q
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                new_phi[i][j] = 0
            else:
                new_phi[i][j] = (-p*(delta**2)/4) + (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4 #This is the solution to our Poisson equation
    plt.figure(10)
    plt.pause(0.001)
    phi = np.copy(new_phi)
    plt.clf()
    plt.imshow(phi)
    
    #I'm not sure how to describe the effect of the grounded wall on the potential distribution of the charge.
    #Th wall is clearly having an effect on the charge.  It looks like some of the charge potential is moving towards the grounded wall.

#Now we have two charges, separated by a small distance
for i in range(Ngrid):
    for j in range(Ngrid):
        if i == 50 and j == 50: #First charge
            phi[i][j] = Q
        elif i == 52 and j == 52: #Second charge
            phi[i][j] = Q
        elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
            phi[i][j] = 0
        else:
            phi[i][j] = 0

plt.figure(11)
plt.imshow(phi)

for k in range(N):
    for i in range(Ngrid):
        for j in range(Ngrid):
            p = Q/(delta**2)
            if i == 50 and j == 50:
                new_phi[i][j] = Q
            elif i == 52 and j == 52:
                new_phi[i][j] = Q
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                new_phi[i][j] = 0
            else:
                new_phi[i][j] = (-p*(delta**2)/4) + (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4 #This is the solution to our Poisson equation
    plt.figure(12)
    plt.pause(0.001)
    phi = np.copy(new_phi)
    plt.clf()
    plt.imshow(phi)
    
    #The potentials of the two charges are forming one larger potential rather than two separate ones.
    #This is reminiscint of a dipole.  This makes sense.