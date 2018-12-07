# -*- coding: utf-8 -*-
"""
Created on Thu Dec 06 22:47:31 2018

@author: Jared
"""


# Disclaimer: I barely had time to write this code at all, so most of it comes from Spencer and Zane's code


import numpy as np
import matplotlib.pyplot as plt

# Load the data. Make sure the address is correct
data = np.loadtxt("\Users\Jared\Downloads\DataAnalysis.txt")

number = 100
Z = np.array([])
D = np.array([])
Sig = np.array([])
length = len(data)
Am = np.linspace(0,1,number)
Em = np.linspace(0,10,number)

# Takes the data from the file and inserts into columns
for i in range(length):
    Z = np.append(Z, data[i][0])
    D = np.append(D, data[i][1])
    Sig = np.append(Sig, data[i][2])

# Define global variables first, just for cleanliness
def Dth(d,z):
    Dth = 1+d*np.exp(-(Z-z)**2)
    return Dth

def Kai2(D, Dth, Sig):
    x2 = np.sum((D-Dth)**2/Sig**2)
    return x2

def Hessian(x,y,arr,i,j):
    # There seems to be a size error on line 39, and I could not seem to fix it in time for submission. FeelsBadMan
    d2x = arr[i-1][j] + arr[i+1][j] - 2*arr[i][j]/(x[i+1]-x[i])
    d2y = arr[i][j-1] + arr[i][j+1] - 2*arr[i][j]/(y[j+1]-y[j])
    dxy = (arr[i+1][j+1] + arr[i-1][j-1] - arr[i+1][j-1] - arr[i-1][j-1])/(4*(x[i]-x[i+1])*(y[j]-y[j+1]))
    H = np.zeros((2,2))
    H[0][0] = -.5*d2x
    H[1][1] = -.5*d2y
    H[0][1] = -.5*dxy
    H[1][0] = -.5*dxy
    return H

Kai2array = np.zeros((number,number))
Kai2min = 100000
a = 0
b = 0
xminimum = 0
yminimum = 0

for i in Am:
    b = 0
    for j in Em:
        Kai2array[b][a] = Kai2(Dth(i,j),D,Sig)
        if Kai2array[b][a] <= Kai2min:
            xminimum = a
            yminimum = b
            Kai2Min = Kai2array[b][a]
        b += 1
    a += 1

Amin = Am[yminimum]
Emin = Em[xminimum]

plt.figure(0)
plt.errorbar(Z,D,Sig,fmt='.')
plt.plot(Z,Dth(Amin,Emin))
plt.show()

H = Hessian(Em,Am,Kai2array,xminimum,yminimum)
C = np.linalg.inv(H)
sigmas = np.sqrt(C.diagonal())
print('Hessian Error:', sigmas)

    