# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 19:42:23 2018

@author: jessi
"""

#Jessica Pietrowski
#Final project:  baseball with spin
#We will need to account for air resistance as well as the spin

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#To begin:  define some constants

x = 0.0 #initial horizontal position in meters
y = 1.5 #initial vertical position in meters
z = 0.0
vx = 20.0 #initial velocity in the x direction in m/s
vy = 20.0 #initial y velocity in the y direction in m/s
vz = 20.0 #initial z velocity in the z direction in m/s
g = -9.81 #acceleration due to gravity in m/s**2
t = 0.0 #initial time in seconds
dt = 0.001 #time increment to change by
xlist =[x] #list of x values including initial position
ylist = [y] #list of y values including initial position
zlist = [z] #list of z values including initial position

#Air resistance
while y > 0 or t == 0:
    m = 0.145 #mass in kilograms
    theta = (50*np.pi)/180
    x += vx * dt #new x
    y += vy * dt #new y
    z += vz * dt
    xlist.append(x) #new list for x
    ylist.append(y) #new list for y
    zlist.append(z)
    t += dt #changing time value
    v = (vx**2 + vy**2 + vz**2)**0.5 #total velocity in m/s
    Fdrag = m*(-0.00004*(v**2)) #Define the drag force
    Fx = Fdrag*np.cos(theta) #Drag force in the x direction
    Fy = Fdrag*np.sin(theta) #Drag force in the y direction
    vy += (g * dt) + (Fy * dt) #appending the value of y-velocity
    vx += -Fx * dt #appending the value of x-velocity
    
print('Distance', x)
plt.figure(1)
plt.plot(xlist,zlist,'go',label='No Spin')
plt.xlabel('Distance (m)')
plt.title('Baseball with Air Resistance')
plt.legend()


#Now to try and account for the spin
#I'm also trying to factor in gravity and changing altitude
#We need to define a new force, Fm, which will be the spin-dependent force

x = 0.0 #initial horizontal position in meters
y = 1.5 #initial vertical position in meters
z = 0.0
vx = 20.0 #initial velocity in the x direction in m/s
vy = 20.0 #initial y velocity in the y direction in m/s
vz = 20.0 #initial z velocity in the z direction in m/s
M = 5.974*(10**24) #mass of the Earth in kilograms
G = -6.674*(10**-11) #gravitational constant
r = 6.374*(10**6) #radius of the earth in meters
g = -9.81 #acceleration due to gravity in m/s**2
w = 2200 #rotational speed of the baseball in revolutions/min
t = 0.0 #initial time in seconds
dt = 0.001 #time increment to change by
S = 6.1*(10**-5) #Spin coefficient, keeping in mind that the textbook says S/m is approximately 4.1 * 10**-4
xlist =[x] #list of x values including initial position
ylist = [y] #list of y values including initial position
zlist = [z] #list of z values including initial position

while y > 0 or t == 0: #Nothing in this section is being registerd as 'defined'
    m = 0.145 #mass in kilograms
    theta = (np.arctan(vy/vx))*np.pi/180
    x += vx * dt #new x
    y += vy * dt #new y
    h = y #altitude with respect to the sea level in meters
    xlist.append(x) #new list for x
    ylist.append(y) #new list for y
    t += dt #changing time value
    v = (vx**2 + vy**2 + vz**2)**0.5 #total velocity in m/s
    Fdrag = (m*(-0.00004*(v**2)))*((1-((2.2*(10**-5))*h))**2.5) #drag force
    Fx = Fdrag*np.cos(theta) #Force in the x direction
    Fy = Fdrag*np.sin(theta) + ((G*m*M)/((y+r)**2)) #force in the y direction
    Fm = S*w*vx #The spin force, only present in the x-direction
    vy += (g * dt) + (Fy * dt) #new y velocity
    vx += -Fx * dt #new x velocity
    vz += -Fm*dt #add in the effect of spin
    z += vz * dt #append z a final time
    zlist.append(z)
    
plt.figure(1)
plt.plot(xlist,zlist,'r-',label='Spin')
plt.legend()

fig = plt.figure(2)
ax = fig.add_subplot(222,projection='3d')
ax.plot(xlist,ylist,zlist,'r-')
print('Distance',x)
print('Z direction', z)
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title('Baseball w/ Spin, Gravity, Changing Air Reistance')




