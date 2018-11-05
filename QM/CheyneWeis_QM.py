from Tkinter import *
from math import *
from sys import argv
from matplotlib import pyplot as plt
import time
import numpy.random as random

import numpy as np
pi = 3.14159265359
global gui
# initiliaze tk object

#CHANGE THIS NUMBER TO CHANGE POTENTIAL
pn = 4
#1=infinite square well
#2=square well with wall in midle
#3=quadratic
#4=tringular well

global n_steps
n_steps = 4000

x_min, x_max = 0.0,1.0
global dx
dx = (x_max-x_min)/n_steps
def v1(x):
	if(x > x_min and x < x_max):
		return 0
	else:
		return 100
def v2(x):
	if(x <= 0.55 and x >= 0.45):
		return 1000
	elif(x > x_min and x < x_max):
		return 0
	else:
		return 100

def v3(x):
	return 10000*((x-0.5)**2)
def v4(x):
	return 1000*x
def solve(x_min, x_max, pn):
    x = np.linspace(x_min, x_max, n_steps)
    A = np.zeros((n_steps,n_steps))
    if(pn == 1): 
    	v = v1(dx)
    elif(pn == 2): 
    	v = v2(dx)
    elif(pn == 3): 
    	v = v3(dx)
    elif(pn == 4): 
    	v = v4(dx)
    A[0][0] = (2/(dx**2)) + v
    A[0][1] = (-1/(dx**2))
    for i in range(1, n_steps - 3):
	    if(pn == 1): 
	    	v = v1((i+1)*dx)
	    elif(pn == 2): 
	    	v = v2((i+1)*dx)
	    elif(pn == 3): 
	    	v = v3((i+1)*dx)
	    elif(pn == 4): 
    		v = v4((i+1)*dx)
	    A[i][i-1] = (-1/(dx**2))
	    A[i][i] = (2/(dx**2)) + v
	    A[i][i+1] = (-1/(dx**2))
    if(pn == 1): 
    	v = v1(x_max - dx)
    elif(pn == 2): 
    	v = v2(x_max - dx)
    elif(pn == 3): 
    	v = v3(x_max - dx)
    elif(pn == 4): 
    	v = v4(x_max - dx)
    A[n_steps - 2][n_steps - 2] = (2/(dx**2)) + v1(x_max - dx)
    A[n_steps - 2][n_steps - 3] = (-1/(dx**2))
    energy, psi_t = np.linalg.eigh(A)
    psi = np.transpose(psi_t)
    return energy, psi

n_plot = 7
x=[]
for i in range(0,n_steps):
	x.append(i*dx)
# infinite square well cv
e, p = solve(x_min, x_max, pn)
print(len(x), len(p[3]))
for i in range(2, n_plot):
    plt.plot(x, p[i])
    print(e[i])
plt.legend()

plt.xlabel('x')
plt.ylabel('Psi')
plt.show()