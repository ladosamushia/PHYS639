# -*- coding: utf-8 -*-
"""
Created on Thu Oct 04 17:52:05 2018

@author: Blaine Fry
"""
# Phys 639
# Cream in coffee

"""
Problem: Cream in Coffee (lvl*)
"""

import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime
startTime = datetime.now()

def coffee_creamer(N_particles,grid_size,N_steps):
    x = np.zeros(N_particles) # x position for each particle
    y = np.zeros(N_particles) # y position for each particle
    for i in range(N_steps):
        # choose a particle (why can only one particle move at a time?)
        p_index = np.random.randint(N_particles)
        # choose random direction
        potential_directions = ['up','down','left','right']
        direction = np.random.choice(potential_directions)
        if direction == 'left' and x[p_index] > -0.5*grid_size:
            x[p_index] -= 1
        if direction == 'right' and x[p_index] < 0.5*grid_size:
            x[p_index] += 1
        if direction == 'up' and y[p_index] < 0.5*grid_size:
            y[p_index] += 1
        if direction == 'down' and y[p_index] > -0.5*grid_size:
            y[p_index] -= 1
    # plot results
    plt.figure(1)
    plt.plot(x,y,'.', label=str(N_steps)+' Steps')
    plt.title('Cream in Coffee')
    plt.xlim(-0.5*grid_size,0.5*grid_size)
    plt.ylim(-0.5*grid_size,0.5*grid_size)
    plt.legend()

for i in range(3,8):
    coffee_creamer(400,200,10**i)
# as more steps are taken, the particles can diffuse farther from the center

"""
Problem: Hole in the box (lvl*) part 1
"""

step_values = []
particle_count = []

def hole_in_box(N_particles,grid_size,N_steps):
    x = [0]*N_particles # x position for each particle
    y = [0]*N_particles # y position for each particle
    for i in range(N_steps):
        # choose a particle (why can only one particle move at a time?)
        p_index = np.random.randint(N_particles)
        # choose random direction
        potential_directions = ['up','down','left','right']
        direction = np.random.choice(potential_directions)
        if direction == 'left' and x[p_index] > -0.5*grid_size:
            x[p_index] -= 1
        if direction == 'right' and x[p_index] < 0.5*grid_size:
            x[p_index] += 1
        if direction == 'up' and y[p_index] < 0.5*grid_size:
            y[p_index] += 1
        if direction == 'down' and y[p_index] > -0.5*grid_size:
            y[p_index] -= 1
        # make a hole in the left wall (just annhiliate the partciles there)
        if x[p_index] == -0.5*grid_size and np.abs(y[p_index]) <= 40:
            x.pop(p_index)
            y.pop(p_index)
            N_particles -= 1
    step_values.append(N_steps)
    particle_count.append(N_particles)

for i in range(0,11):
    hole_in_box(400,200,i*10**6)

plt.figure(2)
plt.plot(step_values,particle_count,'-')
plt.xlim(0,)
plt.title('Hole in the Box 1')
plt.xlabel('Number of Iterations')
plt.ylabel('Particle Count')
# the decline in number vs time makes sense... it takes a long time for particles
# to get to the hole, though.

"""
Problem: Hole in the box (lvl**) part 2
"""

step_values = []
particle_count_1 = []
particle_count_2 = []
particle_count_3 = []

def hole_in_box(N_particles,grid_size,N_steps,trial_number):
    x = [0]*N_particles # x position for each particle
    y = [0]*N_particles # y position for each particle
    for i in range(N_steps):
        # choose a particle (why can only one particle move at a time?)
        p_index = np.random.randint(N_particles)
        # choose random direction
        potential_directions = ['up','down','left','right']
        direction = np.random.choice(potential_directions)
        if direction == 'left' and x[p_index] > -0.5*grid_size:
            x[p_index] -= 1
        if direction == 'right' and x[p_index] < 0.5*grid_size:
            x[p_index] += 1
        if direction == 'up' and y[p_index] < 0.5*grid_size:
            y[p_index] += 1
        if direction == 'down' and y[p_index] > -0.5*grid_size:
            y[p_index] -= 1
        # make a hole in the left wall (just annhiliate the partciles there)
        if x[p_index] == -0.5*grid_size and np.abs(y[p_index]) <= 40:
            x.pop(p_index)
            y.pop(p_index)
            N_particles -= 1
    if trial_number == 1:
        step_values.append(N_steps)
        particle_count_1.append(N_particles)
    if trial_number == 2:
        particle_count_2.append(N_particles)
    if trial_number == 3:
        particle_count_3.append(N_particles)
        
for j in range(1,4):
    for i in range(0,11):
        hole_in_box(400,200,i*10**6,j)

average_count = []
for a in range(len(step_values)):
    average_count.append((particle_count_1[a]+particle_count_2[a]+particle_count_3[a])/3)

plt.figure(3)
plt.plot(step_values,particle_count_1,'-',label='trial 1')
plt.plot(step_values,particle_count_2,'-',label='trial 2')
plt.plot(step_values,particle_count_3,'-',label='trial 3')
plt.plot(step_values,average_count,'-',label='average')
plt.xlim(0,)
plt.title('Hole in the Box 2')
plt.xlabel('Number of Iterations')
plt.ylabel('Particle Count')    
# note that any positive slopes are due to the fact that consecutive points
# aren't from the same diffusion run...

"""
Problem: Entropy (lvl**)
"""

import numpy as np
from matplotlib import pyplot as plt


def coffee_entropy(N_particles,grid_size,N_steps):
    x = [0]*(N_particles) # x position for each particle
    y = [0]*(N_particles) # y position for each particle
    for i in range(N_steps):
        # choose a particle (why can only one particle move at a time?)
        p_index = np.random.randint(N_particles)
        # choose random direction
        potential_directions = ['up','down','left','right']
        direction = np.random.choice(potential_directions)
        if direction == 'left' and x[p_index] > -0.5*grid_size:
            x[p_index] -= 1
        if direction == 'right' and x[p_index] < 0.5*grid_size:
            x[p_index] += 1
        if direction == 'up' and y[p_index] < 0.5*grid_size:
            y[p_index] += 1
        if direction == 'down' and y[p_index] > -0.5*grid_size:
            y[p_index] -= 1
    # place particles in 10x10 grid for calculating entropy
    grid_positions = []
    for j in range(N_particles):
        grid_positions.append((x[j]/(grid_size/10),y[j]/(grid_size/10)))
    # calculate entropy
    entropy = []
    for k in range(-5,5):
        for l in range(-5,5):
            p_count = float(grid_positions.count((k,l)))
            e = (-1)*(1./(100**p_count)*np.log(1./(100**p_count))) # I think that's right... maybe?
            entropy.append(e)
    return sum(entropy)
    
iterations = []
e = []
for i in range(1,11):
    e.append(coffee_entropy(400,200,i*100000))
    iterations.append(i*100000)

plt.figure(4)
plt.title('Entropy vs Number of Steps')
plt.ylabel('Entropy (arb)')
plt.xlabel('N_Steps')
plt.plot(iterations,e,'-')
# there's a general upwards trend... which is good!

# let's time this thing...
print 'runtime = ' + str(datetime.now() - startTime )