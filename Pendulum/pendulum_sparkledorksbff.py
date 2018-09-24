# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 09:35:20 2018

@author: jessica pietrowski
"""

#Same as before, except now we have an external force as well as damping velocity

import numpy as np
import matplotlib.pyplot as plt

#Here we are plotting the motion of a pendulum, except that the pendulum experiences a damping force proportional to velocity

#Define initial conditions
m = 5 #mass in kilograms
v = 0 #initial velocity in meters per second
g = 9.81 #acceleration due to gravity in meters per second squared
q = 1 #numerical value
theta = 10 #initial angle in radians
dtheta = 0 #derivative of initial theta
t0 = 0.0 #initial time in seconds
tf = 10.0 #final time in seconds
Nsteps = 10000 #number of steps
t = np.linspace(t0,tf,Nsteps) #range of t values
L = 2 #length of the string in meters
F = -m*g*np.sin(theta) #force due to gravity at angle theta
Fmax = 5
w = 30*np.pi/180

l = L*theta #path that the mass travels
dt = 0.001 #time derivative
theta = np.zeros(Nsteps) #range of theta values
theta[0] = (20*np.pi)/180 #initial value of theta at time t=0

for i in range(1,Nsteps):
    d2theta = -((g/L)*np.sin(theta[i-1])) #second derivative of theta:  acceleration
    dtheta += d2theta*dt #first derivative of theta:  velocity
    theta[i] = theta[i-1] + dtheta*dt #array of theta values

plt.plot(t,theta,'go',label='Simple Pendulum') #plotting theta versus time
plt.plot(t,theta[0]*np.cos(t*((g/L)**0.5)),'bo',label='Small Angle App.') #small angle approximation plot for comparison

#Now to plot theta versus time when the pendulum is damped
for i in range(1,Nsteps):
    d2theta = -((g/L)*np.sin(theta[i-1])) - (q*dtheta)#second derivative of theta
    dtheta += d2theta*dt #appended first derivative of theta
    theta[i] = theta[i-1] + dtheta*dt #appended theta
    if theta[i] > (90*np.pi/180): #If theta is greater than 90 degrees
        theta[i] = theta[i] - np.pi
    elif theta[i] < -(90*np.pi/180): #if theta is negative
        theta[i] = theta[i] + np.pi

plt.plot(t,theta,'red',label='Damped Pendulum')

#Now the pendulum is damped and has a driving frequency
for i in range(1,Nsteps):
    Fext = Fmax*(np.sin(w)) #Driving force
    d2theta = -((g/L)*np.sin(theta[i-1])) - (q*dtheta) + Fext #second derivative of theta
    dtheta += d2theta*dt #appended first derivative of theta
    theta[i] = theta[i-1] + dtheta*dt #appended theta
    if theta[i] > (90*np.pi/180): #If theta is greater than 90 degrees
        theta[i] = theta[i] - np.pi
    elif theta[i] < -(90*np.pi/180):
        theta[i] = theta[i] + np.pi

plt.plot(t,theta,'y-',label='Driving Pendulum') #plotting angle versus time
plt.title('Theta vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Angle (Radians)')
plt.legend()

#We have a maximum when w is equal to (g/L)**0.5.  This is what we expect.  Our sine waves are adding up with constructive interference

#Now to plot frequency versus amplitude and driving frequency versus maximum angle
def simple_frequency(L):
    amplitude = np.linspace(0.05*np.pi,0.95*np.pi,100) #define amplitude values
    frequencies = [] #creating a blank space for frequencies
    for theta in amplitude:
        v = 0 #velocity
        g = 9.81 #gravity
        t0 = 0 #initial time
        tf = 10 #final time
        dt = 0.001 #time derivative
        root = 0
        theta1 = theta #previous angle
        time = np.linspace(t0,tf,int(tf/dt)) #time to plot
        thetas = [] #blank space for storing thetas
        for t in time: #to append values
            thetas.append(theta) #adding extra theta values
            theta += v*dt #new theta value
            v += -(g/L)*np.sin(theta)*dt #new velocity value
            if theta < 0 and theta1 > 0:
                frequency = np.pi/(t-root) #new frequency
                root = t
            theta1 = theta
            
    frequencies.append(frequency) #adding frequency values
#plotting amplitude and frequency
    plt.figure()
    plt.xlabel('Amplitude')
    plt.ylabel('Frequency')
    plt.title('Simple Pendulum')
    plt.plot(amplitude,frequency,'r')

simple_frequency(2)

def damped_frequency(L,q):
    amplitude = np.linspace(0.05*np.pi,0.95*np.pi,100) #array of amplitude values
    frequencies = [] #blank space for frequency values
    for theta in amplitude:
        v = 0 #velocity
        g = 9.81 #gravity
        t0 = 0 #initial time
        tf = 10 #final time
        dt = 0.001 #time derivative
        root = 0
        theta1 = theta
        time = np.linspace(t0,tf,int(tf/dt))
        thetas = [] #blank space for thetas
        for t in time:
            thetas.append(theta) #appending theta
            theta += v*dt #new theta value
            v += (-(g/L)*np.sin(theta)-q*v)*dt #new velocity values
            if theta < 0 and theta1 > 0:
                frequency = np.pi/(t-root)
                root = t
            theta1 = theta
            
    frequencies.append(frequency)
    
    plt.figure()
    plt.xlabel('Amplitude')
    plt.ylabel('Frequency')
    plt.title('Simple Pendulum')
    plt.plot(amplitude,frequency,'g')
    
damped_frequency(2,1)

#Now to plot the driving frequency
def driving_frequency(theta0,L,q,amax):
    fdrives = np.linspace(0, 10, 100) #valules for driving frequency
    maximums = [] #maximum values

    for fdrive in fdrives:
        theta = theta0 #new initial angle
        v = 0 #velocity
        g = 9.81 #gravity
        t0 = 0 #initial time
        tf = 20 #final time
        dt = 0.001 #time derivative
        
        maximum = theta #setting the maximum value equal to theta
        time = np.linspace(t0,tf,int(tf/dt)) #range of time values
        thetas = [] #blank storage for thetas

        for t in time:
            thetas.append(theta) #appending theta
            theta += v*dt #new theta value
            v += ((-g/L)*np.sin(theta)-q*v+amax*np.sin(fdrive*t))*dt #new velocity
            if theta > maximum:
                maximum = theta
        maximums.append(maximum)
        
    plt.figure()
    plt.xlabel('Driving Frequency')
    plt.ylabel('Max Angle')
    plt.title('Damped Driven Pendulum')
    plt.plot(fdrive,maximums,'b')
    
driving_frequency(np.pi / 4, 10, 0.5, 0.75)

#My code works just fine for plots of angle versus time
#The code runs into problems for frequency versus amplitude and driving frequency versus maximum angle
#I don't entirely know what is wrong with my code.  None of my debugging attempts are working
#The append functions I'm trying to use are not working properly.  Again, I'm not sure why