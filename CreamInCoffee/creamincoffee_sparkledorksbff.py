# -*- coding: utf-8 -*-
"""
Created on Tue Oct 02 13:51:33 2018

@author: jessi
"""

#Jessica Pietrowski

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

Nparticles = 400 #number of particles in our box
L = 200 #Length of the box
l = 40 #size of the hole in the box
Nsteps = 10000 #Number of loops
X = np.zeros(Nparticles) #Create an array of x values
Y = np.zeros(Nparticles) #Create an array of y values
Nlist = [Nparticles] #list of particles including Nparticles
Nnow = Nparticles #Number of particles at the current time
for i in range(Nsteps): #Create your loop
    p_index = random.randint(Nparticles) #Define random position index for the particles
    #Choose a random direction
    # 0 = Left, 1 = Right, 2 = Up, 3 = Down
    direction = random.randint(4) #Set the direction for the particle to move in
    if direction == 0 and X[p_index] >= -L:
        X[p_index] -= 1 #Particle moves to the left 1
    elif direction == 1 and X[p_index] <= L:
        X[p_index] += 1 #Particle moves to the right 1
    elif direction == 2 and Y[p_index] <= L:
        Y[p_index] += 1 #Particle moves up 1
    elif direction == 3 and Y[p_index] >= L:
        Y[p_index] -= 1 #Particle moves down one
#For problem 2, we make a hole in the box.  The hole is on the y axis
    if Y[p_index] == 0 and (L-l)/2 <= X[p_index] <= (L+l)/2:
        Y[p_index] = 1E10 #massive amounts of cream and coffee are spilling out of the hole
        Nnow -= 1 #append the number of particles now
    Nlist.append(Nnow) #Append the list of particles
#Plot!
plt.figure()
plt.plot(X,Y,'.')
plt.title('Cream in Coffee')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0,L)
plt.ylim(0,L)
#Plot for problem #2
plt.figure()
plt.title('Hole #1')
plt.plot(range(int(Nsteps+1)),Nlist,'go')
plt.xlabel('# of Steps')
plt.ylabel('# of Particles In Box')
#For the first problem, we see a random system of particles every time we run the code.  This makes sense
#The plots for the second and third problem are the same, except that the plot for #3 is smoother
#This also makes sense, since #3 asks for an average number of particles


#For problem #3, we want to plot the average # of particles over multiple realizations of the experiment

Nparticles = 400 #number of particles in our box
L = 200 #Length of the box
l = 40 #size of the hole in the box
Trials = 10 #number of experiments to average over
Nsteps = 10000 #Number of loops
Nlists = []
Naverage = [] #empty list for the average number of particles
for j in range(Trials):
    X = np.zeros(Nparticles) #Create an array of x values
    Y = np.zeros(Nparticles) #Create an array of y values
    Nlist = [Nparticles]
    Nnow = Nparticles

    for i in range(Nsteps): #Create your loop
        p_index = random.randint(Nparticles) #Define random position index for the particles
        #Choose a random direction
        # 0 = Left, 1 = Right, 2 = Up, 3 = Down
        direction = random.randint(4) #Set the direction for the particle to move in
        if direction == 0 and X[p_index] >= -L:
            X[p_index] -= 1 #Particle moves to the left 1
        elif direction == 1 and X[p_index] <= L:
            X[p_index] += 1 #Particle moves to the right 1
        elif direction == 2 and Y[p_index] <= L:
            Y[p_index] += 1 #Particle moves up 1
        elif direction == 3 and Y[p_index] >= L:
            Y[p_index] -= 1 #Particle moves down one
    #Add in the hole
        if Y[p_index] == 0 and (L-l)/2 <= X[p_index] <= (L+l)/2:
            Y[p_index] = 1E10
            Nnow -= 1
        Nlist.append(Nnow)
    Nlists.append(Nlist)

for i in range(Nsteps+1):
    ilist = [] #blank list
    for j in Nlists:
        ilist.append(j[i])
    iaverage = np.mean(ilist) #take the average
    Naverage.append(iaverage) #append the average value of the particles
#Plot #3
    
plt.figure()
plt.plot(range(Nsteps+1),Naverage,'r')
plt.title('Hole in Box #2')
plt.xlabel('# of Steps')
plt.ylabel('# of Particles in Box')

#For problems four and five, we are computing entropy and the average entropy of the experiment

Nparticles = 400 #number of particles in our box
Slists = [] #lists for the entropy
Save = [] #average entropy
Trials = 10
L = 200 #Length of the box
Ncell = 100
Nsteps = 10000 #Number of loops
X = np.zeros(Nparticles) #Create an array of x values
Y = np.zeros(Nparticles) #Create an array of y values
t0 = 0 #initial time that the creamer is dropped into the coffee
tf = 100 #final time
t = np.linspace(t0,tf,Nsteps)
for j in range(Trials):
    X = np.zeros(Nparticles) #Create an array of x values
    Y = np.zeros(Nparticles) #Create an array of y values 
    for i in range(Nsteps): #Create your loop
        p_index = random.randint(Nparticles) #Define random position index for the particles
        #Choose a random direction
        # 0 = Left, 1 = Right, 2 = Up, 3 = Down
        direction = random.randint(4) #Set the direction for the particle to move in
        if direction == 0 and X[p_index] >= -L:
            X[p_index] -= 1 #Particle moves to the left 1
        if direction == 1 and X[p_index] <= L:
            X[p_index] += 1 #Particle moves to the right 1
        if direction == 2 and Y[p_index] <= L:
            Y[p_index] += 1 #Particle moves up 1
        if direction == 3 and Y[p_index] >= L:
            Y[p_index] -= 1 #Particle moves down one
        for k in range(Ncell):
            P = int(k/Ncell) #particle in the ith cell
            S = -np.sum(P*np.log(P)) #entropy formula

for i in range(Nsteps+1):
    ilist = []
    for j in Slists:
        ilist.append(j[i])
    iaverage = np.mean(ilist)
    Save.append(iaverage) #Take the average entropy
#Plot problem 4        
plt.figure()
plt.title('Entropy vs. Time #1')
plt.xlabel('Time (s)')
plt.ylabel('Entropy')
plt.plot(t,S,'go')

#Plot problem 5
plt.figure()
plt.title('Entropy vs. Time #2')
plt.xlabel('Time (s)')
plt.ylabel('Average Entropy')
plt.plot(t,Save,'r')

#Like with problems 2 and 3, we expect the plots for problems 4 and 5 to be the same, but 5 will be smoother
#I am not successfully getting plots for 4 and 5.  I know that the dimensions of S are messy, but I'm not sure how to fix them