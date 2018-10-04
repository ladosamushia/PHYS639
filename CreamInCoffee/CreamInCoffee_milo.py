import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

"""
S = -SUM[ Ni * ln( Ni )]
"""


# hole is True if there is a hole
hole = True

def Container(H):
    hole = H

    N_particles = 200
    N_grid = 5  # size of container
    N_steps = 10000 # total times the particles will move all together
    X = np.zeros(N_particles) # particle x position
    Y = np.zeros(N_particles) # poarticle y position
    
    outside = N_grid + 1
    inside = N_grid
    
    top = 1 # top of hole
    bot = 0 # bottom of hole
    
    N_outside = np.zeros(N_steps)
    N_inside = np.zeros(N_steps)
    
    # loop N_step times
    # each loop randomly chooses a particle
    # then chooses the possible directions for it to move depending on its X and Y
    # then randomly chooses a direction for it to move
    # then stores its new location
    
    # 0 - left , 1 - right , 2 - up , 3 - down
    for i in range(N_steps):
        part = random.randint(N_particles) # choose a random particle
    
        # particle can move in any direction while inside the hole
        if hole == True and X[part] >= inside and X[part] <= outside and Y[part] <= top and Y[part] >= bot:
            direction = np.array([0,1,2,3])
    
        # chooses possible directions to move if not inside the hole
        else:
            direction = np.array([]) # reset empty array
    
            if X[part] != outside and X[part] != -inside :
                direction = np.append(direction, 0)
            if X[part] != inside and X[part] != -outside :
                direction = np.append(direction, 1)
            if Y[part] != inside and Y[part] != -outside :
                direction = np.append(direction, 2)
            if Y[part] != outside and Y[part] != -inside :
                direction = np.append(direction, 3)
        
        # chooses random possible direction
        DIR = random.choice(direction) 
        
        # stores new location
        if DIR == 0 :
            X[part] -= 1
        if DIR == 1 :
            X[part] += 1
        if DIR == 2 :
            Y[part] += 1
        if DIR == 3 :
            Y[part] -= 1
     
        #print X[part] , Y[part] , '\n',direction
        incount = 0
        outcount = 0
        for p in range(N_particles):   
            if X[p] <= inside and X[p] >= -inside and Y[p] <= inside and Y[p] >= -inside:
                incount +=  1
            
            outcount = N_particles - incount
        #print i, incount , outcount
        N_outside[i] = outcount
        N_inside[i] = incount
        #print N_outside
        
    # Finds average of particles outside for blocks of time
    divi = 250 #number of steps in an average
    aves = np.zeros(N_steps/divi)
    step = np.zeros(N_steps/divi)    
    for a in range(N_steps/divi):
        average = np.mean(N_outside[a*divi:(a+1)*divi])
        steps = (a+1)*divi        
        step[a] = steps        
        aves[a] = average
        #print steps, average
        
    plt.plot(N_outside)    
    plt.plot(step, aves)
    plt.grid(True)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    border = Rectangle((-N_grid,-N_grid),2*N_grid,2*N_grid,linewidth=1, edgecolor= 'black', facecolor='none', zorder=1)
    ax.add_patch(border)
    plt.grid(True)
    
    if hole == True:    
        plt.plot([N_grid,N_grid], [bot,top], 'w', zorder=2) 

    plt.scatter(X,Y,zorder = 3)
    
 
    print '\n(1) if the particle looks like it is on the border, it is inside of the box'
    print '(2) if the particle is inside the hole, it is considered outside the box'
    print '\nParticles inside:', N_inside[N_steps-1]
    print '\nParticles outside:', N_outside[N_steps-1]
