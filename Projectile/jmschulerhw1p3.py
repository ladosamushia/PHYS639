# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 20:12:38 2018

@author: Jared
"""

import numpy as np
import math
import matplotlib.pyplot as plt

# # Initial Values and Constants
g = 9.8                                     # m/s^2. Gravitational constant of the Earth at surface
m = 100                                     # kg. Mass of thrown object.
x0 = int(input("Initial position in the x-direction in meters:"))       # m. Initial position in x-axis
y0 = int(input("Initial position in the y-direction in meters:"))       # m. Initial position in Y-axis
v0 = int(input("Initial velcoity in m/s:"))     
deg = int(input("Launch angle (in degrees):"))                                  # degrees. Initial angle thrown.
dragco = 0.00004                            # Drag coefficient
tini = 0.0
tfin = 50.0

# Derivative stuff to set up
stepsize = 100000                           # times dt counts, or "steps"
t = np.linspace(tini,tfin,stepsize+1)
dt = (tini + tfin)/stepsize
theta = (deg*math.pi)/180.0  
    
# X and Y components of initial velocity v0
v0x = (v0)*np.cos(theta)
v0y = (v0)*np.sin(theta)
#vt = (m*g)/(dragco)                         # Terminal velocity
    
# X and Y components of drag
drag0x = ((dragco)*(v0)**2)*np.cos(theta)
drag0y = ((dragco)*(v0)**2)*np.sin(theta)
    
xp = np.zeros(stepsize+1)
yp = np.zeros(stepsize+1)
vpx = np.zeros(stepsize+1)
vpy = np.zeros(stepsize+1)
dragpx = np.zeros(stepsize+1)
dragpy = np.zeros(stepsize+1)

xp[0]=x0
yp[0]=y0
vpx[0]=v0x
vpy[0]=v0y
dragpx[0] = drag0x
dragpy[0] = drag0y
    
stop_i = 0

for i in range(1,stepsize+1):
    xp[i] = xp[i-1] + vpx[i-1]*dt -(0.5)*dt - (0.5)*dragpx[i-1]*dt**2
    yp[i] = yp[i-1] + vpy[i-1]*dt -(0.5)*(g + dragpy[i-1]*dt**2)
    if dragpy[i-1] < 0:
        dragpy[i-1] = -dragpy[i-1]
    else: dragpy[i-1] = dragpy[i-1]
    vpy[i] = vpy[i-1] - g*dt - dragpy[i-1]*(((1-(1.22e-5)*(y0+vpy[i-1]*dt))**(5/2)))*dt
    vpx[i] = vpx[i-1] - dragpx[i-1]*(((1-(1.22e-5)*yp[i-1])**(5/2)))*dt
    if yp[i] <= 0 :
        print "Final Height Achieved: " , ((yp[i]-yp[i-1])/2), "meters"
        print "Distance Covered: " ,xp[i], "meters"
        print "Time of impact: ", dt*i, "seconds"
        print ""
        stop_i = i
        break
    if yp[i-2] < yp[i-1] and yp[i] < yp[i-1]:
        print "Maximum Height Achieved: " ,yp[i-1], "meters"
        print "X Displacement at Maximum Height: ", xp[i-1], "meters"
        print "Time to maximum altitude: " ,dt*i, "seconds"
    
plt.plot(xp[:stop_i], yp[:stop_i])
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")