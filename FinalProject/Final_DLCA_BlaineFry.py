# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:29:01 2018

@author: Blaine Fry
"""
# 3D Grid Diffusion With Aggregation
# Von Neumann neighbors
# Periodic Boundaries
# Currently no drag force

import numpy as np
import numpy.random as rand
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import chain

from datetime import datetime
start_time = datetime.now()

# generate a figure etc. to enable plotting when DLCA() is called
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# define the grid on which the particles will move
grid_size = 50
grid = np.zeros((grid_size,grid_size,grid_size))

# generate some particles
N_particles = 200
# place those particles on the grid (0: empty, 1: occupied)
ii = 0
while ii < N_particles:
    xidx = rand.randint(0,grid_size) # randomly select an x index
    yidx = rand.randint(0,grid_size) # randomly select a y index
    zidx = rand.randint(0,grid_size) # randomly select a z index
    if grid[xidx][yidx][zidx] != 1: # make sure that position isn't already occupied
        grid[xidx][yidx][zidx] = 1
        ii += 1

# define possible neighbor positions in grid for use later (Von Neumann)
def neighbors(x,y,z):
    global grid_size
    l = [x-1,y,z] # left
    r = [x+1,y,z] # right
    a = [x,y+1,z] # above
    b = [x,y-1,z] # below
    f = [x,y,z+1] # forward
    k = [x,y,z-1] # back
    tl = [grid_size-1,y,z] # left toroidally
    tr = [0,y,z] # right toroidally
    ta = [x,0,z] # above toroidally
    tb = [x,grid_size-1,z] # below toroidally
    tf = [x,y,0]
    tk = [x,y,grid_size-1]
    # check for corner conditions (this one first bc it's more restrictive than edge conditions)
    if y == grid_size-1 and x == grid_size-1 and z == grid_size-1: # upper right forward corner
        friends = [l,tr,ta,b,tf,k]
    elif y == grid_size-1 and x == 0 and z == grid_size-1: # upper left forward corner
        friends = [tl,r,ta,b,tf,k]
    elif y == 0 and x == grid_size-1 and z == grid_size-1: # lower right forward corner
        friends = [l,tr,a,tb,tf,k]
    elif y == 0 and x == 0 and z == grid_size-1: # lower left forward corner
        friends = [tl,r,a,tb,tf,k]
    elif y == grid_size-1 and x == grid_size-1 and z == 0: # upper right back corner
        friends = [l,tr,ta,b,f,tk]
    elif y == grid_size-1 and x == 0 and z == 0: # upper left back corner
        friends = [tl,r,ta,b,f,tk]
    elif y == 0 and x == grid_size-1 and z == 0: # lower right back corner
        friends = [l,tr,a,tb,f,tk]
    elif y == 0 and x == 0 and z == 0: # lower left back corner
        friends = [tl,r,a,tb,f,tk]
    # check for edge conditions
    elif y == grid_size-1 and x == grid_size-1: # upper right edge
        friends = [l,tr,ta,b,f,k]
    elif y == grid_size-1 and x == 0: # upper left edge
        friends = [tl,r,ta,b,f,k]
    elif y == 0 and x == grid_size-1: # lower right edge
        friends = [l,tr,a,tb,f,k]
    elif y == 0 and x == 0: # lower left edge
        friends = [tl,r,a,tb,f,k]
    elif z == grid_size-1 and x == grid_size-1: # right forward edge
        friends = [l,tr,a,b,tf,k]
    elif z == grid_size-1 and x == 0: # left forward edge 
        friends = [tl,r,a,b,tf,k]
    elif z == 0 and x == grid_size-1: # right back edge
        friends = [l,tr,a,b,f,tk]
    elif z == 0 and x == 0: # left back edge
        friends = [tl,r,a,b,f,tk]
    elif y == grid_size-1 and z == grid_size-1: # upper forward edge
        friends = [l,r,ta,b,tf,k]
    elif y == grid_size-1 and z == 0: # upper back edge
        friends = [l,r,ta,b,f,tk]
    elif y == 0 and z == grid_size-1: # lower forward edge
        friends = [l,r,a,tb,tf,k]
    elif y == 0 and z == 0: # lower back edge
        friends = [l,r,a,tb,f,tk]
    # check for face conditions
    elif y == grid_size-1: # upper face
        friends = [l,r,ta,b,f,k]
    elif y == 0: # bottom face
        friends = [l,r,a,tb,f,k]
    elif x == grid_size-1: # right face
        friends = [l,tr,a,b,f,k]
    elif x == 0: # left face
        friends = [tl,r,a,b,f,k]
    elif z == grid_size-1: # forward face
        friends = [l,r,a,b,tf,k]
    elif z == 0: # back face
        friends = [l,r,a,b,f,tk]
    # particle in the middle
    else:
        friends = [l,r,a,b,f,k]
    # sheesh, finally
    return friends
    
# make a function that can find which particles are in a cluster with a given index
def find_cluster(X,Y,Z):
    cluster = [[X,Y,Z]]
    for c in cluster:
        for n in neighbors(c[0],c[1],c[2]):
            if grid[n[0]][n[1]][n[2]] == 1:
                if n in cluster:
                    pass
                else:
                    cluster.append(n)
    return cluster

# make a function that determines all the aggregates for a given macrostate
def find_aggregates():
    aggregates = []
    for i in range(grid_size):
        for j in range(grid_size):
            for k in range(grid_size):
                aggregates_flat = list(chain.from_iterable(aggregates))
                if grid[i][j][k] == 1 and [i,j,k] not in aggregates_flat:
                    aggregates.append(find_cluster(i,j,k))
    return aggregates

# check for particles that start aggregated
aggregates = find_aggregates()

# make a function that propogates the system one step in time
def DLCA_3D(u):
    global grid
    global aggregates
    directions = ['up','down','left','right','forward','back'] # possible directions of motion; defined here for random selection later
    temp_grid = np.copy(grid) # create a temporary grid so that the grid all at once, also solves issue of a particle moving multiple times in one iteration
    # loop through aggregates
    for cluster in aggregates:
        direction = rand.choice(directions) # randomly select a direction in which to move
        for monomer in cluster:
            i = monomer[0]
            j = monomer[1]
            k = monomer[2]
            # move the particle in the temporary grid
            # determine new location
            if direction == 'up':
                if j == grid_size-1: # check for edge condition
                    new_y = 0 # wrap around in toroidal space if it's on the edge
                    new_x = i
                    new_z = k
                else:
                    new_y = j+1 # otherwise move normally
                    new_x = i
                    new_z = k
            if direction == 'down':
                if j == 0: # check for edge condition
                    new_y = grid_size-1 # wrap around in toroidal space if it's on the edge
                    new_x = i
                    new_z = k
                else:
                    new_y = j-1 # otherwise move normally
                    new_x = i
                    new_z = k
            if direction == 'left':
                if i == 0: # check for edge condition
                    new_y = j
                    new_x = grid_size-1 # wrap around in toroidal space if it's on the edge
                    new_z = k
                else:
                    new_y = j # otherwise move normally
                    new_x = i-1
                    new_z = k
            if direction == 'right':
                if i == grid_size-1: # check for edge condition
                    new_y = j # wrap around in toroidal space if it's on the edge
                    new_x = 0
                    new_z = k
                else:
                    new_y = j # otherwise move normally
                    new_x = i+1
                    new_z = k
            if direction == 'back':
                if k == 0: # check for edge condition
                    new_y = j
                    new_x = i # wrap around in toroidal space if it's on the edge
                    new_z = grid_size-1
                else:
                    new_y = j # otherwise move normally
                    new_x = i
                    new_z = k-1
            if direction == 'forward':
                if k == grid_size-1: # check for edge condition
                    new_y = j # wrap around in toroidal space if it's on the edge
                    new_x = i
                    new_z = 0
                else:
                    new_y = j # otherwise move normally
                    new_x = i
                    new_z = k+1
            # update position
            temp_grid[i][j][k] -= 1 # clear initial location
            temp_grid[new_x][new_y][new_z] += 1 # set new position to be live
    if 2 not in temp_grid: # check if solution is valid
        grid = np.copy(temp_grid)
    aggregates = find_aggregates() ##### calling find_aggregates again checks for cluster-cluster aggregation
    # plot stuff
    x = []
    y = []
    z = []
    ax.clear() # clear figure from previous frame in animation
    ax.set_xlim(-1,grid_size)
    ax.set_ylim(-1,grid_size)
    ax.set_zlim(-1,grid_size)
    for i in range(grid_size):
        for j in range(grid_size):
            for k in range(grid_size):
                if grid[i][j][k] == 1:
                    x.append(i)
                    y.append(j)
                    z.append(k)
    ax.plot(x,y,z,'.')
    return grid

ani = FuncAnimation(fig,DLCA_3D,interval=200)
