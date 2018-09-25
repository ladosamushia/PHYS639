import numpy as np 
import matplotlib.pyplot as plt

#Problem 1: Pendulum
# helped by Cheyne and Philip

L = 5 # pendulum length
g = 9.81 # gravitational acceleration
def f(omega, theta, time, q, F, alpha):
    return (-g/L)*np.sin(theta) -q*omega + F*np.sin(alpha*time)
def pendulum(theta0, v_0, q, F, alpha ): 
#Time Conditions
    tini = 0.0  
    tfin = 10.0
    stepsize = 10000
    dt = (tfin - tini)/stepsize
#Arrays
    time = np.zeros( stepsize + 1 )
    alpha = np.zeros( stepsize + 1 )
    omega = np.zeros ( stepsize + 1 )
    theta = np.zeros ( stepsize + 1 )
#Initial Conditions	
    omega0 = v_0/L
    theta0 = np.deg2rad(theta0) 
    omega[0] = omega0 
    theta[0] = theta0 
    time[0] = tini 
#Function Loop
    for i in range ( 1 , stepsize + 1 ):
        alpha[ i ] = f(omega[ i - 1 ], theta[ i - 1 ], time[ i -1 ], q, F, alpha)
        omega[ i ] = omega[ i - 1 ] + alpha[ i ]*dt
        theta[ i ] = theta[ i- 1 ] + omega[ i ]*dt
        if theta[ i ] > np.pi: 
            theta[ i ] -= 2*np.pi
        if theta[ i ] < -np.pi:
            theta[ i ] += 2*np.pi
        time [ i ] = time[ i - 1 ] + dt
    return [ time, theta ]
time, theta1 = pendulum(10,0,0,0,0)
time, theta2 = pendulum(10,0,0.5,0,0) 
time, theta3 = pendulum(10,0,0.5,3,4) 
time, theta4 = pendulum(10,0,0.5,3,8) 
theta_start = np.deg2rad(10)
theta_a = theta_start*np.cos(np.sqrt(g/L)*time)# Sm. Angle Approx.
plt.figure(1)
plt.plot( time, np.transpose([theta_a, theta1, theta2, theta3, theta4]) )
plt.xlabel( " time (in s) " )
plt.ylabel( " angle (in rad) " )
plt.title ( " angle v time " ) 
plt.legend()

#The following part heavily depended on Phillip's help, and honestly I'm still a little unclear on the exact details. Still working through it with him

alpha_varl = []
theta0 = []
freq = []
angle = []
smallanglefreq =[]
j = 0
theta_var = 1
theta_max = 90
ddt = 0.001
def x(theta, omega): # Undamped/Unforced ODE
    return (-g/L)*np.sin(theta)
#Function Loop
	while theta_var < theta_max:
		k = np.deg2rad(theta_var)
		period = []
		t = 0
		omega = 0
		if len(period)<2:
			while len(period)<2:
				alpha_var = x(k, omega)
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
			freq.append(freq)
			smallanglefreq.append(np.sqrt(g/L))
		thetal.append(theta_var)
		theta_var += 1
plt.figure(2)
plt.plot( thetal, freq, label = "ODE" )
plt.plot( thetal, smallanglefreq, label = "Small Angle" )
plt.xlabel( " Initial Angle (Degrees)" )
plt.ylabel( " Frequency (Hz)" )
plt.legend()