#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:41:52 2018

@author: dylansmac
"""

import numpy as np
import matplotlib.pyplot as plt

# Gravitational field model 

# using a gravitational model as reference for different models later on

m1 = 1
m2 = 1*(10**16)
r0 = 1*(10**5)
G = 6.67*(10**-11)
v0 = 0.001
dt = 0.1
t0 = 0.0

v = v0
r = r0
t = t0

height = []
time = []



while r > 0.001:
    r = r + v*dt
    g = -G*(m2)/(r**2)
    v = v + g*dt
    height.append(r)
    t += dt
    time.append(t)

plt.figure(1)
plt.title("Gravity Model")
plt.xlabel("Time (seconds)")
plt.ylabel("Height (meters)")
plt.plot(time,height)

#%% Particle in an electric field

# a electron is moving in a field equal to the charge of a proton

q1 = 1.6 *10**-19  #proton
q2 = -1.6*10**-19  #electron
k = 9 *10**9
r0 = 100
v0 = 0.001
dt = 0.1
t0 = 0
me = 9.109 * 10**-31

v = v0
t = t0
r = r0

distance = []
time = []

while r > 0:
    r = r + v*dt
    a = (k*q1*q2)/((r**2)*me)
    v = v + a*dt
    distance.append(r)
    t +=dt
    time.append(t)
    

plt.figure(2)
plt.title("Eletric Field Model")
plt.xlabel("Time (seconds)")
plt.ylabel("Distance (meters)")
plt.plot(time,distance)

#%% Particle in a non-uniform electric field

# An electron moving near a dipole system

q1 = 1.6 *10**-19  #proton
q2 = -1.6*10**-19
q3 = (1/3)*(-1.6*10**-19)
k = 9 *10**9
dt = 0.1
t0 = 0
me = 9.109 * 10**-31

x12 = 80.0
y12 = 60.0
theta12 = np.arctan(y12/x12)
r12 = np.sqrt(x12**2 + y12**2)

x23 = 30.0
y23 = 40.0
theta23 = np.arctan(y23/x23)
r23 = np.sqrt(x23**2 + y23**2)

vx = 0.001
vy = 0.001
v = np.sqrt(vx**2 + vy**2)

distance12 = []
distance23 = []
time = []
t = t0

steps = 10

#for i in range(steps):                          #since q2 and q3 are the same charge, r12 will go to zero
while r12 > 0:
    distance12.append(r12)
    distance23.append(r23)
    r12 = r12 - v*dt
    r23 = r23 + v*dt
    a12 = (k*q1*q2)/((r12**2) * me)
    a12x = a12*np.cos(theta12)
    a12y = a12*np.sin(theta12)
    a23 = (k*q2*q3)/((r23**2) * me)
    a23x = a23*np.cos(theta23)
    a23y = a23*np.sin(theta23)
    
    ax = a12x + a23x
    ay = a12y + a23y
    
    vx = vx + ax*dt
    vy = vy + ay*dt    
    v = np.sqrt(vx**2 + vy**2)
    
    x12 += vx*dt
    y12 += vy*dt
    theta12 = np.arctan(y12/x12)
    
    x23 -= vx*dt
    y23 -= vy*dt
    theta23 = np.arctan(y23/x23)
    
    time.append(t)
    t+=1
    
plt.figure(3)
plt.title("Dipole Electric Field Model")
plt.xlabel("Time")
plt.ylabel("Distance")
plt.plot(time,distance12,"r",label="Radius of q1 and q2")
plt.plot(time,distance23,"b",label = "Radius of q2 and q3")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)