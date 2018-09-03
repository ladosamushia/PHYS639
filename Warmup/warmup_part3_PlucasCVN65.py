# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:21:11 2018

Created by Philip Lucas 

Most resources from following along in class modified for two differential
equations
"""

import numpy as np
import matplotlib.pyplot as plt
N0_A = 10
N0_B = 15
tau_A = 703.8
tau_B = 100.2
T0 = 0
Tf = 10*tau_A
NoSteps = 10000
t = np.linspace( T0 , Tf, NoSteps +1 )
N_A = np.zeros( NoSteps +1 )
N_B = np.zeros( NoSteps +1 )
N_A[0] = N0_A
N_B[0] = N0_B
dt = (Tf -T0)/NoSteps
for i in range ( 1 , NoSteps ):
    dN_A =  N_A[i-1]/tau_A
    dN_B = N_A[i-1] - N_B[ i-1 ] 
    N_A[i] = - N_A[ i - 1 ] + dN_A*dt
    N_B[i] = - N_B [ i- 1 ] + dN_B*dt 
plt.plot(t, N_A , N_B , 'go' )
plt.xlabel ( "time in millions of years" )
plt.ylabel ( "Population in mols" )

"""
I could not make this code work but I am still working on it. This is what 
I have so far. I thought I could make two decay approximations like we did
for part one in class. I thought then I could combine them. I guess I don't
fully understand how to do this in python. I also might have a misconception
with coupled differential equations. 
"""