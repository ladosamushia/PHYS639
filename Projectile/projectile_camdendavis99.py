# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:18:10 2018

@author: Camden
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Initial Values - always leave uncommented

# Initializes all initial values and constants
x0 = 0.0
y0 = 0.0
v0 = 100.0
theta0 = 45.0
vx0 = v0 * np.cos(theta0 * (np.pi / 180.0))
vy0 = v0 * np.sin(theta0 * (np.pi / 180.0))
g = 9.8
t_i = 0.0
dt = 0.05
m = 0.5

# Initializes arrays for each variable. Each only holds initial value at first
x = [x0]
y = [y0]
t = [t_i]
vx = [vx0]
vy = [vy0]

#------------------------------------------------------------------------------

# Problem 1: Simple Projectile Motion

# Generates all values of t, vx, vy, x, and y
a = -g
index = -1
while True:
    index += 1
    t.append(t[index] + dt)
    vx.append(vx[index])
    vy.append(vy[index] + (a * dt))
    x.append(x[index] + (vx[index] * dt))
    y.append(y[index] + (vy[index] * dt))
    
    # Finds the final value of t
    if y[index + 1] < 0:
        break
    t_f = t[index + 1]
    
partitions = 1000
t_expected = np.linspace(t_i, t_f, partitions)
def x_expected(x0, vx0, t):
    return(x0 + (vx0 * t))
def y_expected(y0, vy0, g, t):
    return(y0 + (vy0 * t) - (0.5 * g * t * t))

# Graphs 
plt.plot(x, y, 'ro')
plt.plot(x_expected(x0, vx0, t_expected), y_expected(y0, vy0, g, t_expected), 'g')
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Path of projectile")

print("The projectile hits the ground at t = {:.2f}".format(t_f))

#------------------------------------------------------------------------------

# Problem 2: Air Resistance

## Calculates Acceleration
#def a(m, g, v):
#    a_g = -g
#    a_d = (-0.00004 * v * v) / m
#    return(a_g + a_d)
#
## Generates all values of t, vx, vy, x, and y
#index = -1
#while True:
#    index += 1
#    t.append(t[index] + dt)
#    vx.append(vx[index] + (a(m, 0, vx[index]) * dt))
#    vy.append(vy[index] + (a(m, g, vy[index]) * dt))
#    x.append(x[index] + (vx[index] * dt))
#    y.append(y[index] + (vy[index] * dt))
#    
#    # Finds the final value of t
#    if y[index + 1] < 0:
#        break
#    t_f = t[index + 1]
#    
#partitions = 1000
#t_expected = np.linspace(t_i, t_f, partitions)
#def x_expected(x0, vx0, t):
#    return(x0 + (vx0 * t))
#def y_expected(y0, v0y, g, t):
#    return(y0 + (vy0 * t) - (0.5 * g * t * t))
#
## Graphs 
#plt.plot(x, y, 'ro')
#plt.plot(x_expected(x0, vx0, t_expected), y_expected(y0, vy0, g, t_expected), 'g')
#plt.xlabel("x (m)")
#plt.ylabel("y (m)")
#plt.title("Path of projectile")
#
#print("The projectile hits the ground at t = {:.2f}".format(t_f))

#------------------------------------------------------------------------------

# Problem 3: Changing Air Resistance

## Calculates acceleration
#def a(m, g, v, h):
#    a_g = -g
#    a_d = (-0.00004 * v * v * math.pow(1 - 2.2 * math.pow(10, -5) * h, 5.0/2.0)) / m
#    return(a_g + a_d)
#
## Generates all values of t, vx, vy, x, and y
#index = -1
#while True:
#    index += 1
#    t.append(t[index] + dt)
#    vx.append(vx[index] + (a(m, 0, vx[index], y[index]) * dt))
#    vy.append(vy[index] + (a(m, g, vy[index], y[index]) * dt))
#    x.append(x[index] + (vx[index] * dt))
#    y.append(y[index] + (vy[index] * dt))
#    
#    # Finds the final value of t
#    if y[index + 1] < 0:
#        break
#    t_f = t[index + 1]
#    
#partitions = 1000
#t_expected = np.linspace(t_i, t_f, partitions)
#def x_expected(x0, vx0, t):
#    return(x0 + (vx0 * t))
#def y_expected(y0, v0y, g, t):
#    return(y0 + (vy0 * t) - (0.5 * g * t * t))
#
## Graphs 
#plt.plot(x, y, 'ro')
#plt.plot(x_expected(x0, vx0, t_expected), y_expected(y0, vy0, g, t_expected), 'g')
#plt.xlabel("x (m)")
#plt.ylabel("y (m)")
#plt.title("Path of projectile")
#
#print("The projectile hits the ground at t = {:.2f}".format(t_f))

#------------------------------------------------------------------------------

# Problem 4: Changing Gravity

## Calculates acceleration
#def a(m, v, h, gravityToggle):
#    M = 5.972 * math.pow(10, 24)
#    G = 6.674 * math.pow(10, -11)
#    R = 6.371 * math.pow(10, 6)
#    r = R + h
#    a_g = -(G * M) / (r * r) * gravityToggle
#    a_d = -(0.00004 * v * v * math.pow(1 - (2.2 * math.pow(10, -5) * h), 5.0/2.0)) / m
#    return(a_g + a_d)
#
## Generates all values of t, vx, vy, x, and y
#index = -1
#while True:
#    index += 1
#    t.append(t[index] + dt)
#    vx.append(vx[index] + (a(m, vx[index], y[index], 0) * dt))
#    vy.append(vy[index] + (a(m, vy[index], y[index], 1) * dt))
#    x.append(x[index] + (vx[index] * dt))
#    y.append(y[index] + (vy[index] * dt))
#    
#    # Finds the final value of t
#    if y[index + 1] < targetHeight and x[index + 1] > targetDistance:
#        break
#    t_f = t[index + 1]
#    
#partitions = 1000
#t_expected = np.linspace(t_i, t_f, partitions)
#def x_expected(x0, vx0, t):
#    return(x0 + (vx0 * t))
#def y_expected(y0, v0y, g, t):
#    return(y0 + (vy0 * t) - (0.5 * g * t * t))
#
## Graphs 
#plt.plot(x, y, 'ro')
#plt.plot(x_expected(x0, vx0, t_expected), y_expected(y0, vy0, g, t_expected), 'g')
#plt.xlabel("x (m)")
#plt.ylabel("y (m)")
#plt.title("Path of projectile")
#
#print("The projectile hits the ground at t = {:.2f}".format(t_f))

#------------------------------------------------------------------------------

# Problem 5: "Battleship" - UNFINISHED

#targetDistance = 5000
#targetHeight = 500
#
## Calculates force due to gravity
#def Fg(m, h):
#    M = 5.972 * math.pow(10, 24)
#    G = 6.674 * math.pow(10, -11)
#    R = 6.371 * math.pow(10, 6)
#    r = R + h
#    return(-(G * M * m) / (r * r))
#
## Calculates force due to drag
#def Fd(v, h):
#    scalingFactor = math.pow(1 - (0.000022 * h), 2.5)
#    return(-(0.00004 * v * v * scalingFactor))
#
## Calculates acceleration
#def a(m, v, h, gravityToggle):
#    return(((Fg(m, h) * gravityToggle) + Fd(v, h)) / m)
#
#optimalAngle = 420.0
#lowest_v0 = 999999.0
#outOfRange = True
#angle = 45.0
#vIncrement = 100
#
#if targetHeight > y0:
#    passedTargetHeight = False
#else:
#    passedTargetHeight = True
#passedTargetDistance = False
#
#vx0 = v0 * np.cos(angle * (np.pi / 180.0))
#vy0 = v0 * np.sin(angle * (np.pi / 180.0))
#
#x = [x0]
#y = [y0]
#t = [t_i]
#vx = [vx0]
#vy = [vy0]
#
#index = -1
#while True:
#    index += 1
#    
#    t.append(t[index] + dt)
#    vx.append(vx[index] + (a(m, vx[index], y[index], 0) * dt))
#    vy.append(vy[index] + (a(m, vy[index], y[index], 1) * dt))
#    x.append(x[index] + (vx[index] * dt))
#    y.append(y[index] + (vy[index] * dt))
#    
#    print(x[index + 1], y[index + 1])  
#    
#    height = y[index + 1]
#    distance = x[index + 1]
#    
#    if height >= targetHeight and not passedTargetHeight:
#        passedTargetHeight = True
#    
#    if height >= 1 / 0.000022:
#        v0 -= vIncrement
#        
#        vx0 = v0 * np.cos(angle * (np.pi / 180.0))
#        vy0 = v0 * np.sin(angle * (np.pi / 180.0))
#
#        x = [x0]
#        y = [y0]
#        t = [t_i]
#        vx = [vx0]
#        vy = [vy0]
#        index = -1
#    
#    if height < targetHeight and not passedTargetHeight:
#        v0 += vIncrement
#        
#        vx0 = v0 * np.cos(angle * (np.pi / 180.0))
#        vy0 = v0 * np.sin(angle * (np.pi / 180.0))
#
#        x = [x0]
#        y = [y0]
#        t = [t_i]
#        vx = [vx0]
#        vy = [vy0]
#        index = -1
#            
#    if height <= targetHeight and passedTargetHeight:
#        if abs(distance - targetDistance) < 100:
#            break
#        elif distance < targetDistance and not passedTargetDistance:
#            v0 += vIncrement
#        elif distance > targetDistance and passedTargetDistance:
#            v0 -= vIncrement
#        elif distance < targetDistance:
#            vIncrement /= 4
#            v0 += vIncrement
#            passedTargetDistance = False
#        elif distance > targetDistance:
#            vIncrement /= 4
#            v0 -= vIncrement
#            passedTargetDistance = True
#        
#        vx0 = v0 * np.cos(angle * (np.pi / 180.0))
#        vy0 = v0 * np.sin(angle * (np.pi / 180.0))
#
#        x = [x0]
#        y = [y0]
#        t = [t_i]
#        vx = [vx0]
#        vy = [vy0]
#        index = -1
#    