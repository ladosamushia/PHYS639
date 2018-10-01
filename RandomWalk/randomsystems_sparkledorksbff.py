# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:09:12 2018

@author: jessi
"""
#We want to plot the random walk of a particle originally at the origin
#Plot absolute value of position versus number of steps
#The particle can move left and right with equal likelihood
import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Nsteps = 100 #Number of steps the particle will take
trials = 1000 #Number of trials to run the particle through
def average_distance(steps, trials):
    A = [] #Blank space to append distances
    for i in range(trials):
        position = 0.0 #initial position
        for j in range(Nsteps):
            step = random.choice([-1,1]) #random choice of where the particle moves to
            position += step #appending the position to account for the random choice
        A.append(np.abs(position)) #appending A for the absolute value of the position
    return np.mean(A) #return the average distance
distance = [] #Blank space for storing distances
for steps in range(Nsteps):
    distance.append(average_distance(steps, trials)) #append distances
    
plt.figure()
plt.plot(range(Nsteps),distance,'go')
plt.title('1D Walk')
plt.ylabel('distance')
plt.xlabel('Steps')
#The plot for the 1D random walk shows random points scattered everywhere.  Since all spots are equally likely to be reached, this makes sense.

#Now the chance of the particle moving to the left is three times as likely as the particle moving to the right
Nsteps = 100 #Step size
trials = 1000 #Number of trials
def average_distance(steps, trials):
    A = [] #Blank space for distances
    for i in range(trials):
        position = 0.0
        for j in range(Nsteps):
            step = random.choice([-1,1,1,1]) #the particle is three times as likely to move to the left
            position += step
        A.append(np.abs(position))
    return np.mean(A)
distance = []
for steps in range(Nsteps):
    distance.append(average_distance(steps, trials))
    
plt.figure()
plt.plot(range(Nsteps),distance,'red')
plt.title('1D Biased Walk')
plt.ylabel('distance')
plt.xlabel('Steps')
#We expect the particle to move towards the left more frequently than the right.  The graph supports this

#Now the particle is free to move in three dimensions
Nsteps = 100
Trials = 1000
def average_distance(steps, Trials):
    A = []
    for i in range(Nsteps):
        x = 0 #initial x
        y = 0 #initial y
        z = 0 #initial z
        for j in range(Trials):
            step = random.choice(range(6))
            if step == 0:
                x += 1 #x to the left
            elif step == 1:
                x += -1 #x to the right
            elif step == 2:
                y += 1 #y to the left
            elif step == 3:
                y += -1 #y to the right
            elif step == 4:
                z += 1 #z to the left
            else:
                z += -1 #z to the right
        A.append(np.sqrt(x**2 + y**2 + z**2)) #account for the changes in x, y, and z position
    return np.mean(A) #average distances
distance = []
for steps in range(Nsteps):
    distance.append(average_distance(steps, trials)) #append the distance
    
plt.figure()
plt.plot(range(Nsteps),distance,'y-')
plt.title('3d Random Walk')
plt.ylabel('distance')
plt.xlabel('Steps')
#All movements are equally likely.  The graph supports this.

#Now the particle can move in a random direction
Nsteps = 100
Trials = 1000
def average_distance(steps, Trials):
    A = []
    for i in range(Nsteps):
        x = 0
        y = 0
        z = 0
        for j in range(Trials):
            step = random.choice(range(6))
            if step == 0:
                x += 1
            elif step == 1:
                x += -1
            elif step == 2:
                y += 1
            elif step == 3:
                y += -1
            elif step == 4:
                z += 1
            else:
                z += -1
        A.append(np.sqrt(x**2 + y**2 + z**2))
    return np.mean(A)
distance = []
for steps in range(Nsteps):
    distance.append(average_distance(steps, trials))
    
plt.figure()
plt.plot(range(Nsteps),distance,'m')
plt.title('3d Random Walk')
plt.ylabel('distance')
plt.xlabel('Steps')
fig = plt.figure(1)
ax = fig.add_subplot(111,projection='3d')
ax.plot(x,y,z)

#We expect to see equal motion here.  I don't really know what's going on with my graph.

Nsteps = 100 #Need to vary step size for low numbers (5,10,15,etc.)
Trials = 1000
def average_distance(steps, Trials):
    A = []
    for i in range(Nsteps):
        x = 0
        y = 0
        z = 0
        for j in range(Trials):
            theta = np.random.rand(1000)*np.pi #define theta
            phi = np.random.rand(1000)*2*np.pi #define phi
            r = 1 #radius
            x = r*np.sin(theta)*np.cos(phi) #x dependency on r, theta, and phi
            y = r*np.sin(theta)*np.sin(phi) #y dependency on r, theta, and phi
            z = r*np.cos(theta) #z dependency on r and theta
            anglestep = (180/Trials)*np.pi/180 #step for appending theta
            angle2step = (360/Trials)*np.pi/180 #step for appending phi
            step = random.choice(range(4)) #define a range for where the particle can step initially
            if step == 1:
                theta = theta + anglestep #theta moves to the left
            elif step == 2:
                theta = theta - anglestep #theta moves to the right
            elif step == 3:
                phi = phi + angle2step #theta moves to the left
            else:
                phi = phi - angle2step #theta moves to the right
                x = r*np.sin(theta)*np.cos(phi) #x dependency on r, theta, and phi
                y = r*np.sin(theta)*np.sin(phi) #y dependency on r, theta, and phi
                z = r*np.cos(theta) #z dependency on r and theta
        A.append(np.sqrt(x**2 + y**2 + z**2))
    return np.mean(A)
distance = []
for steps in range(Nsteps):
    distance.append(average_distance(steps, trials))
    
plt.figure()
plt.plot(range(Nsteps),distance,'m')
plt.title('3d Random Walk with No Grid')
plt.ylabel('distance')
plt.xlabel('Steps')
fig = plt.figure(2)
ax = fig.add_subplot(222,projection='3d')
ax.plot(x,y,z)
#Overall, the code takes quite a while to run.  For the last problem, we should see random walking all over the graph, but I haven't been able to see the graph.
#There are clearly problems with my code for problems 3 and 4, but I don't really know what those problems are.