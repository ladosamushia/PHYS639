# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 13:06:47 2018

@author: jessi
"""
#In this problem we are coding simple projectile motion
#All we want to know is how far the projectile flies before it hits the ground

import numpy as np
import matplotlib.pyplot as plt

x = 0 #initial horizontal position in meters
y = 0 #initial vertical position in meters
vx = 20 #initial velocity in the x direction in m/s
vy = 20 #initial y velocity in the x direction in m/s
g = -9.81 #acceleration due to gravity in m/s**2
t = 0 #initial time in seconds
dt = 0.001 #time increment to change by
xlist =[x] #list of x values including initial position
ylist = [y] #list of y values including initial position

while y > 0 or t == 0:
    x += vx * dt #new x
    y += vy * dt #new y
    xlist.append(x) #new list for x
    ylist.append(y) #new list for y
    vy += g * dt #new velocity value in y direction
    t += dt #changing time value

    
print('Distance', x)
plt.plot(xlist,ylist,'go')

#In this problem we are coding projectile motion with air resistance

x = 0 #initial horizontal position in meters
y = 0 #initial vertical position in meters
vx = 20 #initial velocity in the x direction in m/s
vy = 20 #initial y velocity in the x direction in m/s
g = -9.81 #acceleration due to gravity in m/s**2
t = 0 #initial time in seconds
dt = 0.001 #time increment to change by
xlist =[x] #list of x values including initial position
ylist = [y] #list of y values including initial position

while y > 0 or t == 0:
    m = 5 #mass in kilograms
    theta = (50*np.pi)/180
    x += vx * dt #new x
    y += vy * dt #new y
    xlist.append(x) #new list for x
    ylist.append(y) #new list for y
    t += dt #changing time value
    v = (vx**2 + vy**2)**0.5 #total velocity in m/s
    Fdrag = m*(-0.00004*(v**2))
    Fx = Fdrag*np.cos(theta)
    Fy = Fdrag*np.sin(theta)
    vy += (g * dt) + (Fy * dt)
    vx += -Fx * dt
    
print('Distance', x)
plt.plot(xlist,ylist,'go')

#Here, air resistance changes with altitude

m = 5 #mass in kilograms
x = 0 #initial horizontal position in meters
y = 0 #initial vertical position in meters
vx = 20 #initial velocity in the x direction in m/s
vy = 20 #initial y velocity in the x direction in m/s
g = -9.81 #acceleration due to gravity in m/s**2
t = 0 #initial time in seconds
dt = 0.001 #time increment to change by
xlist =[x] #list of x values including initial position
ylist = [y] #list of y values including initial position

while y > 0 or t == 0:
    theta = (50*np.pi)/180
    x += vx * dt #new x
    y += vy * dt #new y
    h = y #altitude with respect to the sea level in meters
    xlist.append(x) #new list for x
    ylist.append(y) #new list for y
    t += dt #changing time value
    v = (vx**2 + vy**2)**0.5 #total velocity in m/s
    Fdrag = (m*(-0.00004*(v**2)))*((1-((2.2*(10**-5))*h))**2.5)
    Fx = Fdrag*np.cos(theta)
    Fy = Fdrag*np.sin(theta) 
    vy += (g * dt) + (Fy * dt)
    vx += -Fx * dt
    
print('Distance', x)
plt.plot(xlist,ylist,'go')

#For this problem, altitude is dropping and so is air resistance
#We need to account for the change in gravity as altitude changes

m = 5 #mass of projectile in kilograms
M = 5.974*(10**24) #mass of the Earth in kilograms
G = -6.674*(10**-11) #gravitational constant
r = 6.374*(10**6) #radius of the earth in meters
x = 0 #initial horizontal position in meters
y = 0 #initial vertical position in meters
vx = 200 #initial velocity in the x direction in m/s
vy = 200 #initial y velocity in the x direction in m/s
g = -9.81 #acceleration due to gravity in m/s**2
t = 0 #initial time in seconds
dt = 0.001 #time increment to change by
xlist =[x] #list of x values including initial position
ylist = [y] #list of y values including initial position

while y > 0 or t == 0:
    theta = (np.arctan(vy/vx))*np.pi/180
    x += vx * dt #new x
    y += vy * dt #new y
    h = y #altitude with respect to the sea level in meters
    xlist.append(x) #new list for x
    ylist.append(y) #new list for y
    t += dt #changing time value
    v = (vx**2 + vy**2)**0.5 #total velocity in m/s
    Fdrag = (m*(-0.00004*(v**2)))*((1-((2.2*(10**-5))*h))**2.5) #drag force
    Fx = Fdrag*np.cos(theta) #Force in the x direction
    Fy = Fdrag*np.sin(theta) + ((G*m*M)/((y+r)**2)) #force in the y direction
    vy += (g * dt) + (Fy * dt) #new y velocity
    vx += -Fx * dt #new x velocity
    
def projectile(v, theta):  #Here we are trying to hit a target from a ship
    xtarget = 800 #x range in meters
    ytarget = 0 #y range in meters
    def canon_range(v0,theta): #This is the range of the canon, dependent on velocity and angle
        x, y = projectile(v0,theta,True,False) #Values for x and y
        return np.max(x) #maximum value of x:  the position of the target
        v0 = 10 #initial velocity
        dv0 = 10 #initial velocity derivative
        Nsteps = 100 #Steps for our graph
        theta = np.linspace(0,90,Nsteps) #range of angles
        x_range = np.zeros(Nsteps) #range for x
        target_missed = True #If the canon misses the target
        while target_missed:
            v0 += dv0
        for i in range(Nsteps):
            x_range[i] = canon_range(v0,theta[i]) #Range of x values if the canon misses the target
        if xtarget > np.min(x_range) and xtarget < np.max(x_range):
             target_missed = False #Canon hits the target
        idx = (np.abs(x_range - xtarget)).argmin()
        print('velocity is:', v0) #velocity value for success
        print('angle is:', theta[idx]) #angle value for success

        [x,y] = projectile(v0, theta[idx]) #defining x and y
        plt.plot(x,y)
        plt.plot(xtarget, ytarget, '*',markersize=16) #plot to show that the canon hit the target

