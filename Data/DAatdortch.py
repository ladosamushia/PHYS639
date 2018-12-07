# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:18:19 2018

@author: Aus
"""

#Data Analysis
#Obj: plotting best fit lines with given data points in order to find
#energy distribution and peak values.

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('DataAnalysis.txt')
nsteps = 100
A=[]
E=data[:,0]
N=data[:,1]
SN=data[:,2]

plt.errorbar(E,N,SN, fmt='o')
plt.xlabel('energy')
plt.ylabel('Number of Photons')

N=[]
nerror=[]
E0 = 0
Amax = 10
Evals = np.linspace(0,E0,nsteps)
Avals = np.linspace(0,Amax,num=nsteps)
for i in range(nsteps):
    Eval = Evals[i]
    for j in range(nsteps):
        Nthvals = []
    for e in E:
        Nthvals.append(1 + Avals*np.exp((-1)*(e-Evals)*(e-Evals)))
        chi2 = 0 
    for k in range (len(N)):
        chi2 += (N[k]-Nthvals[k])**2)/(nerror[k]**2)
        chi2vals[i][j] = chi2
        likelyVals[i][j] = np.exp((-0.5)*chi2)
        ApproxlikelyVals[i][j] = 0.5*chi2
    if chi2 < chi2min:
        chi2min = chi2
        E0approx = Evals
        Aapprox = Avals
        
        
x = np.linspace(min(E),max(E),num=1001)
def best_fit(X):
    return 1 + Aapprox*np.exp((-1)*(X-E0approx)*(X-E0approx))
plt.figure(1)
plt.plot(x,best_fit(x),'g-',label='Best Fit')

plt.figure(2)
plt.title('chi2')
plt.figure(3)
plt.title('likelyvals')


def d2Aapprox(A,E0):
    Aray = Avals.toarray[]
    x0dx=aray.index(A)
    E0ray = Evals.toarray[]
    y0dx=E0ray.index(E0)
    return(ApproxlikelyVals[y0dx][x0dx+1] + ApproxlikelyVals[y0dx][x0dx-1] - 2*ApproxlikelyVals[y0dx][x0dx])/((A_list[x0dx+1]-A_list[x0dx])**2)

def d2E0Approx(A,E0):
    Aray = Avals.toarray[]
    x0dx=aray.index(A)
    E0ray = Evals.toarray[]
    y0dx=E0ray.index(E0)
    return(ApproxlikelyVals[y0dx][x0dx+1] + ApproxlikelyVals[y0dx][x0dx-1] - 2*ApproxlikelyVals[y0dx][x0dx])/((A_list[x0dx+1]-A_list[x0dx])**2)

def d2AE0Approx(A,E0):
    Aray = Avals.toarray[]
    x0dx=aray.index(A)
    E0ray = Evals.toarray[]
    y0dx=E0ray.index(E0)
    return(ApproxlikelyVals[y0dx][x0dx+1] + ApproxlikelyVals[y0dx][x0dx-1] - 2*ApproxlikelyVals[y0dx][x0dx])/((A_list[x0dx+1]-A_list[x0dx])**2)
    
Hessian = np.zeros()
Hessian[0][0]=d2Aapprox(Aapprox,E0approx)
Hessian[0][1]=d2AE0Approx(Aapprox,E0approx)
Hessian[1][0]=d2AE0Approx(Aapprox,E0approx)
Hessian[1][1]=d2E0Approx(Aapprox,E0approx)

Hessianinv=np.linalg.inv(Hessian)

Aerror= np.sqrt(Hessianinv[0][0])
E0error=np.sqrt(Hessianinv[1][1])

plt.figure(1)
plt.errorbar(E0approx,1+Aapprox,xerror=E0error,yerror=Aerror,fmt='go',label='(E0approx,1+Approx)')
plt.ylim(0,2)
plt.legend()
plt.grid()

#having trouble defining chi2 in line 20. 
