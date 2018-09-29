# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:10:05 2018

@author: Aus
"""

import numpy as np
import random as rand
import matplotlib.pyplot as plt



particles = 100
steps = np.arange(1000)
Nsteps = 1000



position = np.zeros(Nsteps)      # position of particles start at zero

right = 1; left = 2                 # assign values to left and right positions

for step in steps:           
    for p in range(particles):
        walk = rand.randint(1,2)
        if walk == right:
            position[step] += 1
        elif walk == left:
            position[step] -=1
displacement = position-0

print(position)

plt.plot(steps,displacement,'og')



#----------------------------------------------------------------------

import numpy as np
import random as rand
import matplotlib.pyplot as plt



particles = 100
steps = np.arange(1000)
Nsteps = 1000



position = np.zeros(Nsteps)      # position of particles start at zero

right = 1; left = 2                 # assign values to left and right positions

for step in steps:           
    for p in range(particles):
        walk = rand.randint(1,2)
        if walk == right:
            position[step] += 1
        elif walk == left:
            position[step] -=3
displacement = position-0

print(position)

plt.plot(steps,displacement,'og')


#-------------------------------------------------------------------------

import numpy as np
import random as rand
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


ax = plt.axes(projection='3d')
fig = plt.figure()
ax.scatter3D(steps,displacement)
x = steps
y = displacement

particles = 100
steps = np.arange(1000)
Nsteps = 1000



position = np.zeros(Nsteps)      # position of particles start at zero

right = 1; left = 2; forward = 3; backward = 4; up = 5; down = 6

for step in steps:           
    for p in range(particles):
        walk = rand.randint(1,7)
        if walk == right:
            position[step] += 1
        elif walk == left:
            position[step] -=1
        elif walk == forward:
            position[step] +=1
        elif walk == backward:
            position[step] -=1
        elif walk == up:
            position[step] +=1
        elif walk == down:
            position[step] -=1
displacement = position-0

z = np.linspace(up,down)
print(position)



ax.scatter3D(x,y,z,'g')



