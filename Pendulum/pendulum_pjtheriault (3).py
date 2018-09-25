
# coding: utf-8

# In[1]:


#Written by Paul Theriault
#The purpose of this program is to simulate pendulum motion
import numpy as np
import math
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#Problem I: Simple Pendulum 
a = float(input('Please input a launch angle in degrees between 0 and 90: '))
s = float(input('Please input length of string: '))
c = float(input('Please input a damping constant: '))
#Start by defining a function to call on 
def pendulum(L,g,T):
    #Initial Conditions
    t = 0
    dt = 0.01
    theta = math.radians(T)
    #I'll denote the differential equations as x2 = d^2theta/dt^2 and x1 = dtheta/dt
    x2 = 0
    x1 = 0
    #Let's make some arrays to store values
    ta = np.array([t])
    theta_a = np.array([theta])
    x2a = np.array([x2])
    #Let's run a loop to generate the values
    for i in range(1000):
        x2 = (-g/L)*np.sin(theta) #d^2theta/dt^2
        x1 += x2*dt #x2*dt gives dtheta/dt
        theta += x1*dt #x1*dt gives theta
        t += dt
        ta = np.append(ta,t)
        theta_a = np.append(theta_a,theta)
        x2a = np.append(x2a,x2)
    return [ta, theta_a]
#Now we make use of our function and plot it
[t0,theta0] = pendulum(s,10,1) #This plots a small angle approximation 
[t1,theta1] = pendulum(s,10,a) #This plots the users input
plt.plot(t0,theta0,label='Small angle')
plt.plot(t1,theta1,label='Your Input')
plt.title('Theta vs Time')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Theta');
plt.show()

#A small angle is included for convience; however large launch angles will blow up the graph (hard to see)    
#This approximation is easier to see for launch angles below 10 degrees   
    
#################################################################################################################################
    
#Let's check that the small angle holds up in small angle approximation 
#sin(x)=x for small x approximately 
#The following is a quick rewrite of the above except sin(x)=x now
def TEST(p,q,w): #p for size, q for gravity and w for angle
    z= 0
    dz = 0.01
    theta_z = math.radians(w)
    x4 = 0
    x3 = 0
    za = np.array([z])
    theta_az = np.array([theta_z])
    x4a = np.array([x4])
    for i in range(1000):
        x4 = (-q/p)*theta_z #d^2theta/dt^2
        x3 += x4*dz #x2*dt gives dtheta/dt
        theta_z += x3*dz #x1*dt gives theta
        z += dz
        za = np.append(za,z)
        theta_az = np.append(theta_az,theta_z)
        x4a = np.append(x4a,x4)
    return [za, theta_az]

[t3,theta3] = pendulum(s,10,1) #This plots a small angle  
[t2,theta2] = TEST(s,10,1) #This plots the sin(x)=x solution 
plt.plot(t3,theta3,label='Small angle')
plt.plot(t2,theta2,label='sin(x)=x solution')
plt.title('Small Angle Approximation Comparison')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Theta');
plt.show()

#Looking at the graph it's clear that pendulum(s,10,1) is the same as TEST(s,10,1)
#The only difference between the functions pendulum and TEST are that sin(x)=x in TEST

#################################################################################################################################

#Problem II Damped Pendulum Motion

#The only thing that changes in this problem is we slap on a damping effect that will cause the oscillations to decay

#Let's start by defining a function
def DAMP(L,g,T,V): #Where L=Length, g=Gravity, T=Angle, and V=Damping constant
    #Inital Conditions
    t = 0
    dt = 0.01
    x6 = 0
    x5 = 0
    theta = math.radians(a)
    #Let's make use of some arrays
    x6a = np.array([x6])
    ta = np.array([t])
    theta_a = np.array([theta])
    #Let's run a loop to generate values
    for i in range(1000):
        x6 = (-g/L)*np.sin(theta)-V*x5
        x5 += x6*dt
        theta += x5*dt
        t += dt
        x6a = np.append(x6a,x6)
        ta = np.append(ta,t)
        theta_a = np.append(theta_a,theta)
    return [ta, theta_a]
#Let's make use of our function and plot
[t4,theta4] = DAMP(s,10,a,0.5) #This plots a standard small damping constant for comparison
[t5,theta5] = DAMP(s,10,a,c) #This plots the users inputs 
plt.plot(t4,theta4,label='small damping q=0.05')
plt.plot(t5,theta5,label='User Input Damping')
plt.title('Theta vs Time with Damping')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Theta');
plt.show()

#The graph clearly shows that the larger the damping constant the faster the oscillation decays

#################################################################################################################################

#Lastly we need to make graphs of Frequency vs Amplitude for our pendulum 
#Sadly I couldn't determine how to do this; however, I'd be happy to learn how to do this. I'll stop by.

#frequency = 1/period. It's the length of one cycle
#Amplitude is the maximum point on the wave

#Final comments 
#Everything works as expected. Large damping quickly decays an oscillation. 

