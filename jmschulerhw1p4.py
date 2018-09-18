# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 20:36:11 2018

@author: Jared
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt

g = 9.8
m = 100
x0 = int(input("Initial position in the x-direction in meters:"))       # m. Initial position in x-axis
y0 = int(input("Initial position in the y-direction in meters:"))       # m. Initial position in Y-axis
v0 = int(input("Initial velcoity in m/s:"))     
deg = int(input("Launch angle (in degrees):"))                                  # degrees. Initial angle thrown.
dragco = 0.00004
tini = 0.0
tfin = 10000

earth_r = 6371000.00                # radius of the Earth
earth_m = 5.972e24                  # mass of the Earth
G_constant = 6.67409e-11            # gravitational constant 
G0 = ((earth_m)*G_constant)/((earth_r + y0)**2)

vx0 = (v0)*np.cos(theta)
vy0 = (v0)*np.sin(theta)

xp = np.zeros(stepsize+1)
yp = np.zeros(stepsize+1)
vpx = np.zeros(stepsize+1)
vpy = np.zeros(stepsize+1)
G = np.zeroes(stepsize+1)                   # need to do this since gravity will vary

vpx[0] = vx0
vpy[0] = vy0
xp[0] = x0
yp[0] = y0
G[0] = G0
stop_i = 0


# For some reason, I am getting my xp[i] on line 47 being returned as "Invalid syntax" error for no apparent reason..

for i in range (1, stepsize+1):
    G[i] = ((earth_m)*(G_constant)/((earth_r + yp[i-1] + vpy[i-1]*dt)**2)
    xp[i] = xp[i-1] + vpx[i-1]*dt
    yp[i] = yp[i-1] + vpy[i-1]*dt - (0.5)*(G[i-1])*dt**2
    vpy[i] = vpy[i-1] - G[i-1]*dt
    vpx[i] = vpx[i-1]
    if yp[i] <= 0:
        print "Final Height: " ,((yp[i] + yp[i-1])/2), "meters"
        print "Final Displacement: " xp[i], "meters"
        print "Time of impact: " ,dt*i, "s"
        print "    "
        stop_i = i
        break
    if yp[i-2] < yp[-1] and yp[i] < yp[i-1]:
        print "Maximum Altitude:" , yp[i-1], "meters"
        print "X Displacement at maximum altitude: ", xp[i-1], "meters"
        print "Time to maximum altitude: ", dt*i, "seconds"
        
plt.plot(xp[:stop_i], yp[:stop_i], 'g')
plt.xlabel("X Position (meters)")
plt.ylabel("Y Position (meters)")

