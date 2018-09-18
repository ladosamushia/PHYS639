# -*- coding: utf-8 -*-
"""
Created on Tue Sep 04 13:24:24 2018

@author: Jared
"""
import numpy as np
import matplotlib.pyplot as plt
import math 

# For loop constructed with reference from Philip Lucas' code. 
# Initial Values and Constants
g = 9.8                                    # m/s^2. Gravitational constant of the Earth at surface
m = 100                                    # kg. Mass of thrown object.
x0 = int(input("Initial position in the x-direction in meters:"))       # m. Initial position in x-axis
y0 = int(input("Initial position in the y-direction in meters:"))       # m. Initial position in Y-axis
v0 = int(input("Initial velcoity in m/s:"))                             # m/s. Initial velocity thrown at angle theta
tini = 0.0                                  # s. Initial time
tfin = 50.0                                 # s. Final time for program to run too.
deg = int(input("Launch angle (in degrees):"))                        # degrees. Initial angle thrown.

# Derivative stuff/computational values to set
stepsize = 100000                                                                # times dt counts, or "steps"
t = np.linspace(tini,tfin,stepsize+1)
dt = (tini + tfin)/stepsize
theta = (deg*math.pi)/180.0                                                     # Gives the desired theta in radians

# X and Y components of initial velocity v0
v0x = (v0)*np.cos(theta)
float(v0x)
v0y = (v0)*np.sin(theta)
float(v0y)

# Since doing a *lot* of steps, setup an array for said values to be entered into.
xp = np.zeros(stepsize+1)               # Updates the x-position over time
yp = np.zeros(stepsize+1)               # Updates the y-position over time
vxp = np.zeros(stepsize+1)              # Updates the x-component of v0 over time
vyp = np.zeros(stepsize+1)              # Updates the y-component of v0 over time

# Make sure your initial positions defined above are the initial values set in your arrays
xp[0] = x0                              
yp[0] = y0
vxp[0] = v0x                           
vyp[0] = v0y


# Now, setup the for loop. 
# The for loop will have the equations for velocity and displacement in both x and y directions
# Will also posessess a break when the equation hits zero again for the y-component

for i in range(1,stepsize+1):           # Array starts at bleh[1] then continues to stepsize
    xp[i] = xp[i-1] + v0x*dt            # Since no drag, your x-value is the same however you must include the displacement from before to get a *true* displacement
    yp[i] = yp[i-1] + vyp[i-1]*dt - (.5)*g*dt**2
    vyp[i] = vyp[i-1] - g*dt
    if yp[i-2] < yp[i-1] and yp[i] < yp[i-1]:
        print "Maximum height achieved at:", yp[i-1], "m"
        print "X displacement at maximum height:" ,xp[i-1], "m"
        print "Time to maximum height:" ,dt*i, "s"
        
    if yp[i] <= 0:
        print "Final Achieved Height:" , ((yp[i] + yp[i-1])/2), "m"
        print "Range achieved: " ,xp[i], "m"
        print "Time at impact:" ,dt*i, "s"
        print ""
        stop_i = i 
        break
    
plt.plot(xp[:stop_i],yp[:stop_i],'r')
plt.xlabel("X position (m)")
plt.ylabel("Y position (m)")

# Part 2 With Drag

#print " Part 2: Drag"
#print " "
#
#drag0x = ((dragco)*(v0)**2)*np.cos(theta)
#drag0y = ((dragco)*(v0)**2)*np.sin(theta)
#
#xpd = np.zeros(stepsize+1)
#ypd = np.zeros(stepsize+1)
#dragpx = np.zeros(stepsize+1)
#dragpy = np.zeros(stepsize+1)
#
#dragpx[0] = drag0x
#dragpy[0] = drag0y
#xpd[0] = x0
#ypd[0] = y0
#
#stop_i = 0
#
#for i in range(1, stepsize+1):
#    xpd[i]=xp[i-1] + vxp[i-1]*dt - (.5)*dragpx[i-1]*dt**2     
#    ypd[i]=yp[i-1] + vyp[i-1]*dt - (.5)*(g + dragpy[i-1])*dt**2
#    if dragpy[i-1] < 0:
#        dragpy[i-1] = -dragpy[i-1]
#    else:
#        dragpy[i-1] = dragpy[i-1]
#    vyp[i] = vpy[i-1] - g*dt - dragpy[i-1]*dt
#    vxp[i] = vpx[i-1] - dragpx[i-1]*dt
#    if yp[i-1] <=0:
#        print "Final Height Achieved: " , ((yp[i]-yp[i-1])/2), "meters"
#        print "Distance Covered: " , xp[i], "m"
#        print "Time of impact: " ,dt*i, "s"
#        print ""
#        stop_i = i 
#        break
#    if yp[i-2] < yp[i-1] and yp[i] < yp[i-1]:
#        print "Maximum Height Achieved:" ,y_p[i-1], "m"
#        print " X Displacement at Maximum Height:" ,xp[i-1], "m"
#        print "Time to Maximum Height:" ,dt*i, "s"
#        
#plt.plot(xpd[:stop_i], ypd[:stop_i], 'r')
#plt.xlabel("X position (m)")
#plt.ylabel("Y position (m)")

    