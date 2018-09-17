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




#%%     Projectile
                                #Defining variables
a = -9.8
h0 = 0.001
x0 = 0.0
vx0 = 100.0
vy0 = 500.0
steps = 1000.0

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


##%   Projectile with constant drag 
#                                #Defining variables and drag equations
#mass = 20
#dragy = -0.00004*(vy(t)**2)
#dragx = -0.00004*(vx0**2)
#
#def xd(t):                      #Position in X direction 
#    return dragx*(t**2) + vx0*t + x0 
#
#def yd(t):                      #Position in Y direction
#    return .5*(a + dragy)*(t**2) + (vy0)*t + h0 
#
#t = 0.0
#
#while yd(t) > 0.0001:           #Loops looking for zeros
#    if t < 1000:
#        t = t +.00001
#    else:
#        print "Fail"
#        break
#
#while yd(t) < 0:                #Loops looking for zeros
#    if t > 0:
#        t = t - .00001
#    else:
#        print "t going to be less than 0"
#        break
#    
#else:                           #If loops are false, print and graph solution
#    print "t is: ", t, " when the particle hits the ground"
#    print xd(t), yd(t)
#    tfd = t
#    dtd = np.linspace(0.0, tfd, steps)
#    plt.plot(xd(dtd), yd(dtd),"r", label="Constant Drag")
#    plt.xlabel("Distance")
#    plt.ylabel("Height")
#    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#%

dt = 0.01
tini = 0.0
y = 0.001
x = 0.0
vx = 100.0
vy = 500.0

x_coord = []
y_coord = []

while y > 0.0001:
    x = x + vx*dt
    y = y + vy*dt
    v2 = vx**2 + vy**2
    vx = vx + (-0.00004*v2)*vx/np.sqrt(v2)*dt
    vy = vy - 9.8*dt + (-0.00004*v2)*vy/np.sqrt(v2)*dt
    x_coord.append(x)
    y_coord.append(y)

plt.figure(1)
plt.plot(x_coord, y_coord,"r", label= "Drag")
plt.xlabel("Distance")
plt.ylabel("Height")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


#%%    Projectile with dynamic drag
    

#def h(t):
#    
#dc = (1-(2.2 * (10**-5))*h)**(2.5)
#dragdx = -0.00004*(vx0**2)*dc
#dragdy = -0.00004*(vy(t)**2)*dc
#
#
#
#def xdd(t):                      
#    return dragdx*(t**2) + vx0*t + x0 
#
#def ydd(t):
#    return .5*(a + dragdy)*(t**2) + (vy0)*t + h0 
#
#t = 0.0
#
#while ydd(t) > 0.0001:           #Loops looking for zeros
#    if t < 1000:
#        t = t +.00001
#    else:
#        print "Fail"
#        break
#
#while ydd(t) < 0:                #Loops looking for zeros
#    if t > 0:
#        t = t - .00001
#    else:
#        print "t going to be less than 0"
#        break
#    
#else:                           #If loops are false, print and graph solution
#    print "t is: ", t, " when the particle hits the ground"
#    print xdd(t), ydd(t)
#    tfdd = t
#    dtdd = np.linspace(0.0, tfdd, steps)
#    plt.plot(xdd(dtdd), ydd(dtdd),"g", label="Dynamic Drag")
#    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

dt = 0.01
tini = 0.0
y = 0.001
x = 0.0
vx = 100.0
vy = 500.0
mass = 100

x_coordd = []
y_coordd = []



while y > 0.0001:
    x = x + vx*dt
    y = y + vy*dt
    ax = ((-0.00004 * (1-(2.2*(10**-5)*y))**(2.5))*v2)*vx/np.sqrt(v2)
    ay = -9.8 + ((-0.00004 * (1-(2.2*(10**-5)*y))**(2.5))*v2)*vy/np.sqrt(v2)
    v2 = vx**2 + vy**2
    vx = vx + ax*dt
    vy = vy + ay*dt
    x_coordd.append(x)
    y_coordd.append(y)

plt.plot(x_coordd, y_coordd,"y", label= "Dynamic Drag")
plt.xlabel("Distance")
plt.ylabel("Height")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#%%Dynamic Gravity and Drag

dt = 0.01
tini = 0.0
y = 0.001
x = 0.0
vx = 100.0
vy = 500.0
mass = 100
R = (6.371*(10**6))
G = (6.67*(10**-11))
Me = (5.972 * (10**24))



x_coorddg = []
y_coorddg = []



while y > 0.0001:
    x = x + vx*dt
    y = y + vy*dt
    g = -G*(Me)/((R+y)**2)
    ax = ((-0.00004 * (1-(2.2*(10**-5)*y))**(2.5))*v2)*vx/np.sqrt(v2)
    ay = g + ((-0.00004 * (1-(2.2*(10**-5)*y))**(2.5))*v2)*vy/np.sqrt(v2)
    v2 = vx**2 + vy**2
    vx = vx + ax*dt
    vy = vy + ay*dt
    x_coorddg.append(x)
    y_coorddg.append(y)

plt.plot(x_coorddg, y_coorddg,"grey", label= "Dynamic Drag & Gravity")
plt.xlabel("Distance")
plt.ylabel("Height")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#%%Battleship approximation

dt = 0.01
tini = 0.0
y = 0.001
x = 0.0
#vx = 100.0
#vy = 100.0
mass = 100
R = (6.371*(10**6))
G = (6.67*(10**-11))
Me = (5.972 * (10**24))
v = 1


xf = input("Distance from target: ")
yf = input("Height of target: ")
theta = np.arctan(2*yf/xf)
print theta

vx = v*np.cos(theta)
vy = v*np.sin(theta)

x_cordb = []
y_cordb = []
s_cordb = []

def test(x, y, v, vx, vy):
        x = x+vx*dt
        y = y+vy*dt
        g = -G*(Me)/((R+y)**2)
        ax = ((-0.00004 * (1-(2.2*(10**-5)*y))**(2.5))*v)*vx/np.sqrt(v)
        ay = g + ((-0.00004 * (1-(2.2*(10**-5)*y))**(2.5))*v)*vy/np.sqrt(v)
        vx = vx + ax*dt
        vy = vy + ay*dt
        x_cordb.append(x)
        y_cordb.append(y)
        s = yf
        s_cordb.append(s)
    
while y > 0.0001:
    test(x, y, v, vx, vy)
    if xf-5 > x > xf+5:
        if yf-5 > y > yf+5:
            plt.figure(2)
            plt.plot(x_cordb, y_cordb,"grey", label= "Projectile")
            plt.plot(s_cordb, label = "Battleship")
            plt.xlabel("Distance")
            plt.ylabel("Height")
            plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
            break
        else:
            v = v+0.1
            y = 0.001
            x = 0.0
