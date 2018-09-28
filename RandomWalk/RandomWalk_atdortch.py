# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:10:05 2018

@author: Aus
"""

import numpy as np
import random as rand
import matplotlib.pyplot as plt



particles = 10
steps = 20




position = np.zeros(particles)      # position of particles start at zero

right = 1; left = 2                 # assign values to left and right positions

for step in range(steps):           
    for p in range(particles):
        walk = rand.randint(1,2)
        if walk == right:
            position[p] += 1
        elif walk == left:
            position[p] -=1
displacement = position-0

print(position)

plt.plot(steps,displacement)

