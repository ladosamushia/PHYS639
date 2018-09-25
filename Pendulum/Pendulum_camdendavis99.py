# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 13:26:00 2018

@author: Camden
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Initial Values - always leave uncommented

# Initializes all initial values and constants
g = 9.8
L = 1.0
q = 0.5
dt = 0.0001
t = [0]
tf = 10

# Initializes arrays for each variable. Each only holds initial value at first
a0 = 1.0
aDot0 = 0.3
a = [a0]
aDot = [aDot0]

#------------------------------------------------------------------------------

# Problem 1: Simple Pendulum

# Initializes variables used to find period, as well as the current index
zeros = 0
periodFound = False
index = 0

while t[index] <= tf:
    # Keeps the angle between pi and -pi
    if a[index] > np.pi:
        a[index] -= 2 * np.pi
    elif a[index] < -np.pi:
        a[index] += 2 * np.pi
    
    # Calculates current angular acceleration
    aDot2 = (-g / L) * np.sin(a[index])

    # Generates new values for time and angle arrays        
    t.append(t[index] + dt)
    a.append(a[index] + aDot[index] * dt)
    aDot.append(aDot[index] + aDot2 * dt)
    index += 1
    
    # Finds period of function if not done already
    if not periodFound:
        if (a[index] > 0 and a[index - 1] < 0) or (a[index] < 0 and a[index - 1] > 0):
            if zeros == 0:
                t1 = t[index]
            elif zeros == 2:
                t2 = t[index]
                periodFound = True
            zeros += 1
    
# Graph 
plt.plot(t, a, 'ro')
plt.xlabel("t (s)")
plt.ylabel("a (degrees)")
plt.title("Angle of pendulum")

print("Period is {:.2f}s".format(t2 - t1))
print("Frequency is {:.2f}Hz".format(1/(t2 - t1)))

#------------------------------------------------------------------------------

# Problem 2: Damped Pendulum

#index = 0
#frequency = []
#frequencyTimes = []
#
#while t[index] <= tf:
#    # Keeps the angle between pi and -pi
#    if a[index] > np.pi:
#        a[index] -= 2 * np.pi
#    elif a[index] < -np.pi:
#        a[index] += 2 * np.pi
#
#    # Calculates current angular acceleration, accounting for dampening
#    aDot2 = (-g / L) * np.sin(a[index]) - q * aDot[index]
#
#    # Generates new values for time and angle arrays
#    t.append(t[index] + dt)
#    a.append(a[index] + aDot[index] * dt)
#    aDot.append(aDot[index] + aDot2 * dt)
#    index += 1
#    
#    # Finds period of function if not done already
#    if (a[index] > 0 and a[index - 1] < 0) or (a[index] < 0 and a[index - 1] > 0):
#        frequencyTimes.append(t[index])
#
## Calculates frequencies at known zeros
#for i in range(len(frequencyTimes) - 1):
#    frequency.append(1 / (2 * (frequencyTimes[i + 1] - frequencyTimes[i])))
#frequencyTimes.remove(frequencyTimes[len(frequencyTimes) - 1])
#
## Graph 
#plt.plot(frequencyTimes, frequency, 'g')
#plt.plot(t, a, 'ro')
#plt.xlabel("t (s)")
#plt.ylabel("a (degrees)")
#plt.title("Angle of pendulum (with dampening)")

#------------------------------------------------------------------------------

# Problem 3: Damped Driven Pendulum

#maxAmps = np.zeros(10)
#index = 0
#
## Finds maximum amplitude of pendulums with ten different driving forces
#for i in range(10):
#    maxAmp = -np.pi
#    f_max = 2.0
#    omega = 20.0 * i
#    f_ext = [f_max * np.sin(omega * t[0])]
#    
#    while t[index] <= tf:
#        # Keeps the angle between pi and -pi
#        if a[index] > np.pi:
#            a[index] -= 2 * np.pi
#        elif a[index] < -np.pi:
#            a[index] += 2 * np.pi
#    
#        # Calculates current angular acceleration, accounting for all factors now
#        aDot2 = (-g / L) * np.sin(a[index]) - q * aDot[index] + f_ext[index]
#
#        # Generates new values for time, angle, and force arrays
#        t.append(t[index] + dt)
#        a.append(a[index] + aDot[index] * dt)
#        aDot.append(aDot[index] + aDot2 * dt)
#        f_ext.append(f_max * np.sin(omega * t[index + 1]))
#        index += 1
#        
#        # Updates maximum amplitude if necessary
#        if a[index] > maxAmp:
#            maxAmp = a[index]
#    
#    # Resets initial values
#    index = 0
#    maxAmps[i] = maxAmp
#    a = [a0]
#    aDot = [aDot0]
#    t = [0]
#
#f_max = 2.0
#omega = math.sqrt(g / L)
#f_ext = [f_max * np.sin(omega * t[0])]
#
#frequency = []
#frequencyTimes = []
#
#while t[index] <= tf:
#    # Keeps the angle between pi and -pi
#    if a[index] > np.pi:
#        a[index] -= 2 * np.pi
#    elif a[index] < -np.pi:
#        a[index] += 2 * np.pi
#    
#    # Calculates current angular acceleration, accounting for all factors now
#    aDot2 = (-g / L) * np.sin(a[index]) - q * aDot[index] + f_ext[index]
#
#    # Generates new values for time, angle, and force arrays
#    t.append(t[index] + dt)
#    a.append(a[index] + aDot[index] * dt)
#    aDot.append(aDot[index] + aDot2 * dt)
#    f_ext.append(f_max * np.sin(omega * t[index + 1]))
#    index += 1
#    
#    # Finds period of function if not done already
#    if (a[index] > 0 and a[index - 1] < 0) or (a[index] < 0 and a[index - 1] > 0):
#        frequencyTimes.append(t[index])
#
## Calculates frequencies at known zeros
#for i in range(len(frequencyTimes) - 1):
#    frequency.append(1 / (2 * (frequencyTimes[i + 1] - frequencyTimes[i])))
#frequencyTimes.remove(frequencyTimes[len(frequencyTimes) - 1])
#    
## Graph 
#plt.figure(1)
#plt.plot(frequencyTimes, frequency, 'g')
#plt.plot(t, a, 'ro')
#plt.xlabel("t (s)")
#plt.ylabel("a (degrees)")
#plt.title("Angle of pendulum")
#
#plt.figure(2)
#plt.plot(np.linspace(0, 2, 10), maxAmps, 'go')
#plt.xlabel("F (N)")
#plt.ylabel("max amplitude, a (degrees)")
#plt.title("Max angle of pendulum")