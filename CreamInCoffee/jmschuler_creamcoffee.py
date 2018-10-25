# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:06:51 2018

@author: Jared
"""

import numpy as np
import matplotlib.pyplot as plt

particles = 100            # Number of particles in the system
Sizegrid = 100              # Size of the grid
stepsizelim = 50000         # Limit of steps

# Part 1: Cream in Coffee
positionxy = [np.zeros(particles), np.zeros(particles)]     # Gives the position in the x and y directions

for i in range (stepsizelim):
    for j in range(particles):
        going = np.random.randint(1,5)
        
        if going == 1 and positionxy[0][j] > -Sizegrid:
            positionxy[0][j] -= 1
        elif going == 2 and positionxy[0][j] < Sizegrid:
            positionxy[0][j] += 1
        elif going == 3 and positionxy[1][j] > -Sizegrid:
            positionxy[1][j] -= 1
        elif going == 4 and positionxy[1][j] < Sizegrid:
            positionxy[1][j] += 1
        
plt.figure(1)        
plt.plot(positionxy[0], positionxy[1],'bo')
plt.xlabel("X vector")
plt.ylabel("Y vector")
plt.title("Problem 1: Random generation of particles in a cream of coffee")

# Part 2: Hole in ze box
sizehole = 40
Tophole = sizehole / 2
Bothole = -sizehole / 2
particles2 = 100                # To avoid any potential overlap with the graph from part 1
stepsizelim2 = 35000

partcount = [particles2]
position = [np.zeros(particles2), np.zeros(particles2)]
badparticles = []

for a in range(stepsizelim2):
    for b in range(particles2):
        if b in badparticles:
            continue
        going2 = np.random.randint(1,5)
        if going2 == 1 and position[0][b] == -Sizegrid and position[1][b] <= Tophole and position[1][b] >= Bothole:
            particles2 -= 1
            badparticles.append(b)
            position[0][b] = None
        
        else:
            if going2 == 1 and position[0][b] > -Sizegrid:
                position[0][b] -= 1
            elif going2 == 2 and position[0][b] < Sizegrid:
                position[0][b] += 1
            elif going2 == 3 and position[1][b] > -Sizegrid:
                position[1][b] -= 1
            elif going2 == 4 and position[1][b] < Sizegrid:
                position[1][b] += 1 
                
    if a >= Sizegrid:
        partcount.append(particles2)

plt.figure(2)
plt.plot(partcount, 'ro')
plt.xlabel("Steps")
plt.ylabel("Remaining Particles")
plt.title("Part 2: Particles remaining in system after N steps")

plt.figure(3)
plt.plot(position[0], position[1], 'ro')
plt.xlabel("X vector")
plt.ylabel("Y vector")
plt.title("Part 2: Location of particles in coffee")

# Part 3: Hole in ze box part 2

# We will use the same dimensions and constants from the first part of hole in the box.

ntrials = 5 
avgpartcount = np.zeros(stepsizelim2)

plt.figure(4)
plt.xlabel('Steps')
plt.ylabel('Particles remaining')
plt.title('Part 3: Particles remaining after N steps. Average is in green')

for c in range(ntrials):
    particlesx = 100
    particount = [particlesx]
    
    positions = [np.zeros(particlesx), np.zeros(particlesx)]
    badbadparticles = []
    
    for d in range(stepsizelim2):
        for e in range(particlesx):
            if e in badbadparticles:
                continue
        
            going3 = np.random.randint(1,5)
        
            if going3 == 1 and positions[0][e] == -Sizegrid and positions[1][e] <= Tophole and positions[1][e] >= Bothole:
                particlesx -= 1
                badbadparticles.append(e)
                positions[0][e] = None
        
            else:
                if going3 == 1 and positions[0][e] > -Sizegrid:
                    positions[0][e] -= 1
                elif going3== 2 and positions[0][e] < Sizegrid:
                    positions[0][e] += 1
                elif going3 == 3 and positions[1][e] > -Sizegrid:
                    positions[1][e] -= 1
                elif going3 == 4 and positions[1][e] < Sizegrid:
                    positions[1][e] += 1  
        if c >= Sizegrid:
            particount.append(particlesx)
            avgpartcount[d] += particlesx / ntrials
        else:
            avgpartcount[d] = particlesx
    plt.plot(particount, 'ro')

plt.plot(avgpartcount, 'go')

plt.figure(5)
plt.plot(positions[0], positions[1], 'ro')
plt.xlabel('X vector')
plt.ylabel('Y vector')
plt.title('Part 3: Location of cream in coffee')

        