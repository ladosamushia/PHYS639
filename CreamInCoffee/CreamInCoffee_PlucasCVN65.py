# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 by Philip Lucas

For Part 1 only comment out lines 34-41 and 56-60
For Part 2 run without the above comments 

"""
from time import time
import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
numberofparticles = 400
number = 1e7
N= 4 #determines increments of plots
numberofsteps = [number]
time0 = time()
k = 0
K=[]
B=[]
b = 0
for j in range(0,1):
    gridsize = 100
    R = 1
    X = np.zeros(numberofparticles)
    Y = np.zeros(numberofparticles)
    for i in range(int(numberofsteps[j])):
        particleindex = random.randint(numberofparticles)
        r = R
        theta = np.deg2rad(random.choice(range(0, 360)))
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        #this will take particles out of the box and no longer use them
        #it will also count the number of particles in the box for each step in a list
        #keeps particles out of the box from going back in
        if X[particleindex] + x >= gridsize and Y[particleindex] + y >= -10 and Y[particleindex] + y <= 10:
            X[particleindex] = None
            Y[particleindex] = None
            if True:
                numberofparticles -= 1
            elif False:
                numberofparticles += 0
        B.append(numberofparticles)
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
print('Time to Completion:',time1-time0)