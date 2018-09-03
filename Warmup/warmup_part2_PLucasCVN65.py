# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:44:36 2018

Created by Philip Lucas

Warm up Exercise Number 2 "Population models"
"""

import numpy as np 
import matplotlib.pyplot as plt

N0 = 100.0 #This is the intial population
alpha = 0.9 # this is a growth factor for the population 
beta = 0.006 # This is the decay factor for the population

T0 = 0.0 # Intial time for inital population
Tf = 10.0 # Final time for plotting purposes
NoSteps = 1000 #This breaks the function into fractional steps in approximation
t = np.linspace( T0, Tf, NoSteps +1)
N = np.zeros( NoSteps + 1)
N[0] = alpha*N0 - beta*(N0**2)
#line 21 and 22 build the equation to plot
dt = (Tf-T0)/NoSteps #This approximated dt as a Change in T 
for i in range (1 , NoSteps + 1):
    dN = alpha*N[ i - 1 ] - beta*( N[ i - 1 ]**2 )
    N[i] = N[i - 1] + dN*dt
#line 24-27 run through the loop of building the function
plt.plot( t, N, 'go')
plt.xlabel ("Time")
plt.ylabel ("Population")
#Line 31-33 plots the function N from T0 to Tf and lables the axii
"""
This solution makes sense given we expect population N0 to grow with
time till a certain time where beta*N**2 reaches equalibrium with alpha*N
Alpha and Beta must be picked such that one or the other does not immediately
dominate the function otherwise python sees -inf or inf. Also Alpha and Beta
must both be >0 

Using Wolfram
N(t) = (Alpha/Beta)/((1+(alpha-beta*N0)/(beta*N0))*np.exp(-alpha*t))
"""

