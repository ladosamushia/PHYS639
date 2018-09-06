# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 13:10:39 2018

@author: Blaine Fry

This program plots a projectile path given the initial velocity, launch angle,
launch position, and landing altitude; air resistance, changing air density,
and changing gravity (inverse square) are taken into account.
"""

import numpy as np
from matplotlib import pyplot as plt

# define initial parameters
v0 = 825.0 # initial velocity in meters per second
x0 = 0.0 # initial x position in meters
y0 = 0.0 # initial y position in meters
m = 272.155 # mass of projectiles in kilograms
theta_deg = 15 # launch angle in degrees
yf = 0.0 # final y position (altitude of landing)
plot_figures = True

# vector decomposition
theta = (np.pi/180)*theta_deg # convert to radians
vy0 = v0*np.sin(theta)
vx0 = v0*np.cos(theta)

# set up time interval
t_i = 0.0 # start time in seconds
t_f = 100.0 # end time in seconds
N = 10**4 # number of sub intervals 
t = np.linspace(t_i,t_f,N) # time range
dt = (t_f - t_i)/N # small change in t for solving eqs

# constants for calculating acceleration due to gravity at a given altitude
m_earth = 5.9723e24 # mass of earth in kilograms (https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html)
r_earth = 6371.000e3 # volumetric mean radius of earth in meters (https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html)
G_const = 6.67408e-11 # gravitational constant (https://physics.nist.gov/cgi-bin/cuu/Value?bg|search_for=gravity)

# set up the equations
x = np.zeros(N) # array in which to store x positions
y = np.zeros(N) # array in which to store y positions
vx = np.zeros(N) # array in which to store x velocities
vy = np.zeros(N) # array in which to store y velocities
Fx = np.zeros(N) # array in which to store x forces
Fy = np.zeros(N) # array in which to store y forces
g = np.zeros(N) # array in which to store values of acceleration due to gravity
# set intial values
x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0

# solve the equations
for i in range(1,N): # starts at 1 bc the zeroth elements are determined
    g[i] = (-1)*(G_const*m_earth)/((r_earth + y[i-1])**2) # calculate newtonian gravitation
    Fx[i] = ((1.0 - 2.2e-5*y[i-1])**(5/2))*(-0.00004)*m*vx[i-1]*vx[i-1] # drag term (modified for rarification at high altitudes)
    Fy[i] = m*g[i] + ((1.0 - 2.2e-5*y[i-1])**(5/2))*(-0.00004)*m*vy[i-1]*vy[i-1]# gravity + modified drag term
    vx[i] = vx[i-1] + (Fx[i]/m)*dt
    vy[i] = vy[i-1] + (Fy[i]/m)*dt
    x[i] = x[i-1] + vx[i]*dt
    y[i] = y[i-1] + vy[i]*dt
    if y[i] <= yf:
        print 'range = ' + str(x[i]) + ' meters'
        break

if plot_figures is True:
    plt.figure(1)
    plt.grid(True)
    plt.title('Projectile Y Motion')
    plt.ylabel('altitude (m)')
    plt.xlabel('time (s)')
    plt.plot(t,y, 'b.')
    plt.xlim((-0.05)*t[i],(1.05)*t[i])
    
    plt.figure(2)
    plt.grid(True)
    plt.title('Projectile Path')
    plt.ylabel('altitude (m)')
    plt.xlabel('distance (m)')
    plt.plot(x,y, 'r.')

