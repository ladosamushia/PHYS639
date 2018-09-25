# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:09:57 2018

@author: Mikelobe
"""


import numpy as np
import matplotlib.pyplot as plt

#Problem 1 Simple Pendulum

g=9.8 #acceleration due to gravity
L=100 #length of the string/pendulum
ti=0 #initial time
tf=100 #final time
q=0.1 #damping constant
F=0.01 #Force max that is applied into Force external
O=0.313 #omega driving force frequency
Steps=1000
theta=np.deg2rad(15) #initial angle theta
Vtheta=0 #initial velocity of theta
Atheta=-(g/L) #initial acceleration of theta
t=np.linspace(ti,tf,Steps+1)
dt=(tf-ti)/Steps
t_array=np.array(ti) #time array
theta_array=np.array(theta) #theta array
Vtheta_array=np.array(Vtheta) #velocity array
for i in range (1,Steps): #Second Order Differential Equation
    Atheta=-(g/L)*np.sin(theta)
    Vtheta=Vtheta+Atheta*dt
    theta=theta+Vtheta*dt
    theta_array=np.append(theta_array,theta)
    Vtheta_array=np.append(Vtheta_array,Vtheta)
    t_array=np.append(t_array,(i)*dt)
plt.subplot(221)
plt.plot(t_array,theta_array,'r-')
plt.xlabel('time in seconds')
plt.ylabel('theta in radians')
plt.title('theta vs time')

#Small Angle Approximation

t=np.linspace(ti,tf,Steps+1)
dt=(tf-ti)/Steps
t_array=np.array(ti)
theta_array=np.array(theta)
Vtheta_array=np.array(Vtheta)
for i in range (1,Steps):
    Atheta=(-(g/L)*theta) #assume angle theta small enough that sin theta = theta
    Vtheta=Vtheta+Atheta*dt
    theta=theta+Vtheta*dt
    theta_array=np.append(theta_array,theta)
    Vtheta_array=np.append(Vtheta_array,Vtheta)
    t_array=np.append(t_array,(i)*dt)
plt.plot(t_array,theta_array,'g-')

#For angles below 30 degrees the approximation is very close to the actual.
#and it is especially close when below 15 degrees.

#Problem 2 Damped Pendulum

t=np.linspace(ti,tf,Steps+1)
dt=(tf-ti)/Steps
t_array=np.array(ti)
theta_array=np.array(theta)
Vtheta_array=np.array(Vtheta)
for i in range (1,Steps): #Second Order Differential Equation but with Dampening
    Atheta=-(g/L)*np.sin(theta)-(q*Vtheta) #Damped Acceleration
    Vtheta=Vtheta+Atheta*dt
    theta=theta+Vtheta*dt
    theta_array=np.append(theta_array,theta)
    Vtheta_array=np.append(Vtheta_array,Vtheta)
    t_array=np.append(t_array,(i)*dt)
plt.plot(t_array,theta_array,'b-')

#The higher the q value the quicker it becomes 0, as in the quicker it becomes
#completely damped, which is expected because q determines the rate at which the
#function damps. At a certain q the function won't even go below 0; it will just
#go to 0 and stay there.

#Problem 3 Damped Driven Pendulum

t=np.linspace(ti,tf,Steps+1)
dt=(tf-ti)/Steps
t_array=np.array(ti)
theta_array=np.array(theta)
Vtheta_array=np.array(Vtheta)
for i in range (1,Steps): #Second Order Differential Equation including Dampening and External Force
    Atheta=-(g/L)*np.sin(theta)-(q*Vtheta)+(F*np.sin(i*dt*O)) #Damped and Driven Acceleration
    Vtheta=Vtheta+Atheta*dt
    theta=theta+Vtheta*dt
    theta_array=np.append(theta_array,theta)
    Vtheta_array=np.append(Vtheta_array,Vtheta)
    t_array=np.append(t_array,(i)*dt)
plt.plot(t_array,theta_array,'y-')

#Based on the omega changes the wavelength of the function, and changing the
#force max changes the amplitude of the function. If omega is made to be the
#sqrt of g/L then the graph will level out like the simple pendulum but it
#will have a much higher amplitude.

#Damped Driven Pendulum Plot for frequency vs amplitude

dO = 0.01 #change in omega driving frequency
O = dO #omega driving frequency
Of = 5 #final omega driving frequency
O_array=np.array(0.0)
maxtheta_array=np.array(0.0)
while (O <= Of): #loop to collect omega values and their amplitudes and store them to be plotted
    maxtheta = 0
    t=np.linspace(ti,tf,Steps+1)
    dt=(tf-ti)/Steps
    t_array=np.array(ti)
    theta_array=np.array(theta)
    Vtheta_array=np.array(Vtheta)
    for i in range (1,Steps):
        Atheta=-(g/L)*np.sin(theta)-(q*Vtheta)+(F*np.sin(i*dt*O))
        Vtheta=Vtheta+Atheta*dt
        theta=theta+Vtheta*dt
        if(theta > maxtheta): #if statement to know if we store the theta value
            maxtheta = theta
        theta_array=np.append(theta_array,theta)
        Vtheta_array=np.append(Vtheta_array,Vtheta)
        t_array=np.append(t_array,(i)*dt)
    O_array=np.append(O_array,O)
    maxtheta_array=np.append(maxtheta_array, maxtheta)
    O += dO
plt.subplot(222)
plt.plot(O_array,maxtheta_array,'g-')
plt.xlabel('omega frequency')
plt.ylabel('amplitude')
plt.title('frequency vs amplitude')

#there is a high peak at where the frequency would have resonance for that specific
#driving max force.