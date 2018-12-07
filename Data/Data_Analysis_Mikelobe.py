# -*- coding: utf-8 -*-
"""


@author: mikelobe
"""

import numpy as np
import matplotlib.pyplot as plt


Data = np.loadtxt("HW9_DataAnalysis.txt") #downloads the text file with all the data
n=19
size=100
E=np.array([])
N=np.array([])
sig=np.array([])
length=len(Data)
for i in range(length):
    E=np.append(E,Data[i][0])
    N=np.append(N,Data[i][1])
    sig=np.append(sig,Data[i][2])
def Nth(A,E0):
    B=1
    return B+A*np.exp(-(E-E0)**2)
def Xsquared(N,Nth,sig):
    X2=np.sum((N-Nth)**2/sig**2)
    return X2
Xsquared_array=np.zeros((size,size))
Xsquared_min=100000
b=0
a=0
min_x=0
min_y=0
Em=np.linspace(0,10,size)
Am=np.linspace(0,1,size)
for i in Am:
    b=0
    for j in Em:
        Xsquared_array[b][a]=Xsquared(Nth(i,j),N,sig)
        if Xsquared_array[b][a]<=Xsquared_min:
            min_x=b
            min_y=a
            Xsquared_min=Xsquared_array[b][a]
        b+=1
    a+=1
min_E=Em[min_x]
min_A=Am[min_y]

plt.figure(1)
plt.errorbar(E,N,sig,fmt=".")
plt.plot(E,Nth(min_A,min_E))

def Xsquared2(N,Nth,sig):
    return -Xsquared(N,Nth,sig)/2
def hessian(x,y,arr,i,j):
    dxx = arr[i-1][j]+arr[i+1][j]-2*arr[i][j]/(x[i+1]-x[i])
    dyy = arr[i][j-1]+arr[i][j-1]-2*arr[i][j]/(y[j+1]-y[j])
    dxy = (arr[i+1][j+1]+arr[i-1][j-1]-arr[i+1][j-1]-arr[i-1][j-1])/4*(x[i]-x[i+1])*(y[j]-y[j+1])
    H = np.zeros((2,2))
    H[0][0]=-.5*dxx
    H[1][1]=-.5*dyy
    H[0][1]=-.5*dxy
    H[1][0]=-.5*dxy
    return H
Hessian=hessian(Em,Am,Xsquared_array,min_x,min_y)
C=np.linalg.inv(Hessian)
Sig=np.sqrt(C.diagonal())
print('Hessian Error:',Sig)

