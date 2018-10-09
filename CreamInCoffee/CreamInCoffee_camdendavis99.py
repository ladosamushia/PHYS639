# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:14:59 2018

@author: Camden
"""

import numpy as np
import matplotlib.pyplot as plt

# NOTE: Problems 1-3 take some time to run, and Problems 4 and 5 take absurdly
#       long to run, so I wouldn't even try them.

#------------------------------------------------------------------------------

# Problem 1: Cream in Coffee

# Initializes particle number, grid size, and number of steps
particles = 100
gridSize  = 100
stepLimit = 50000

# Array of positions ([[x position of particle i], [y position of particle i]])
positions = [np.zeros(particles), np.zeros(particles)]

# Runs through the given number of steps
for i in range(stepLimit):
    # Runs through each particle
    for j in range(particles):
        # Randomly selects direction for the particle to move
        direction = np.random.randint(1, 5)
        
        # Updates particle location
        if direction == 1 and positions[0][j] > -gridSize:
            positions[0][j] -= 1
        elif direction == 2 and positions[0][j] < gridSize:
            positions[0][j] += 1
        elif direction == 3 and positions[1][j] > -gridSize:
            positions[1][j] -= 1
        elif direction == 4 and positions[1][j] < gridSize:
            positions[1][j] += 1
            
# Graph of distance from origin
plt.plot(positions[0], positions[1], 'ro')
plt.xlabel("x Position")
plt.ylabel("y Position")
plt.title("Location of cream particles in coffee")

#------------------------------------------------------------------------------

# Problem 2: Hole in the Box

## Initializes particle number and grid conditions
#holeSize = 40
#holeTop = holeSize / 2
#holeBot = -holeSize / 2
#gridSize  = 100
#stepLimit = 35000
#particles  = 100
#particleCount = [particles]
#        
## Array of positions ([[x position of particle i], [y position of particle i]])
#positions = [np.zeros(particles), np.zeros(particles)]
#banishedParticles = []
#
## Runs through given number of steps
#for i in range(stepLimit):
#    # Runs through each particle
#    for j in range(particles):
#        # Skips current particle if it has left the box already
#        if j in banishedParticles:
#            continue
#        
#        # Randomly selects direction for particle to move
#        direction = np.random.randint(1, 5)
#        
#        # Checks if particle leaves the box, and "banishes" it from the box
#        if direction == 1 and positions[0][j] == -gridSize and positions[1][j] <= holeTop and positions[1][j] >= holeBot:
#            particles -= 1
#            banishedParticles.append(j)
#            positions[0][j] = None
#        # Updates particle locations
#        else:
#            if direction == 1 and positions[0][j] > -gridSize:
#                positions[0][j] -= 1
#            elif direction == 2 and positions[0][j] < gridSize:
#                positions[0][j] += 1
#            elif direction == 3 and positions[1][j] > -gridSize:
#                positions[1][j] -= 1
#            elif direction == 4 and positions[1][j] < gridSize:
#                positions[1][j] += 1
#    
#    # Updates particle count array
#    if i >= gridSize:
#        particleCount.append(particles)
#
## Graph of average particle count
#plt.figure(1)
#plt.plot(particleCount, 'ro')
#plt.xlabel("Steps")
#plt.ylabel("Particles remaining")
#plt.title("Particles remaining after N steps")
#
## Graph of distance from origin
#plt.figure(2)
#plt.plot(positions[0], positions[1], 'ro')
#plt.xlabel("x Position")
#plt.ylabel("y Position")
#plt.title("Location of cream particles in coffee")

#------------------------------------------------------------------------------

# Problem 3: Hole in the Box Part 2

## Initializes particle number and grid conditions
#trials = 5
#holeSize = 40
#holeTop = holeSize / 2
#holeBot = -holeSize / 2
#gridSize  = 100
#stepLimit = 35000
#
## Creates an array to store average particle counts
#averageParticleCount = np.zeros(stepLimit)
#
## Graph of particle count
#plt.figure(1)
#plt.xlabel("Steps")
#plt.ylabel("Particles remaining")
#plt.title("Particles remaining after N steps")
#
## Runs through given number of trials
#for h in range(trials):
#    particles  = 100
#    particleCount = [particles]
#        
#    # Array of positions ([[x position of particle i], [y position of particle i]])
#    positions = [np.zeros(particles), np.zeros(particles)]
#    banishedParticles = []
#    
#    # Runs through the given number of steps
#    for i in range(stepLimit):
#        # Runs through each particle
#        for j in range(particles):
#            # Skips current particle if it has left the box already
#            if j in banishedParticles:
#                continue
#            
#            # Randomly selects direction for particle to move
#            direction = np.random.randint(1, 5)
#            
#            # Checks if particle leaves the box, and "banishes" it from the box
#            if direction == 1 and positions[0][j] == -gridSize and positions[1][j] <= holeTop and positions[1][j] >= holeBot:
#                particles -= 1
#                banishedParticles.append(j)
#                positions[0][j] = None
#            # Updates particle location
#            else:
#                if direction == 1 and positions[0][j] > -gridSize:
#                    positions[0][j] -= 1
#                elif direction == 2 and positions[0][j] < gridSize:
#                    positions[0][j] += 1
#                elif direction == 3 and positions[1][j] > -gridSize:
#                    positions[1][j] -= 1
#                elif direction == 4 and positions[1][j] < gridSize:
#                    positions[1][j] += 1
#        
#        # Updates current particle count and average particle count
#        if i >= gridSize:
#            particleCount.append(particles)
#            averageParticleCount[i] += particles / trials
#        else:
#            averageParticleCount[i] = particles
#    plt.plot(particleCount, 'ro')
#
## Graph of average particle count
#plt.figure(2)
#plt.plot(averageParticleCount, 'ro')
#plt.xlabel("Steps")
#plt.ylabel("Particles remaining")
#plt.title("Average particles remaining after N steps")
#
## Graph of distance from origin
#plt.figure(3)
#plt.plot(positions[0], positions[1], 'ro')
#plt.xlabel("x Position")
#plt.ylabel("y Position")
#plt.title("Location of cream particles in coffee")

#------------------------------------------------------------------------------

# Problem 4: Entropy
# NOTE: I think my code works, but I haven't been able to optimize it well
#       enough to run in a reasonable amount of time. Same goes for Problem 5.

## Initializes particle number, grid size, and number of steps
#particles = 100
#gridSize  = 100
#stepLimit = 10000
#
## Array of positions ([[x position of particle i], [y position of particle i]])
#positions = [np.zeros(particles), np.zeros(particles)]
#entropyValues = np.zeros(particles)
#
## Returns current entropy in system
#def entropy(positions, particles, gridSize):
#    # Initializes values for entropy grid
#    entropyGridWidth = 10
#    entropyGridSize = int(entropyGridWidth / 2)
#    chunkSize = gridSize / entropyGridSize
#    entropyGridPositions = np.zeros(entropyGridWidth * entropyGridWidth)
#    
#    # Checks each chunk of the grid for particles
#    for i in range(-entropyGridSize, entropyGridSize):
#        for j in range(-entropyGridSize, entropyGridSize):
#            # Sets which location the current amount of particles is loggd in
#            entropyPositionsIndex = j + entropyGridSize + ((i + entropyGridSize) * entropyGridWidth)
#            
#            # Sets boundaries of current chunk
#            xMin = i
#            xMax = xMin + chunkSize
#            yMax = -j
#            yMin = yMax - chunkSize
#            
#            # Counts the number of particles in the chunk
#            for k in range(particles):
#                if (positions[0][k] > xMin and positions[0][k] < xMax) and (positions[1][k] > yMin and positions[1][k] < yMax):
#                    entropyGridPositions[entropyPositionsIndex] += 1
#    
#    totalEntropy = 0
#    # Calculates current entropy            
#    for particleNum in entropyGridPositions:
#        P = particleNum / particles
#        if P != 0:
#            totalEntropy -= P * np.log(P)
#        
#    return totalEntropy
#
## Runs through the given number of steps
#for i in range(stepLimit):
#    # Runs through each particle
#    for j in range(particles):
#        # Randomly selectes direction for particle to move
#        direction = np.random.randint(1, 5)
#        
#        # Updates particle location
#        if direction == 1 and positions[0][j] > -gridSize:
#            positions[0][j] -= 1
#        elif direction == 2 and positions[0][j] < gridSize:
#            positions[0][j] += 1
#        elif direction == 3 and positions[1][j] > -gridSize:
#            positions[1][j] -= 1
#        elif direction == 4 and positions[1][j] < gridSize:
#            positions[1][j] += 1
#            
#        # Records current entropy in system
#        entropyValues[j] = entropy(positions, particles, gridSize)
#        
#            
## Graph of entropy after each step
#plt.plot(entropyValues,  'ro')
#plt.xlabel("Steps")
#plt.ylabel("Entropy")
#plt.title("Entropy after N steps")
#
## Graph of distance from origin
#plt.figure(2)
#plt.plot(positions[0], positions[1], 'ro')
#plt.xlabel("x Position")
#plt.ylabel("y Position")
#plt.title("Location of cream particles in coffee")

#------------------------------------------------------------------------------

# Problem 5: Entropy Part 2

## Initializes particle number, grid size, number of steps, and trials
#particles = 100
#gridSize  = 100
#stepLimit = 10000
#trials = 3
#
#averageEntropy = np.zeros(particles)
#
## Returns current entropy in system
#def entropy(positions, particles, gridSize):
#    # Initializes values for entropy grid
#    entropyGridWidth = 10
#    entropyGridSize = int(entropyGridWidth / 2)
#    chunkSize = gridSize / entropyGridSize
#    entropyGridPositions = np.zeros(entropyGridWidth * entropyGridWidth)
#    
#    # Checks each chunk of the grid for particles
#    for i in range(-entropyGridSize, entropyGridSize):
#        for j in range(-entropyGridSize, entropyGridSize):
#            # Sets which location the current amount of particles is loggd in
#            entropyPositionsIndex = j + entropyGridSize + ((i + entropyGridSize) * entropyGridWidth)
#            
#            # Sets boundaries of current chunk
#            xMin = i
#            xMax = xMin + chunkSize
#            yMax = -j
#            yMin = yMax - chunkSize
#            
#            # Counts the number of particles in the chunk
#            for k in range(particles):
#                if (positions[0][k] > xMin and positions[0][k] < xMax) and (positions[1][k] > yMin and positions[1][k] < yMax):
#                    entropyGridPositions[entropyPositionsIndex] += 1
#    
#    totalEntropy = 0
#    # Calculates current entropy            
#    for particleNum in entropyGridPositions:
#        P = particleNum / particles
#        if P != 0:
#            totalEntropy -= P * np.log(P)
#        
#    return totalEntropy
#
## Runs through given number of trials
#for h in range(trials):
#    # Array of positions ([[x position of particle i], [y position of particle i]])
#    positions = [np.zeros(particles), np.zeros(particles)]
#    
#    # Runs through the given number of steps
#    for i in range(stepLimit):
#        # Runs through each particle
#        for j in range(particles):
#            # Randomly selectes direction for particle to move
#            direction = np.random.randint(1, 5)
#            
#            # Updates particle location
#            if direction == 1 and positions[0][j] > -gridSize:
#                positions[0][j] -= 1
#            elif direction == 2 and positions[0][j] < gridSize:
#                positions[0][j] += 1
#            elif direction == 3 and positions[1][j] > -gridSize:
#                positions[1][j] -= 1
#            elif direction == 4 and positions[1][j] < gridSize:
#                positions[1][j] += 1
#                
#            # Records current entropy in system
#            averageEntropy[j] += entropy(positions, particles, gridSize) / trials
#        
#            
## Graph of entropy after each step
#plt.plot(averageEntropy, 'ro')
#plt.xlabel("Steps")
#plt.ylabel("Entropy")
#plt.title("Entropy after N steps")
#
## Graph of distance from origin
#plt.figure(2)
#plt.plot(positions[0], positions[1], 'ro')
#plt.xlabel("x Position")
#plt.ylabel("y Position")
#plt.title("Location of cream particles in coffee")














        
