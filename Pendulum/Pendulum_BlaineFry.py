# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:13:28 2018

@author: Blaine Fry
"""

# Phys 639 - Pendulum

"""
Problem: Simple Pendulum (lvl*)
Describe the motion of a simple (undamped, undriven) pendulum, and compare periods
for different starting angles. Check against the small angle approx. for validity.
"""

import numpy as np
from matplotlib import pyplot as plt

frequencies = [] # an empty list to store values of pendulum periods as they are calculated by the function below

def simple_pendulum(theta_initial,make_plot,plot_number,store_period): # takes an initial angle as input. If you want a graph, set make_plot == True. If you want the periods to be stored for plotting, make store_period == True
    # define parameters
    g = 9.8 # acceleration due to gravity in m/s/s 
    l = 10 # length of pendulum in meters 
    # describe time interval
    t_i = 0. # start time in seconds
    t_f = 20. # end time in seconds
    N = 10**4 # number of sub intervals 
    t = np.linspace(t_i,t_f,N) # time range
    t.tolist()
    dt = (t_f - t_i)/N # small change in t for solving eqs
    # set up lists to store values as equations are propagated through time
    alpha = [0]*N # angle of pendulum in radians
    d_alpha = [0]*N # small change of alpha w/ respect to time
    d_d_alpha = [0]*N # small change of d_alpha w/ respect to time
    T = [] # stores times when pendulum crosses alpha=0 to calculate period
    # set initial value
    alpha[0] = np.deg2rad(theta_initial)
    # solve equations
    for i in range(1,N): # starts at 1 bc initial values (idx 0) are determined
        d_d_alpha[i] = (-1)*(g/l)*np.sin(alpha[i-1]) # undamped, undriven pendulum
        d_alpha[i] = d_alpha[i-1] + d_d_alpha[i]*dt
        alpha[i] = alpha[i-1] + d_alpha[i]*dt
        if alpha[i] <= 0 and alpha[i-1] >= 0: # checks to see when pendulum passes through alpha = 0 from one direction
            T.append(t[i])
    frequency = 1/(T[1] - T[0]) # the period is the time between the values stored in the T list
    if store_period is True:
        frequencies.append(frequency) # stores periods for later comparison
    # plot motion
    if make_plot is True:
        plt.figure(plot_number)
        plt.title('Pendulum Angle vs Time')
        plt.plot(t,alpha,label='starting angle = ' + str(theta_initial) + ' degrees')
        plt.grid(True)
        #plt.legend()
        plt.ylabel('Pendulum Angle (Radians)')
        plt.xlabel('Time (s)')
    
# compare to small angle approx. as a check for validity
simple_pendulum(10,True,1,False)
# generate values from analytical solution
t_i = 0. # start time in seconds
t_f = 20. # end time in seconds
N = 10**4 # number of sub intervals 
t = np.linspace(t_i,t_f,N) # time range
l = 10 # length of pendulum
g = 9.8 # acceleration due to gravity
alpha_analytical = (np.deg2rad(10))*np.sin(t*np.sqrt(g/l)+np.deg2rad(85)) # I had to introduce a phase shift to get the plots to be on top of each other...
plt.plot(t,alpha_analytical, label = 'analytcial solution for small angle')
plt.legend()
# The amplitude and period of the numerical solution line up nicely with the 
# small angle approx. I had to introduce a phase shift in the analytical solution
# to make it match with my code in terms of phase.

# compare period to starting angle        
for z in range(1,89): # call the pendulum function on a reasonable range of angles
    simple_pendulum(z,False,42,True) # plot number doesn't matter
    # as the pendulum function runs, it will store values for each starting angle in the periods list
# calculate period for the small angle approximation
f_small_angle = [1/(2*np.pi*np.sqrt(l/g))]*88
# make a plot to compare periods to the small angle approximation
plt.figure(2)
plt.title('Frequency vs Initial Angle')
plt.plot(range(1,89),frequencies, label = 'Period as a function of initial angle')
plt.plot(range(1,89),f_small_angle, label = 'small angle approx. period')
plt.grid(True)
plt.xlabel('Initial Angle (Deg)')
plt.ylabel('Pendulum Frequency (Hz)')
plt.legend()