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


##dipole and capacitor
def relax(A, indlist, n_steps, C):
    B = np.zeros((n_steps,n_steps))
    for x in indlist:
        i = x[0]
        j = x[1]
        B[i][j] = (A[i+1][j] + A[i-1][j] + A[i][j+1] + A[i][j-1] + C[i][j])/4
    return B

global n_steps
n_steps = 100

A = np.zeros((n_steps,n_steps))
C = np.zeros((n_steps,n_steps))
F = np.zeros((n_steps,n_steps))
x_min, x_max = 0.0,1.0
global dx
indlist = []
dx = (x_max-x_min)/n_steps
V1 = 100.0
V0 = 0.0
V = 50.0
um = (n_steps/2) + (n_steps/20)
lm = (n_steps/2) - (n_steps/20)
cum = (n_steps/2) + (n_steps/20)
clm = (n_steps/2) - (n_steps/20)

cshift = (n_steps/4)

shift = (n_steps/8)
for i in range(n_steps):
    for j in range(n_steps):
        if(i == 0 or j == 0 or i == n_steps-1 or j == n_steps-1):
            A[i][j] = 0
        elif(i <= um + shift and j <= um and i >= lm + shift and j >= lm):
            A[i][j] = -1*V1
        elif(i <= um - shift and j <= um and i >= lm - shift and j >= lm):
            A[i][j] = V1
        else:
            if(j <= cum - cshift and i <= cum + shift/3 and j >= clm - cshift and i >= clm + shift/3):
                C[i][j] = V1/10
            if(j <= cum - cshift and i <= cum - shift/3 and j >= clm - cshift and i >= clm - shift/3):
                C[i][j] = (-1)*V1/10
            F[i][j] = 0
            indlist.append((i,j))
l =0
AF = A + F
for k in range(4000):
    F = relax(AF, indlist, n_steps, C)
    AF = A + F

plt.imshow(AF)
plt.show()
