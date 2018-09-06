#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:01:11 2018

@author: dylan0611
"""

"""

This code uses the basic kinematic equations to find the path of a particle
thown. It divides the equations into two dimensions: X and Y. 

"""

import numpy as np
import matplotlib.pyplot as plt

                                #Defining variables
a = -9.8
h0 = 0.001
x0 = 0.0
vx0 = 10.0
vy0 = 100.0
steps = 1000.0

#%%     Projectile
def vy(t):                      #Velocity in the Y direction
    return a*t + vy0

def x(t):                       #Position in the X direction
    return vx0*t + x0 

def y(t):                       #Position in the Y direction
    return .5*(a)*(t**2) + (vy0)*t + h0 

t = 0.0

while y(t) > 0.0001:            #Loops looking for zeros 
    if t < 1000:
        t = t +.00001
    else:
        print "Fail"
        break

while y(t) < 0:                 #Loops looking for zeros
    if t > 0:
        t = t - .00001
    else:
        print "t going to be less than 0"
        break
    
else:                           #If loops are false, print out and graph solution
    print "t is: ", t, " when the particle hits the ground"
    print x(t), y(t)
    tf = t
    dt = np.linspace(0.0, tf, steps)
    plt.plot(x(dt), y(dt), "b", label="No Drag")

 
#%%   Projectile with constant drag 
                                #Defining variables and drag equations
mass = 20
dragy = -0.00004*(vy(t)**2)
dragx = -0.00004*(vx0**2)

def xd(t):                      #Position in X direction 
    return dragx*(t**2) + vx0*t + x0 

def yd(t):                      #Position in Y direction
    return .5*(a + dragy)*(t**2) + (vy0)*t + h0 

t = 0.0

while yd(t) > 0.0001:           #Loops looking for zeros
    if t < 1000:
        t = t +.00001
    else:
        print "Fail"
        break

while yd(t) < 0:                #Loops looking for zeros
    if t > 0:
        t = t - .00001
    else:
        print "t going to be less than 0"
        break
    
else:                           #If loops are false, print and graph solution
    print "t is: ", t, " when the particle hits the ground"
    print xd(t), yd(t)
    tfd = t
    dtd = np.linspace(0.0, tfd, steps)
    plt.plot(xd(dtd), yd(dtd),"r", label="Drag")
    plt.xlabel("Distance")
    plt.ylabel("Height")
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
