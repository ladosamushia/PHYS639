# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 12:02:49 2018

@author: Aus
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


 
# function that defines coupled differentials
def decay(N,t):
    alpha = 20
    beta = 0.25
    
    dadt = -alpha/t
    
    dbdt = -alpha/t - beta/t
    return([dadt,dbdt])

# initial value
N0 = 1000
t = np.linspace(1,1500)

Na = odeint(decay,N0,t)
Nb = odeint(decay,N0,t)

# plot
plt.y(t,Na,)
plt.y(t,Nb)
plt.xlabel('time')
plt.ylabel('N(t)')
plt.show()
