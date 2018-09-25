# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:47:33 2018

@author: Jared
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
from scipy.integrate import odeint

#initial conditions
tini = 0
tfin = 10
time = np.arange(tini, tfin, .025)
deg = 15.0                                              # Anything above around 10 degrees will break the nonlinear approximation
theta0 = np.radians(deg)
avx0 = np.radians(0.0)                                                # Angular velocity

#define equations and functions
def simple_pendulum(y0,t):
    theta, x = y0
    d2theta = [x, -(g/L)*np.sin(theta)]
    return d2theta

def plot_results(time, theta1, theta2):
    plt.plot(time, theta1[:,0], "r")
    plt.plot(time, theta2)
    
    plt.title('Pendulum Motion')
    plt.xlabel('time(s)')
    plt.ylabel('angle (rads)')
    plt.grid(True)
    plt.legend(['nonlinear', 'linear'], loc='lower right')
    plt.show()
    
    
#parameters
g = 9.8                                                 # m/s^2
L = 1.0                                                 # m
# Find solution to nonlinear problem
theta1 = odeint(simple_pendulum, [theta0, avx0], time)

# Find solution to linear problem
omega = np.sqrt(g/L)
theta2 = [theta0*np.cos(omega*t) for t in time]             # Stores as a list in theta2

# Plot results
plot_results(time, theta1, theta2)

# Amplitude vs Frequency of Oscillation
