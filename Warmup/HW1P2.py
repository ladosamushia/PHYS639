# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 13:49:08 2018

@author: Aus
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# function returns dN/dt
def model(N,t):
    a = 2
    b = 2
    dNdt = a*N - b*N**2
    return dNdt

# initial condition
N0 = 10

# time interval
t = np.linspace(0,20)

# solution to differential equation
N = odeint(model,N0,t)

# graph of results
plt.plot(t,N)
plt.xlabel('time')
plt.ylabel('N(t)')
plt.show()

