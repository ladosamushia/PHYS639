#James Corona
#Pendulum
#PHYS 639

import numpy as np
import matplotlib.pyplot as plt

#This program is only valid so long as -pi <= theta <= pi. I also fixed the
#starting velocity to 0.

##############################################################################

#Problem: Simple Pendulum

def simple(theta, length):
    
    vel = 0
    grav = 9.81
    tfin = 20
    dt = 0.001
    
    omega = np.sqrt(grav / length)
    time = np.linspace(0, tfin, int(tfin / dt))
    thetas = []
    smallthetas = []
    
    for t in time:
        smallthetas.append(theta * np.cos(omega * t))
    
    for t in time:
        thetas.append(theta)
        theta += vel * dt
        vel += -(grav / length) * np.sin(theta) * dt

    plt.figure()
    plt.xlabel('Time')
    plt.ylabel('Angle')
    plt.title('Simple Pendulum')
    plt.plot(time, thetas, 'r', label = 'Actual')
    plt.plot(time, smallthetas, 'y', label = 'Small Angle')
    plt.legend(loc = 'upper left')

def simplefreq(length):
    
    amplitudes = np.linspace(0.05 * np.pi, 0.95 * np.pi, 100)
    freqs = []
    
    for theta in amplitudes:
    
        vel = 0
        grav = 9.81
        tfin = 20
        dt = 0.001
        
        root = 0
        thetaprev = theta
        time = np.linspace(0, tfin, int(tfin / dt))
        thetas = []
    
        for t in time:
            
            thetas.append(theta)
            theta += vel * dt
            vel += -(grav / length) * np.sin(theta) * dt
            
            if theta < 0 and thetaprev > 0:
                freq = np.pi / (t - root)
                root = t
            
            thetaprev = theta
                
        freqs.append(freq)
    
    plt.figure()
    plt.xlabel('Amplitude')
    plt.ylabel('Frequency')
    plt.title('Simple Pendulum')
    plt.plot(amplitudes, freqs, 'r')


simple(np.pi / 4, 10)
simplefreq(10)

#simple(theta, length) plots angle vs time for some initial angle 'theta' and
#pendulum length 'length'. simplefreq(length) plots frequency vs amplitude
#for some pendulum length 'length'.

##############################################################################

#Problem: Damped Pendulum

def damped(theta, length, q):
    
    vel = 0
    grav = 9.81
    tfin = 20
    dt = 0.001
    
    time = np.linspace(0, tfin, int(tfin / dt))
    thetas = []
    
    for t in time:
        thetas.append(theta)
        theta += vel * dt
        vel += (-(grav / length) * np.sin(theta) - q * vel) * dt

    plt.figure()
    plt.xlabel('Time')
    plt.ylabel('Angle')
    plt.title('Damped Pendulum')
    plt.plot(time, thetas, 'g')
    
def dampedfreq(length, q):
    
    amplitudes = np.linspace(0.05 * np.pi, 0.95 * np.pi, 100)
    freqs = []
    
    for theta in amplitudes:
    
        vel = 0
        grav = 9.81
        tfin = 20
        dt = 0.001
        
        root = 0
        thetaprev = theta
        time = np.linspace(0, tfin, int(tfin / dt))
        thetas = []
    
        for t in time:
            
            thetas.append(theta)
            theta += vel * dt
            vel += (-(grav / length) * np.sin(theta) - q * vel) * dt
            
            if theta < 0 and thetaprev > 0:
                freq = np.pi / (t - root)
                root = t
            
            thetaprev = theta
                
        freqs.append(freq)
    
    plt.figure()
    plt.xlabel('Amplitude')
    plt.ylabel('Frequency')
    plt.title('Damped Pendulum')
    plt.plot(amplitudes, freqs, 'g')

damped(np.pi / 4, 10, 0.1)
dampedfreq(10, 0.1)

#damped(theta, length, q) plots angle vs time for some initial angle 'theta',
#pendulum length 'length', and damping coefficient 'q'. dampedfreq(length, q)
#plots frequency vs amplitude for some pendulum length 'length' and some
#damping coefficient 'q'. If the pendulum is overdamped, the frequency vs
#amplitude plot is not valid.

##############################################################################

#Problem: Damped Driven Pendulum

def dampeddriven(theta, length, q, accelmax, freqdrive):
    
    vel = 0
    grav = 9.81
    tfin = 20
    dt = 0.001
    
    time = np.linspace(0, tfin, int(tfin / dt))
    thetas = []
    
    for t in time:
        thetas.append(theta)
        theta += vel * dt
        vel += (-(grav / length) * np.sin(theta) - q * vel + accelmax * np.sin(freqdrive * t)) * dt

    plt.figure()
    plt.xlabel('Time')
    plt.ylabel('Angle')
    plt.title('Damped Driven Pendulum')
    plt.plot(time, thetas, 'b')
    
def dampeddrivenmax(theta0, length, q, accelmax):
    
    freqsdrive = np.linspace(0, 2, 100)
    maximums = []
    
    for freqdrive in freqsdrive:
        
        theta = theta0
        vel = 0
        grav = 9.81
        tfin = 50
        dt = 0.001
        
        maximum = theta
        time = np.linspace(0, tfin, int(tfin / dt))
        thetas = []
    
        for t in time:
            
            thetas.append(theta)
            theta += vel * dt
            vel += (-(grav / length) * np.sin(theta) - q * vel + accelmax * np.sin(freqdrive * t)) * dt
            
            if theta > maximum:
                maximum = theta
                
        maximums.append(maximum)
    
    plt.figure()
    plt.xlabel('Driving Frequency')
    plt.ylabel('Maximum Angle')
    plt.title('Damped Driven Pendulum')
    plt.plot(freqsdrive, maximums, 'b')

dampeddriven(np.pi / 4, 10, 0.1, 0.2, 0.6)
dampeddrivenmax(np.pi / 4, 10, 0.1, 0.2)

#dampeddriven(theta, length, q, accelmax, freqdrive) plots angle vs time in a
#similar fashion to the other two scenarios. dampeddrivenmax(theta0, length, q,
#accelmax) plots maximum angle vs frequency. There is a sharp peak on the
#graph, which corresponds to when the drive frequency is equal to the natural
#frequency of the pendulum.

##############################################################################