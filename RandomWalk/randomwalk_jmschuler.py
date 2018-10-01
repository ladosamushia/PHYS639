# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:25:15 2018

@author: Jared
"""

import numpy as np
from numpy import random as rand
import matplotlib.pyplot as plt
import mpl_toolkits
from mpl_toolkits import mplot3d               # for problem 3 and 4


# Problem 1. This problem in particular is quite taxing for processor power and how fast it actually is, I would assume there are faster ways to complete this program.
p = 100                                    # how many particles there are
stepmax = 1000                            # maximum steps the for loop goes for
stepsize = np.zeros(stepmax)
sum = np.zeros(p)

for i in range(p):
    for j in range(stepmax):
        stepsize[j] = rand.choice([-1,1])
        sum[i] += stepsize[j]
    sum[i] = abs(sum[i])                    # Takes the absolute value of i

plt.figure()
plt.plot(sum, '.')
plt.title('Problem 1 Scatter Plot')

plt.figure()
plt.hist(sum,100)
plt.title('Problem 1 Histogram')
# --------------------------------------------------------------------------

# Problem 2. Same as Problem 1, but add three (+1) options instead of just one. 
p2 = 100                                 # how many particles there are
stepmax2 = 1000                           # maximum steps the for loop goes for
stepsize2 =np.zeros(stepmax2)
sum2 = np.zeros(p2)

for k in range(p2):
    for l in range(stepmax):
        stepsize[l] = rand.choice([-1,1,1,1])
        sum[k] += stepsize[l]
    sum2[k] = abs(sum[k])                # Takes the absolute value of i. Couldn't figure out how to set it as a different name to make it less confusing.

plt.figure()
plt.plot(sum2, '.')
plt.title('Problem 2 Scatter Plot')

plt.figure()
plt.hist(sum2, 100)
plt.title('Problem 2 Histogram')

#-----------------------------------------------------------------------------

# Problem 3. Now,the particle can move left, right, up, down, forwards, backwords, etc. Code adapted from Camden Davis's code

stepmax3 = 1000
stepsize3 = np.zeros(stepmax3)

for h in range(1, stepmax3):
    stepsize3 = h
    x = np.zeros(stepsize3)
    y = np.zeros(stepsize3)
    z = np.zeros(stepsize3)
    # They all need to apply to the same stepsize because it's one trial run with 6 possible directions
    xsteps = np.zeros(stepsize3)
    ysteps = np.zeros(stepsize3)
    zsteps = np.zeros(stepsize3)
    
    for u in range(1, stepsize3):
        step = rand.randint(1,7)
        if step == 1:
            xsteps[u]= -1           # left
        if step == 2:
            xsteps[u] = 1           # right
        if step == 3:
            ysteps[u] = -1          # down
        if step == 4:
            ysteps[u] = 1           # up
        if step == 5:
            zsteps[u] = -1          # backward
        if step == 6:
            zsteps[u] = 1           # forward
            
        if u == 0:
            x[u] = xsteps[u]
            y[u] = ysteps[u]
            z[u] = zsteps[u]
        else:
            x[u] = x[u-1] + xsteps[u]
            y[u] = y[u-1] + ysteps[u]
            z[u] = z[u-1] + zsteps[u]
            
plt.figure()
plt.plot(x, 'r', label = 'x-direction')
plt.plot(y, 'g', label = 'y-direction')
plt.plot(z, 'b', label = 'z-direction')
plt.title('Problem 3: Directions travelled')
plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0)


plt.figure()
ax = plt.title('Problem 3')
ax = plt.axes(projection='3d')
ax.scatter3D(x,y,z, c=z, cmap='Greens');
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
axLim = stepmax3/20
ax.set_xlim(-axLim, axLim)
ax.set_ylim(-axLim, axLim)
ax.set_zlim(-axLim, axLim)
            