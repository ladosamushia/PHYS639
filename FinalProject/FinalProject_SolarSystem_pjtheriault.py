# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:58:29 2018

@author: Angela
"""
import matplotlib
#matplotlib.use('GTKAgg') 
import numpy as np 
import matplotlib.pyplot as plt
import random 

pi = np.pi

#Note: You said to turn this in as is and to continue working on it in my spare time
#I will do this. Currently the code simulates the planets in the correct ellptical orbits
#Eventually I would like this Rogue Object to gravitationally attract the planets.

###########################################################################################

#This section defines a function for the mathematical calculations.
#NOTE: the t in the while loop is vital for how many years the animation will run.
#Ms = 1.98e30
def PLANET(x,y,vx,vy):
    t=0
    dt=0.001 
    clist = []
    xlist=[]
    ylist=[]
    while t<1: #t is in years this should correspond with the period of the orbit you're interested in.
        r=np.sqrt(x**2+y**2)
        vx = vx - ((4*pi**2*x)/r**3)*dt 
        x = x + vx*dt
        xlist.append(x)
        vy = vy - ((4*pi**2*y)/r**3)*dt 
        y = y + vy*dt
        ylist.append(y)
        clist.append((x, y))
        t=t+dt
    return xlist,ylist,clist

###########################################################################################
    
#This section defines array's and inital conditions for the planets and stores data.
#My planets start at perhelion with perhelion velocity in AU/year.
#The array ps holds the inital conditions and is passed through a loop and function.
#The array orbit then holds all of the information about the orbits for each planet. 
    
ps = []
#ps.append([x,y,vx,vy]                  Some Planet Information:
orbit = []                              #Planet:  Period:    Avg Vel.   Max Vel.
ps.append([0.3074961999,0,0,12.4343])   #Mercurey 0.24 years 47.4 km/s  58.98 km/s
ps.append([0.7184317819,0,0,7.4337])    #Venus    0.61 years 35.0 km/s  35.26 kn/s
ps.append([0.9832929499,0,0,6.3854])    #Earth    1.00 year  29.8 km/s  30.29 km/s
ps.append([1.381410723,0,0,5.5867])     #Mars     2.00 years 24.1 km/s  26.50 km/s
ps.append([4.95107964,0,0,2.8899])      #Jupiter  12.0 years 13.1 km/s  13.72 km/s
ps.append([9.0229557,0,0,2.1461])       #Saturn   29.0 years 9.70 km/s  10.18 km/s
ps.append([18.28212786,0,0,1.50295])    #Uranus   84.0 years 6.80 km/s  7.11  km/s
ps.append([29.81159956,0,0,1.15504])    #Neptune  163  years 5.40 km/s  5.50  km/s
ps.append([29.65776906,0,0,1.28859])    #Pluto    248  years 4.72 km/s  6.10  km/s
ps.append([random.randint(30,35),0,-random.randint(1,3),3,2.00e35]) #Rogue Object
for i in range(10): #was 8
    orbit.append(PLANET(ps[i][0], ps[i][1], ps[i][2], ps[i][3]))
#The array orbit stores all the information about the orbits.
 

y = np.array(orbit[3][1]) #Vector y 
x = np.array(orbit[3][0]) #Vector x
L = np.arctan2(y,x) #arctan2 accounts for the quadrent your angle is in
R = np.sqrt(x**2+y**2) #The magnitude of the vector (the len of R is needed later)

Rlist=[]
Llist=[]

###########################################################################################

#This section is the mathematical conversion from cartesian to polar.
#I go planet by planet in this section and for each x and y we find the Radial length in polar.
#I then find the polar angle using each of the x and y's. 
#I then add a shift to the polar angle (the longitude of perhelion) to rotate the planets to the correct positions.
#Note: I wasn't able to determine a simpler way to do this without going planet by planet.

y1 = np.array(orbit[0][1]) #All of Mercury's y's
x1 = np.array(orbit[0][0]) #All of Mercury's x's
y2 = np.array(orbit[1][1]) #Venus y's
x2 = np.array(orbit[1][0]) #Venus x's
y3 = np.array(orbit[2][1]) #Earth y's
x3 = np.array(orbit[2][0]) #Earth x's
y4 = np.array(orbit[3][1]) #Mars  y's
x4 = np.array(orbit[3][0]) #Mars  x's
y5 = np.array(orbit[4][1]) #Jupiter y's
x5 = np.array(orbit[4][0]) #Jupiter x's
y6 = np.array(orbit[5][1]) #Saturn  y's
x6 = np.array(orbit[5][0]) #Satrun  x's
y7 = np.array(orbit[6][1]) #Uranus  y's
x7 = np.array(orbit[6][0]) #Uranus  x's
y8 = np.array(orbit[7][1]) #Neptune y's
x8 = np.array(orbit[7][0]) #Neptune x's
y9 = np.array(orbit[8][1]) #Pluto   y's
x9 = np.array(orbit[8][0]) #Pluto   x's
###################################################
y10 = np.array(orbit[9][1]) #Rogue Object y's
x10 = np.array(orbit[9][0]) #Rogue Object x's

#The np.deg2rad angle is the logitude of perhelion 
#Addition of logitude of perhelion rotates postion to correct starting point.
L1 = np.arctan2(y1,x1)+np.deg2rad(77.45645)   #Mercury Polar Angle
R1 = np.sqrt(x1**2+y1**2)                     #Mercury Radial
L2 = np.arctan2(y2,x2)+np.deg2rad(131.53298)  #Venus Polar Angle
R2 = np.sqrt(x2**2+y2**2)                     #Venus Radial
L3 = np.arctan2(y3,x3)+np.deg2rad(102.94719)  #Earth Polar Angle
R3 = np.sqrt(x3**2+y3**2)                     #Earth Radial
L4 = np.arctan2(y4,x4)+np.deg2rad(336.04084)  #Mars Polar Angle
R4 = np.sqrt(x4**2+y4**2)                     #Mars Radial
L5 = np.arctan2(y5,x5)+np.deg2rad(14.75385)   #Jupiter Polar Angle
R5 = np.sqrt(x5**2+y5**2)                     #Jupiter Radial
L6 = np.arctan2(y6, x6)+np.deg2rad(92.43194)  #Saturn Polar Angle
R6 = np.sqrt(x6**2+y6**2)                     #Saturn Radial
L7 = np.arctan2(y7, x7)+np.deg2rad(170.96424) #Uranus Polar Angle
R7 = np.sqrt(x7**2+y7**2)                     #Uranus Radial 
L8 = np.arctan2(y8, x8)+np.deg2rad(44.97135)  #Neptune Polar Angle
R8 = np.sqrt(x8**2+y8**2)                     #Neptune Radial
L9 = np.arctan2(y9, x9)+np.deg2rad(224.06676) #Pluto Polar Angle
R9 = np.sqrt(x9**2+y9**2)                     #Pluto Radial 
######################################
L10 = np.arctan2(y10, x10)                    #Rogue Object Polar Angle
R10 = np.sqrt(x10**2+y10**2)                  #Rogue Object Radial 
#print(max(R8), min(R8), ps[9][0], ps[9][2])
##########################################################################################

#This section is the code for plotting the data into a polar animation.
#As far as I can tell there is not an obvious way to zoom in and out dynamically.
#I used if statements based off the size of R which is connected to the time in years.
#The code will zoom out twice to the outer edge of the Solar System.
#Note: Neptune and Pluto move very slowly and it's difficult to see them move.
#You many need to set time (t) to a larger value in the while loop in the function.

for i in range(np.size(R)):
        plt.clf()
        ax=plt.subplot(111, polar = True)
        #Line 133 plots Polar Angle and Radial for each i for Mercury, Venus, Earth, Mars and Rogue Object.
        plt.plot([L1[i], L2[i], L3[i], L4[i], L10[i]],[R1[i], R2[i], R3[i], R4[i], R10[i]],'o')
        #plt.plot([L[i]], [R[i]], 'o')
        ax.set_rticks([0.5, 1, 1.5, 2])    #less radial ticks
        ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
        label_position=ax.get_rlabel_position()
        ax.text(np.radians(label_position+20),ax.get_rmax()/2.,'AU',
        rotation=label_position,ha='center',va='center')
        ax.grid(True)
        ax.set_title("Solar System")
        ax.yaxis.labelpad=40
        #ax.set_ylabel("Distance from Sun (AU)", va='bottom')
        ax.set_rlim(0,2) #Sets radial distance cap
        ax.annotate('Sun', xy=(0,0))
        if i <=500:    
           ax.annotate('Mercury', xy=(L1[i],R1[i]))
           ax.annotate('Venus', xy=(L2[i],R2[i]))
           ax.annotate('Earth', xy=(L3[i],R3[i]))
           ax.annotate('Mars', xy=(L4[i],R4[i]))
           ax.annotate('Object', xy=(L10[i],R10[i]))
        if i >=500: 
            #plt.clf()
            #ax=plt.subplot(111, polar = True)
            plt.plot([L5[i], L6[i], L7[i]],[R5[i], R6[i], R7[i]], 'o')
            ax.set_rticks([4,8,12,16,20])
            ax.set_rlim(0,20)
            ax.annotate('Jupiter', xy=(L5[i],R5[i]))
            ax.annotate('Saturn', xy=(L6[i],R6[i]))
            ax.annotate('Uranus', xy=(L7[i],R7[i]))
            ax.annotate('Object', xy=(L10[i],R10[i]))
            #plt.pause(0.01)
        #plt.pause(0.01)
        if i >=700:
            plt.plot([L8[i], L9[i]], [R8[i], R9[i]], 'o')
            ax.set_rticks([4,8,12,16,20,24,28,32,34])
            ax.set_rlim(0,34)
            ax.annotate('Neptune', xy=(L8[i],R8[i]))
            ax.annotate('Pluto', xy=(L9[i],R9[i]))
        plt.pause(0.01)
        
#Much of the planetary orbital information came from these links
#Most of it from nssdc.gsfc.nasa.gov when clicking on the planet names. 
        
#https://www.princeton.edu/~willman/planetary_systems/Sol/
#http://farside.ph.utexas.edu/teaching/celestial/Celestialhtml/node34.html    
#https://nssdc.gsfc.nasa.gov/planetary/factsheet/    


