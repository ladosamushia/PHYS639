# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:09:16 2018

@author: phili
"""

"""
Created on Thu Aug 30 2018
Created by Philip Lucas
"""
import numpy as np 
import matplotlib.pyplot as plt
L = 5
g = 9.81
def f(omega, theta, time):
    q = 0.0 #damping constant
    Fext = 5 # force applied
    OMEGA = 10# np.sqrt(g/L)# driving frequency 
    return (-g/L)*np.sin(theta) -q*omega + Fext*np.sin(OMEGA*time)
#creating a dt and a time window 
t_0 = 0.0
t_f = 10.0
stepsize = 10000
dt = (t_f - t_0)/stepsize
v_0 = 1 # intitual velocity for any applied kick
omega_0 = v_0/L # allows me to give the pendulum a "Kick"
theta_0 = np.deg2rad(30) # start angle
#alloting Memory
time = np.zeros( stepsize + 1 )
alpha = np.zeros( stepsize + 1 )
omega = np.zeros ( stepsize + 1 )
theta = np.zeros ( stepsize + 1 ) 
omega[0] = omega_0
theta[0] = theta_0
time[0] = t_0
for i in range ( 1 , stepsize + 1 ):
    alpha[i] = f(omega[ i - 1 ], theta[ i - 1 ], time[ i -1 ])
    omega[i] = omega[ i - 1 ] + alpha[ i ]*dt
    theta[i] = theta[ i- 1 ] + omega[ i ]*dt
    time [i] = time[ i - 1 ] + dt
# small angle approximation 
theta_a = theta_0*np.cos(np.sqrt(g/L)*time)
#plots
plt.figure(1)
plt.plot( time, theta, label = "Differential Equation" )
plt.plot( time, theta_a, label = "Small Angle approximation")
plt.xlabel(" Time (s) " )
plt.ylabel(" Angle (rad) ")
plt.title ( "Angle versus Time" ) 
plt.legend()
plt.figure(2)

