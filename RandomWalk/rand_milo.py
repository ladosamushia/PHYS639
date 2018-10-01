import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

dir1 = [-1,1]
dir2 = [-1,-1,-1,1]

def stepping(dir):
    x = 0
    y = 0 
    step_size = [1,2,3]         # you have the ability to take a step of size 1 to size 3
    direction = dir             # in the +/- direction
        # Assume left is the -x direction
    i0 = 0
    ifin = 10
    
    ### FIND BETTER WAY TO MAKE ARRAYS
    position_x = np.array([])   # new position for every step
    position_y = np.array([])
    distance = np.array([])
    
    for i in range(i0,ifin):
        step = random.choice(step_size)*random.choice(direction)
        x += step    
        position_x = np.append(position_x, x)    
        position_y = np.append(position_y, y)    
        distance = np.append(distance,np.absolute(position_x[i]))
        
        #print position_x[i], position_y[i], distance[i]
        
   # ave_pos = np.mean(position_x)
    ave_dist = np.mean(distance)
    ### HOW DO YOU MAKE MULTIPLE PLOTS
    ### HOW TO PLOT ON A LINE
    ### HOW TO PLOT A LINE FOR AVE_DIST
    plt.xlabel('STEP')
    plt.ylabel('POSITION')
    plt.plot(position_x,'.')
    print 'The average distance is',ave_dist
    #plt.plot(position_x,position_y)