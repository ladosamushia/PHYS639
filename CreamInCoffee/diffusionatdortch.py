# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:34:55 2018

@author: Aus
"""

import numpy as np
import random as rand
import matplotlib.pyplot as plt
from time import time

Nparticles = 400
Ngrid = 100
Nsteps = 10000
itime = time()
k = 0
K=[]
B=[]
b = 0
x = np.zeros(Nparticles)
y = np.zeros(Nparticles)

# define a loop where I choose a particle in Nparticles
for i in range(Nsteps):
    
    p_index = rand.randint(Nparticles)
    
    # Choose a random direction
    
    # 0 - left, 1 - right, 2 - up, 3 - down
    for j in range(0,1):
        gridsize = 100
        R = 1
        X = np.zeros(Nparticles)
        Y = np.zeros(Nparticles)
    for i in range(int(Nsteps[j])):
        particleindex = rand.randint(Nparticles)
        r = R
        theta = np.deg2rad(rand.choice(range(0, 360)))
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        #this will take particles out of the box and no longer use them
        #it will also count the number of particles in the box for each step in a list
        #keeps particles out of the box from going back in
        if X[particleindex] + x >= gridsize and Y[particleindex] + y >= -10 and Y[particleindex] + y <= 10:
            X[particleindex] = None
            Y[particleindex] = None
            if True:
                Nparticles -= 1
            elif False:
                Nparticles += 0
        B.append(Nparticles)
        #recoils the particle if needed so it doesn't leave the box for spaces not satisified above for the window
        if X[particleindex] + x >= gridsize:
            x = -x
        elif Y[particleindex] + y >= gridsize: 
            y = -y
        elif X[particleindex] + x <= -gridsize:
            x = -x
        elif Y[particleindex] +y <= -gridsize:
            y = -y
        k += 1
        K.append(k)
        #if all the above is false the particle will move as randomly decided
        X[particleindex] += x
        Y[particleindex] += y
plt.figure( 2 )
plt.plot(B)
plt.xlabel (" Itrration Step ")
plt.ylabel (" Particles in Box ")
plt.title ("Particles in the Box")
plt.figure( 1 )
plt.plot(X, Y, '.')
plt.xlabel (" X position ")
plt.ylabel (" Y position ")
plt.title (" Browning Motion ")
plt.xlim(-125,125)
plt.ylim(-125,125)
time1 = time()
print('Time to Completion:',time1-itime)

    
    
