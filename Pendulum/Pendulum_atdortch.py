# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:24:30 2018

@author: Aus
"""

import math
import matplotlib.pyplot as plt
import numpy as np


"Intialize Variables"
t = np.linspace(0,math.pi)
itheta = math.pi/4
length = 2.0
omega = 9.8/length

"Defined function that calculates displacement"
def displacement (itheta,omega,t):
    
    theta = itheta*np.cos(omega*t)
    
    return([theta])
    
theta = itheta
    
[theta] = displacement(theta,omega,t)

"Plot graph"
plt.plot(t,theta)
plt.xlabel('Time')    
plt.ylabel('Theta')

"---------------------------------------------------------------------------"




import math
import matplotlib.pyplot as plt
import numpy as np


"Intialize Variables"
t = np.linspace(0,math.pi)
itheta = math.pi/4
length = 2.0
omega = 9.8/length
b=2

"Defined function that calculates displacement"
def displacement (itheta,omega,t):
    
    theta = itheta*np.exp((-b/2)*t)*np.cos(omega*t)
    
    return([theta])
    
theta = itheta
    
[theta] = displacement(theta,omega,t)

"Plot graph"
plt.plot(t,theta,'g')
plt.xlabel('Time')    
plt.ylabel('Theta')


"------------------------------------------------------------------------"

import math
import matplotlib.pyplot as plt
import numpy as np


"Intialize Variables"
t = np.linspace(0,np.pi)
itheta = np.pi/4
length = 2.0
omega = 9.8/length
k=.01
b=2
z = np.sqrt(b**2-(omega-k/omega)**2)



"Defined function that calculates displacement"
def displacement (itheta,omega,t):
    
    theta = (itheta/z)*np.cos(omega*t)
    
    return([theta])
    
theta = itheta
    
[theta] = displacement(theta,omega,t)

"Plot graph"
plt.plot(t,theta,'r')
plt.xlabel('Time')    
plt.ylabel('Theta')


