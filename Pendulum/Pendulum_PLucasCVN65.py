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

def f(omega, theta, time, q, Fext, OMEGA):
    return (-g/L)*np.sin(theta) -q*omega + Fext*np.sin(OMEGA*time)

def pendulum(theta_0, v_0, q, Fext, OMEGA):
    #creating a dt and a time window 
    t_0 = 0.0
    t_f = 10.0
    stepsize = 10000
    dt = (t_f - t_0)/stepsize
    omega_0 = v_0/L # allows me to give the pendulum a "Kick"
    theta_0 = np.deg2rad(theta_0)
    #alloting Memory
    time = np.zeros( stepsize + 1 )
    alpha = np.zeros( stepsize + 1 )
    omega = np.zeros ( stepsize + 1 )
    theta = np.zeros ( stepsize + 1 ) 
    omega[0] = omega_0
    theta[0] = theta_0
    time[0] = t_0
    for i in range ( 1 , stepsize + 1 ):
        alpha[i] = f(omega[ i - 1 ], theta[ i - 1 ], time[ i -1 ], q, Fext, OMEGA)
        omega[i] = omega[ i - 1 ] + alpha[ i ]*dt
        theta[i] = theta[ i- 1 ] + omega[ i ]*dt
        if theta[i] > np.pi:
            theta[i] -= 2*np.pi
        if theta[i] < -np.pi:
            theta[i] += 2*np.pi
        time [i] = time[ i - 1 ] + dt
    return [time, theta]
    
time, theta1 = pendulum(10,0,0,0,0)
time, theta2 = pendulum(10,0,0.5,0,0)
time, theta3 = pendulum(10,0,0.5,3,4)
time, theta4 = pendulum(10,0,0.5,3,8)
# small angle approximation 
theta_a = theta_0*np.cos(np.sqrt(g/L)*time)
#plots
plt.figure(1)
plt.plot( time, np.transpose([theta1, theta2, theta3, theta4]), label = "Differential Equation" )
plt.xlabel(" Time (s) " )
plt.ylabel(" Angle (rad) ")
plt.title ( "Angle versus Time" ) 
plt.legend()
plt.figure(2)
