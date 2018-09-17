# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 13:10:39 2018

@author: Blaine Fry
"""
### Phys 639 Projectile Motion
"""
Problem: Simple Projectile Motion (lvl *)
This code plots a projectile described by simple kinematic motion
WITHOUT air resistance, changing gravity, etc. 
"""

import numpy as np
from matplotlib import pyplot as plt

# define initial parameters
v0 = 400.0 # initial velocity in meters per second
x0 = 0.0 # initial x position in meters
y0 = 0.0 # initial y position in meters
g = -9.8 # acceleration due to gravity (m/s2)
theta_deg = 45.0 # launch angle in degrees
yf = 0.0 # final y position (altitude of landing)
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
# set up the equations
x = np.zeros(N) # array in which to store x positions
y = np.zeros(N) # array in which to store y positions
vx = np.zeros(N) # array in which to store x velocities
vy = np.zeros(N) # array in which to store y velocities
ax = np.zeros(N) # array in which to store x forces
ay = np.zeros(N) # array in which to store y forces
# set intial values
x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0
# solve the equations
for i in range(1,N): # starts at 1 bc the zeroth elements are determined
    ax[i] = 0.0
    ay[i] = g
    vx[i] = vx[i-1] + (ax[i])*dt
    vy[i] = vy[i-1] + (ay[i])*dt
    x[i] = x[i-1] + vx[i]*dt
    y[i] = y[i-1] + vy[i]*dt
    if y[i] <= yf:
        break
plt.figure(1)
plt.grid(True)
plt.title('Simple Projectile Path')
plt.ylabel('altitude (m)')
plt.xlabel('distance (m)')
plt.plot(x,y, 'go', label = 'program: range = ' + str(x[i]) + ' meters')
plt.legend()

# checking validity by comparing with kinematics:
y_kinematic = y0 + (np.tan(theta))*(x) + (0.5)*g*(((x)/(v0*np.cos(theta)))**2)
plt.figure(1)
plt.plot(x,y_kinematic, 'r.', label= 'kinematics')
plt.legend()
# the plots line up pretty well...

"""
Problem: Air Resistance (lvl *)
This program plots a projectile path without neglecting air resistance.
Air resistace follows F/m = -0.00004*v**2
"""
# define initial parameters
v0 = 400.0 # initial velocity in meters per second
x0 = 0.0 # initial x position in meters
y0 = 0.0 # initial y position in meters
g = -9.8 # acceleration due to gravity (m/s2)
theta_deg = 45.0 # launch angle in degrees
yf = 0.0 # final y position (altitude of landing)
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
# set up the equations
x = np.zeros(N) # array in which to store x positions
y = np.zeros(N) # array in which to store y positions
vx = np.zeros(N) # array in which to store x velocities
vy = np.zeros(N) # array in which to store y velocities
ax = np.zeros(N) # array in which to store x accelerations
ay = np.zeros(N) # array in which to store y accelerations
angle = np.zeros(N) # instantaneous angle in flight
a_drag = np.zeros(N) # acceleration due to air drag
a_drag_x = np.zeros(N)
a_drag_y = np.zeros(N)
# set intial values
x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0
# solve the equations
for i in range(1,N): # starts at 1 bc the zeroth elements are determined
    # calculate air resistance
    angle[i] = np.arctan(vy[i-1]/vx[i-1])
    a_drag[i] = -0.00004*((vx[i-1])*(vx[i-1])+(vy[i-1])*(vy[i-1]))
    a_drag_x[i] = a_drag[i]*np.cos(angle[i])
    a_drag_y[i] = a_drag[i]*np.sin(angle[i])
    # calculate x and y accelerations, velocities, and positions
    ax[i] = a_drag_x[i]
    ay[i] = g + a_drag_y[i]
    vx[i] = vx[i-1] + (ax[i])*dt
    vy[i] = vy[i-1] + (ay[i])*dt
    x[i] = x[i-1] + vx[i]*dt
    y[i] = y[i-1] + vy[i]*dt
    if y[i] <= yf: 
        break
plt.figure(2)
plt.grid(True)
plt.title('Projectile Path W/ air resistance')
plt.ylabel('altitude (m)')
plt.xlabel('distance (m)')
plt.plot(x,y, 'b.', label = 'range = ' + str(x[i]) + ' meters')
plt.legend()

# Comparing to simple projectile path:
plt.figure(1)
plt.plot(x,y, 'b.', label = 'air resistance: range = ' + str(x[i]) + ' meters')
plt.legend()
# That makes sense to me! The range was drastically reduced by drag.


"""
Problem: Changing Air Resistance (lvl *)
This program is like problem 2, but with an air resistance modified to 
reflect the changing density of the atmosphere with altitude.
"""
# define initial parameters
v0 = 400.0 # initial velocity in meters per second
x0 = 0.0 # initial x position in meters
y0 = 0.0 # initial y position in meters
g = -9.8 # acceleration due to gravity (m/s2)
theta_deg = 45.0 # launch angle in degrees
yf = 0.0 # final y position (altitude of landing)
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
# set up the equations
x = np.zeros(N) # array in which to store x positions
y = np.zeros(N) # array in which to store y positions
vx = np.zeros(N) # array in which to store x velocities
vy = np.zeros(N) # array in which to store y velocities
ax = np.zeros(N) # array in which to store x accelerations
ay = np.zeros(N) # array in which to store y accelerations
angle = np.zeros(N) # instantaneous angle in flight
a_drag = np.zeros(N) # accleration due to air drag
a_drag_x = np.zeros(N)
a_drag_y = np.zeros(N)
# set intial values
x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0
# solve the equations
for i in range(1,N): # starts at 1 bc the zeroth elements are determined
    # calculate air resistance
    angle[i] = np.arctan(vy[i-1]/vx[i-1])
    a_drag[i] = ((1.0 - 2.2e-5*y[i-1])**(5/2))*(-0.00004)*((vx[i-1])*(vx[i-1])+(vy[i-1])*(vy[i-1]))
    a_drag_x[i] = a_drag[i]*np.cos(angle[i])
    a_drag_y[i] = a_drag[i]*np.sin(angle[i])
    # calculate x and y accelerations, velocities, and positions
    ax[i] = a_drag_x[i]
    ay[i] = g + a_drag_y[i]
    vx[i] = vx[i-1] + (ax[i])*dt
    vy[i] = vy[i-1] + (ay[i])*dt
    x[i] = x[i-1] + vx[i]*dt
    y[i] = y[i-1] + vy[i]*dt
    if y[i] <= yf: 
        break
plt.figure(3)
plt.grid(True)
plt.title('Projectile Path W/ modified air resistance')
plt.ylabel('altitude (m)')
plt.xlabel('distance (m)')
plt.plot(x,y, 'g.', label = 'range = ' + str(x[i]) + ' meters')
plt.legend()

# The modified air resistance allowed the projectile to travel further.
# This would follow from the fact that the air resistance is lower at
# higher altitudes.

"""
Problem: Changing Gravity (lvl*)
This program plots a projectile path with modified air resistance and
gravity that changes with altitude.
"""

# define initial parameters
v0 = 400.0 # initial velocity in meters per second
x0 = 0.0 # initial x position in meters
y0 = 0.0 # initial y position in meters
theta_deg = 45.0 # launch angle in degrees
yf = 0.0 # final y position (altitude of landing)
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
ax = np.zeros(N) # array in which to store x accelerations
ay = np.zeros(N) # array in which to store y accelerations
angle = np.zeros(N) # instantaneous angle in flight
a_drag = np.zeros(N) # acceleration due to air drag
a_drag_x = np.zeros(N)
a_drag_y = np.zeros(N)
g = np.zeros(N) # array in which to store values of acceleration due to gravity
# set intial values
x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0
# solve the equations
for i in range(1,N): # starts at 1 bc the zeroth elements are determined
    # calculate air resistance
    angle[i] = np.arctan(vy[i-1]/vx[i-1])
    a_drag[i] = ((1.0 - 2.2e-5*y[i-1])**(5/2))*(-0.00004)*((vx[i-1])*(vx[i-1])+(vy[i-1])*(vy[i-1]))
    a_drag_x[i] = a_drag[i]*np.cos(angle[i])
    a_drag_y[i] = a_drag[i]*np.sin(angle[i])
    # calculate newtonian gravitation 
    g[i] = (-1)*(G_const*m_earth)/((r_earth + y[i-1])**2)  
    # calculate x and y accelerations, velocities, and positions
    ax[i] = a_drag_x[i]
    ay[i] = g[i] + a_drag_y[i]
    vx[i] = vx[i-1] + (ax[i])*dt
    vy[i] = vy[i-1] + (ay[i])*dt
    x[i] = x[i-1] + vx[i]*dt
    y[i] = y[i-1] + vy[i]*dt
    if y[i] <= yf: 
        break
plt.figure(4)
plt.grid(True)
plt.title('Projectile Path W/ modified air resistance & Gravity')
plt.ylabel('altitude (m)')
plt.xlabel('distance (m)')
plt.plot(x,y, 'k.', label = 'range = ' + str(x[i]) + ' meters')
plt.legend()

# Note that this part of the program predicts the lowest range.
# A brief investigation shows that the value of acceleration due to 
# gravity calculated using Newton's law of gravity and the constants I found
# predicts a slightly higher than accepted value for the acceleration at earth's
# surface:
print (-1)*(G_const*m_earth)/((r_earth)**2)
print '' 

"""
Problem: Battleship (lvl**)
This program takes the 2d position of launch and the 2d position of the target
and computes the optimal launch velocity and angle to fire a ballistic projectile
at the target. Air resistance, changing density of atmosphere with altitude, and
changing gravity (inverse square) are considered.
"""

def boom(x_cannon,y_cannon,x_target,y_target):
    # rename inputs to keep following code easier to type
    x0 = float(x_cannon)
    y0 = float(y_cannon)
    xf = float(x_target)
    yf = float(y_target)
    # set up time interval (breaks up flight time into N sub intervals)
    t_i = 0.0 # start time in seconds
    t_f = 150.0 # end time in seconds
    N =  10**4 # number of sub intervals # don't make too big
    T = np.linspace(t_i,t_f,N) # time range
    dt = (t_f - t_i)/N # small change in t for solving eqs  
    # constants for calculating acceleration due to gravity at a given altitude
    m_earth = 5.9723e24 # mass of earth in kilograms (https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html)
    r_earth = 6371.000e3 # volumetric mean radius of earth in meters (https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html)
    G_const = 6.67408e-11 # gravitational constant (https://physics.nist.gov/cgi-bin/cuu/Value?bg|search_for=gravity)   
    # run through loop of increasing launch velocities and angles
    impact = False # if impact is true, loops will break
    x_range = 0 # determines impact. must be initialized here or else things will be messed up in kernel
    for u in range(1,500): # test launch velocities
        v_launch = u # define launch velocity for this run
        for t in range(10,80): # runs through reasonable launch angles in degrees
            theta_deg_launch = float(t) # define launch angle for this run
            # vector decomposition
            v0 = float(v_launch)
            theta = (np.pi/180)*theta_deg_launch # convert to radians
            vy0 = v0*np.sin(theta)
            vx0 = v0*np.cos(theta)
            # set up the equations
            x = np.zeros(N) # array in which to store x positions
            y = np.zeros(N) # array in which to store y positions
            vx = np.zeros(N) # array in which to store x velocities
            vy = np.zeros(N) # array in which to store y velocities
            ax = np.zeros(N) # array in which to store x accelerations
            ay = np.zeros(N) # array in which to store y accelerations
            angle = np.zeros(N) # instantaneous angle in flight
            a_drag = np.zeros(N) # acceleration due to air drag
            a_drag_x = np.zeros(N)
            a_drag_y = np.zeros(N)
            g = np.zeros(N) # array in which to store values of acceleration due to gravity
            # set intial values
            x[0] = x0
            y[0] = y0
            vx[0] = vx0
            vy[0] = vy0
            # solve the equations
            for i in range(1,N): # starts at 1 bc the zeroth elements are determined
                # calculate air resistance
                angle[i] = np.arctan(vy[i-1]/vx[i-1])
                a_drag[i] = ((1.0 - 2.2e-5*y[i-1])**(5/2))*(-0.00004)*((vx[i-1])*(vx[i-1])+(vy[i-1])*(vy[i-1]))
                a_drag_x[i] = a_drag[i]*np.cos(angle[i])
                a_drag_y[i] = a_drag[i]*np.sin(angle[i])
                # calculate newtonian gravitation 
                g[i] = (-1)*(G_const*m_earth)/((r_earth + y[i-1])**2)  
                # calculate x and y accelerations, velocities, and positions
                ax[i] = a_drag_x[i]
                ay[i] = g[i] + a_drag_y[i]
                vx[i] = vx[i-1] + (ax[i])*dt
                vy[i] = vy[i-1] + (ay[i])*dt
                x[i] = x[i-1] + vx[i]*dt
                y[i] = y[i-1] + vy[i]*dt
                if y[i] <= yf:
                    x_range = x[i]
                    break
            if x_range >= xf:
                impact = True
                print ''
                print 'Optimal Launch Velocity = ' + str(v_launch) + ' m/s'
                print 'Launch angle = ' + str(theta_deg_launch) + ' degrees'
                plt.figure(5)
                plt.grid(True)
                plt.title('Battleship Projectile Path')
                plt.ylabel('altitude (m)')
                plt.xlabel('x-position (m)')
                plt.plot(x,y, 'r.')
                break
        if impact is True:
            break
    if impact is False:
        print 'No impact reached target. Check max velocity, angle range, or time of flight.'
  
# As a check for consitency, one can ask it to find the launch conditions
# for the range predicted by the previous sections of code. They should
# match up with the inputs of the previous code. This calculation will take
# a long time, though!           
#boom(0,0,11364.6458,0)

# The launch velocity is consistent with the previous code,
# but the angle falls short by 3 degrees. I didn't have this problem
# with smaller ranges, so I'm not sure why it's occuring.


# If you want it to run in a reasonable time, try the following:
boom(0,0,50,0)
