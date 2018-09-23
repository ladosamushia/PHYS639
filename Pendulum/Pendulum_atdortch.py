# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:24:30 2018

@author: Aus
"""

import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt

dt = 1
itheta = math.pi/6
length = 2.0
omega = 9.8/length
period = 2*math.pi/omega


def displacement (itheta,omega,dt):
    
    theta = itheta*math.cos(omega*dt)
    
    return([theta])
    
theta = itheta


while theta>=0:
    
    [theta] = displacement(theta,omega,dt)
    plt.plot(theta,dt)
    
    