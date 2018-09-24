# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 13:25:53 2018

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

def simple_pendulum(alpha_initial,d_alpha_initial,make_plot,plot_number,store_period): # takes an initial angle as input. If you want a graph, set make_plot == True. If you want the periods to be stored for plotting, make store_period == True
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
    alpha[0] = np.deg2rad(alpha_initial) # rad
    d_alpha[0] = np.deg2rad(d_alpha_initial) # rad/s 
    # solve equations
    for i in range(1,N): # starts at 1 bc initial values (idx 0) are determined
        d_d_alpha[i] = (-1)*(g/l)*np.sin(alpha[i-1]) # undamped, undriven pendulum
        d_alpha[i] = d_alpha[i-1] + d_d_alpha[i]*dt
        alpha[i] = alpha[i-1] + d_alpha[i]*dt
        if alpha[i] > np.pi: # constrains motion to within +/- 180 deg
            alpha[i] -= 2*np.pi
        elif alpha[i] < -np.pi:
            alpha[i] += 2*np.pi
        if alpha[i] <= 0 and alpha[i-1] >= 0: # checks to see when pendulum passes through alpha = 0 from one direction
            T.append(t[i])
    frequency = 1/(T[1] - T[0]) # the period is the time between the values stored in the T list
    if store_period is True:
        frequencies.append(frequency) # stores periods for later comparison
    # plot motion
    if make_plot is True:
        plt.figure(plot_number)
        plt.title('Figure ' + str(plot_number) + ': Pendulum Angle vs Time')
        plt.plot(t,alpha,'.',label='init. angle = ' + str(alpha_initial) + ' degrees; init ang vel = ' + str(d_alpha_initial) + ' deg/s')
        plt.grid(True)
        plt.legend()
        plt.ylabel('Pendulum Angle (Radians)')
        plt.xlabel('Time (s)')

# let's just make some plots with it!
simple_pendulum(15,0,True,1,False)
simple_pendulum(15,40,True,1,False)    

# compare to small angle approx. as a check for validity
simple_pendulum(10,0,True,2,False) # starts at 10 deg, no initial velocity
# generate values from analytical solution
t_i = 0. # start time in seconds
t_f = 20. # end time in seconds
N = 10**4 # number of sub intervals 
t = np.linspace(t_i,t_f,N) # time range
l = 10 # length of pendulum
g = 9.8 # acceleration due to gravity
alpha_analytical = (np.deg2rad(10))*np.sin(t*np.sqrt(g/l)+np.deg2rad(85)) # I had to introduce a phase shift to get the plots to be on top of each other...
plt.figure(2)
plt.plot(t,alpha_analytical, label = 'analytcial solution for small angle')
plt.legend()
# The amplitude and period of the numerical solution line up nicely with the 
# small angle approx. I had to introduce a phase shift in the analytical solution
# to make it match with my code in terms of phase.

# compare period to amplitude        
for z in range(1,89): # call the pendulum function on a reasonable range of angles
    simple_pendulum(z,0,False,42,True) # for an d_alpha_initial = 0, the amplitude is the initial angle
    # as the pendulum function runs, it will store values for each starting angle in the periods list
# calculate period for the small angle approximation
f_small_angle = [1/(2*np.pi*np.sqrt(l/g))]*88
# make a plot to compare periods to the small angle approximation
plt.figure(3)
plt.title('Figure 3: Frequency vs Amplitude')
plt.plot(range(1,89),frequencies, label = 'Frequency as a function of Amplitude')
plt.plot(range(1,89),f_small_angle, label = 'small angle approx. frequency')
plt.grid(True)
plt.xlabel('Amplitude (Deg)')
plt.ylabel('Pendulum Frequency (Hz)')
plt.legend()
# the period/frequency of the small angle approx. depeneds only on l and g
# for the numerical solution, as the ampitude increases, the pendulum swings slower

"""
Problem: Damped Pendulum (lvl*)
Describe the motion of a pendulum that experiences a damping force proportional to 
velocity. Vary the coeffecient of this damping term and see if things make sense.
"""

def damped_pendulum(alpha_initial,d_alpha_initial,q,make_plot,plot_number):
    # define parameters
    g = 9.8 # acceleration due to gravity in m/s/s 
    l = 10 # length of pendulum in meters 
    # describe time interval
    t_i = 0. # start time in seconds
    t_f = 20. # end time in seconds
    N = 10**5 # number of sub intervals 
    t = np.linspace(t_i,t_f,N) # time range
    t.tolist()
    dt = (t_f - t_i)/N # small change in t for solving eqs
    # set up lists to store values as equations are propagated through time
    alpha = [0]*N # angle of pendulum in radians
    d_alpha = [0]*N # small change of alpha w/ respect to time
    d_d_alpha = [0]*N # small change of d_alpha w/ respect to time
    # set initial value
    alpha[0] = np.deg2rad(alpha_initial) # rad
    d_alpha[0] = np.deg2rad(d_alpha_initial) # rad/s 
    # solve equations
    for i in range(1,N): # starts at 1 bc initial values (idx 0) are determined
        d_d_alpha[i] = (-1)*(g/l)*np.sin(alpha[i-1]) - q*d_alpha[i-1] # damped, undriven pendulum
        d_alpha[i] = d_alpha[i-1] + d_d_alpha[i]*dt
        alpha[i] = alpha[i-1] + d_alpha[i]*dt
        if alpha[i] > np.pi: # constrains motion to within +/- 180 deg
            alpha[i] -= 2*np.pi
        elif alpha[i] < -np.pi:
            alpha[i] += 2*np.pi
    # plot motion
    if make_plot is True:
        plt.figure(plot_number)
        plt.title('Figure ' + str(plot_number) + ': Damped Pendulum')
        plt.plot(t,alpha,'.',label='init angle = ' + str(alpha_initial) + ' degrees; init vel = ' + str(d_alpha_initial) + ' deg/s; q = ' + str(q))
        plt.grid(True)
        plt.legend()
        plt.ylabel('Pendulum Angle (Radians)')
        plt.xlabel('Time (s)')

damped_pendulum(40,0,0,True,4)
damped_pendulum(40,0,0.125,True,4)
damped_pendulum(40,0,0.25,True,4)
damped_pendulum(40,0,2,True,4)

# as q increases (that is to say, as the damping is 'turned on'), the pendulum
# oscillations begin to decrease with time exponentially. The greater the q, the 
# faster the oscillations fall off, until the pendulum is overdamped like
# the red line. This behavior makes sense; the frequency appears to be conserved
# until overdamping occurs.

"""
Problem: Damped Driven Pendulum (lvl**)
Introduce a periodic driving force on the pendulum. Experiment with different 
amplitudes and frequencies of this force. Check for resonance and plot
maximum amplitude vs driving frequency.
"""

max_values = [] # list in which to store maximum angle values found by below code
omega_values = []
def damped_driven_pendulum(alpha_initial,d_alpha_initial,q,F_drive_amp,F_drive_frequency,make_plot,plot_number,store_max):
    # define parameters
    g = 9.8 # acceleration due to gravity in m/s/s 
    l = 2 # length of pendulum in meters 
    # describe time interval
    t_i = 0. # start time in seconds
    t_f = 20. # end time in seconds
    N = 10**5 # number of sub intervals 
    t = np.linspace(t_i,t_f,N) # time range
    t.tolist()
    dt = (t_f - t_i)/N # small change in t for solving eqs
    # set up lists to store values as equations are propagated through time
    alpha = [0]*N # angle of pendulum in radians
    d_alpha = [0]*N # small change of alpha w/ respect to time
    d_d_alpha = [0]*N # small change of d_alpha w/ respect to time
    # set initial value
    alpha[0] = np.deg2rad(alpha_initial) # rad
    d_alpha[0] = np.deg2rad(d_alpha_initial) # rad/s 
    # solve equations
    for i in range(1,N): # starts at 1 bc initial values (idx 0) are determined
        d_d_alpha[i] = (-1)*(g/l)*np.sin(alpha[i-1]) - q*d_alpha[i-1] + F_drive_amp*np.sin(F_drive_frequency*t[i-1]) # damped, undriven pendulum
        d_alpha[i] = d_alpha[i-1] + d_d_alpha[i]*dt
        alpha[i] = alpha[i-1] + d_alpha[i]*dt
        if alpha[i] > np.pi: # constrains motion to within +/- 180 deg
            alpha[i] -= 2*np.pi
        elif alpha[i] < -np.pi:
            alpha[i] += 2*np.pi
    if store_max is True:
        max_values.append(max(alpha))
        omega_values.append(F_drive_frequency)
    # plot motion
    if make_plot is True:
        plt.figure(plot_number)
        plt.title('Figure ' + str(plot_number) + ': Complex Pendulum')
        plt.plot(t,alpha,'.',label='init angle = ' + str(alpha_initial) + ' degrees; init vel = ' + str(d_alpha_initial) + ' deg/s; q = ' + str(q) + ' ; F_drv_amp = ' + str(F_drive_amp) + ' ; omega = ' + str(F_drive_frequency))
        plt.grid(True)
        #plt.legend()
        plt.ylabel('Pendulum Angle (Radians)')
        plt.xlabel('Time (s)')

# make a plot with it (figure 5)
damped_driven_pendulum(20,-10,0.3,0.8,np.sqrt(9.8/2),True,5,False)
# the pendulum is being driven at its resonant frequency... but it starts out of phase.
# the driving force kicks the pendulum into phase with it, then tends towards some
# equilibrium amplitude (it doesn't tend to infinity bc there's damping)

# let's try a range of driving forces (figure 6)
for f in range(0,5):
    damped_driven_pendulum(0,0,0.6,f*0.2,2,True,6,False)
# for this, I started the pendulum at alpha = 0, at rest, to see how the driving 
# force would start the pendulum swinging. The driving frequency is close to the resonant
# frequency. As the driving force increases, so does the equilibrium amplitude.
# feel free to uncomment the plt.legend() command.

# now let's examine a range of driving frequencies. (figure 7)
for z in range(0,5):
    damped_driven_pendulum(0,0,0.6,1,z*0.4,True,7,False)
# some driving frequencies make long, choppy plots. Others are smoother and have 
# higher peak amplitudes.

# plot max amplitude vs driving frequency
for w in range(0,200):
    damped_driven_pendulum(0,0,0.6,0.8,w*0.02,False,9,True)
plt.figure(8)
plt.plot(omega_values,max_values, 'o')
plt.title('Max Amplitude vs Driving Frequency')
plt.ylabel('Max Amplitude (Rad)')
plt.xlabel('Driving Frequency (Rad/s)')
plt.grid(True)
# hmm... The peak around sqrt(9.8/2) makes sense. That's the natural frequency
# of the pendulum. I expected a different (and symmetrical) pattern around that point though.
