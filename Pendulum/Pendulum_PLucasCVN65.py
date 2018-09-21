"""
Pendulum Motion: Created on 9/18/18 By: Philip Lucas
-Some function help by Cheyne Weis on 9/20/18
-Some in-class help by Dr. Lado Samushia on more functions  on 9/20/18
-Assisted  by Dylan Parker on how to use list for Frequency versus angle on 9/21/18
"""
import numpy as np 
import matplotlib.pyplot as plt
L = 5 # length of pendulum in mKs
g = 9.81 # Gravitational acceleration near earths surface
def f(omega, theta, time, q, Fext, OMEGA):# defining a function for Eulers Method
    return (-g/L)*np.sin(theta) -q*omega + Fext*np.sin(OMEGA*time)
def pendulum(theta_0, v_0, q, Fext, OMEGA ): 
    t_0 = 0.0  # line 14 - 17 creating a dt and a time window
    t_f = 10.0
    stepsize = 10000
    dt = (t_f - t_0)/stepsize
    omega_0 = v_0/L # allows me to give the pendulum a "Kick"
    theta_0 = np.deg2rad(theta_0) # allows degree inputs to auto convert to radians
    time = np.zeros( stepsize + 1 )
    alpha = np.zeros( stepsize + 1 )
    omega = np.zeros ( stepsize + 1 )
    theta = np.zeros ( stepsize + 1 ) 
    omega[0] = omega_0 #intial condition angular velocity
    theta[0] = theta_0 #intial condition angle
    time[0] = t_0 #intial condition time
    for i in range ( 1 , stepsize + 1 ):# for loop to use eulers method
        alpha[ i ] = f(omega[ i - 1 ], theta[ i - 1 ], time[ i -1 ], q, Fext, OMEGA)
        omega[ i ] = omega[ i - 1 ] + alpha[ i ]*dt
        theta[ i ] = theta[ i- 1 ] + omega[ i ]*dt
        if theta[ i ] > np.pi: # line 31-34 keep theta between pi and -pi 
            theta[ i ] -= 2*np.pi
        if theta[ i ] < -np.pi:
            theta[ i ] += 2*np.pi
        time [ i ] = time[ i - 1 ] + dt
    return [ time, theta ]
time, theta1 = pendulum(10,0,0,0,0)#inputs pendulum(theta_0, v_0, q, Fext, OMEGA )
time, theta2 = pendulum(10,0,0.5,0,0) 
time, theta3 = pendulum(10,0,0.5,3,4) 
time, theta4 = pendulum(10,0,0.5,3,8) 
theta_start = np.deg2rad(10)#small angle approximation initial angle
theta_a = theta_start*np.cos(np.sqrt(g/L)*time)# small angle approximation 
plt.figure(1)
plt.plot( time, np.transpose([theta_a, theta1, theta2, theta3, theta4]) )
plt.xlabel( " Time (s) " )
plt.ylabel( " Angle (rad) " )
plt.title ( " Angle versus Time " ) 
plt.legend()
#Note: I started fresh here. I couldn't get it to work within the above function
#creating lists and variables
alpha_varl = []
thetal = []
frequency = []
angle = []
smallanglefreq =[]
j = 0
theta_var = 1
theta_max = 90
ddt = 0.001
def z(theta, omega): # function for undamped and unforced ODE motion
    return (-g/L)*np.sin(theta)
while theta_var < theta_max: # While loop to run through angles
    k = np.deg2rad(theta_var)
    period = []
    t = 0
    omega = 0
    if len(period)<2: # allows me to only use two sequential times
        while len(period)<2:
            alpha_var = z(k, omega)
            alpha_varl.append(alpha_var)
            omega += alpha_var*ddt
            k += omega*ddt
            angle.append(k)
            if angle[ j - 1 ] > 0.0 and angle[ j ] < 0.0:
                period.append(t)
            j += 1 
            t += ddt
        periodtotal = period[1] - period[0]
        freq = 2*np.pi/periodtotal
        frequency.append(freq)
        smallanglefreq.append(np.sqrt(g/L))
    thetal.append(theta_var)
    theta_var += 1
plt.figure(2)
plt.plot( thetal, frequency, label = "ODE" )
plt.plot( thetal, smallanglefreq, label = "Small Angle" )
plt.xlabel( " Start angle (Degrees)" )
plt.ylabel( " Frequency (Hz)" )
plt.legend()
