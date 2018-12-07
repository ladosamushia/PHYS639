# -*- coding: utf-8 -*-
"""
Data Analysis for PHYS 639 @ Kansas State
Coded in Python 2.7
Created on Thu Nov 29 through Thu Dec 6 by Philip Lucas
Part 1 was built and modified from inclass discussion with Dr. Lado Samushia 
Part 2 was assisted by Parker Stoops
"""
###################################################################################
#Question number 1 best fit
print "Question 1 and 2:"
import numpy as np
import matplotlib.pyplot as plt
# change Data .txt location to work for you.
Data = np.loadtxt("DataAnalysis.txt")
E = Data[:,0]
N = Data[:,1]
SN = Data[:,2]
step = 100
E0 =  np.linspace(0,20,step)
Xsq = np.zeros((step,step))
# loops will run through A and E0 values to find Xsq, and the lowest is the best fit for
# for Amin and E0min
for i in range (step):
    A = np.linspace(0, 1, 100)
    for j in range (step): 
        Nth = 1 + A[j]*np.exp(-(E-E0[i])**2)
        Xsq[i][j] = np.sum((Nth-N)**2/SN**2)       
print "Minimum Xsq =" , np.round(np.min(Xsq), 3)
imin, jmin = np.where(Xsq == np.min(Xsq))
E0min = E0[imin[0]]
Amin = A[jmin[0]]
g = Amin
M = E0min
KKSQ = np.min(Xsq)
#########################################################################################
#Question number 2 Error Bars  Ultilized help from Parker Stoops
def Hmat(Xsq,A,E0,jmin,imin):
    #Partial second derivativres with respect to a, e and ae
    dada=(Xsq[imin,jmin+1]+Xsq[imin,jmin-1]-2*Xsq[imin,jmin])/((A[jmin+1]-A[jmin])**2)
    dede=(Xsq[imin+1,jmin]+Xsq[imin-1,jmin]-2*Xsq[imin,jmin])/((E0[imin+1]-E0[imin])**2)
    dade=(Xsq[imin-1,jmin-1]+Xsq[imin+1,jmin+1]-Xsq[imin-1,jmin+1]-Xsq[imin+1,jmin-1])/(4*(A[jmin+1]-A[jmin])*(E0[imin+1]-E0[imin]))
    # Assigning matrix positions
    Hess=np.zeros((2,2))
    Hess[0][0]=.5*dada
    Hess[0][1]=.5*dade
    Hess[1][0]=.5*dade
    Hess[1][1]=.5*dede
    return Hess
#Determining and inverting Hessian Matrix
Hess= Hmat(Xsq,A,E0,jmin,imin)
C=np.linalg.inv(Hess)
sigma=np.sqrt(np.diagonal(C))
print "Rounded Values"
print( 'E0 = ', np.round(E0min, 2), "+/-", np.round(sigma[0], 2))
print( 'A =', np.round(Amin, 1), "+/-" , np.round(sigma[0], 1))
print "Raw Values"
print('A is', Amin,'E0 is',E0min)
print('sigmaE0 is', sigma[0],'sigmaA is',sigma[1])
Esmooth = np.linspace(0,20,10000)
# following two plots are for clarity. It is easier to see and less cluttered with two plots. 
plt.figure(1)
#Plot of the scatter plot with the model
plt.plot(Esmooth,1 + Amin*np.exp(-(Esmooth-E0min)**2), "black")
plt.title("Data and Best fit Model")
plt.xlabel("Energy")
plt.ylabel("N value")
plt.figure(2)
# Plots a hilighted bar for a model fit. Taking into account my possible error. 
plt.errorbar(Esmooth,1 + Amin*np.exp(-(Esmooth-E0min)**2), sigma[0], sigma[1], "yellow")
plt.plot(Esmooth,1 + Amin*np.exp(-(Esmooth-E0min)**2), "black")
plt.title("Data and Best fit Model with Uncertantity Band")
plt.xlabel("Energy")
plt.ylabel("N value")
#################################################################################################
## Question number 3 I spent too long working on part 2 and didn't get to finish this code. I was going 
## make a random set of data and cycle through and log all my Xsq values. It currently does not work
## I don't think it's working quite right. I am getting a goodness of fit of 0. 
Erand = np.random.normal(0, 19)
Ntruerand = 1 + g*np.exp(-(E-M)**2)
Afake = np.zeros(1000)
Kai = []
for o in range(1000):
    noise1 = np.random.normal(0, SN)
    Nmeasured = Ntruerand + noise1
    for c in range (step):
        A1 = np.linspace(0, 1, 100)
        for b in range (step):  
            Nth = 1 + A1[b]*np.exp(-(E-E0[c])**2)
            Xsq[c][b] = np.sum((Nth-Nmeasured)**2/SN**2)
    cmin, bmin = np.where(Xsq == np.min(Xsq))
    Kai = np.append(cmin, bmin)   
goodnessoffit = np.sum(Kai <= KKSQ)/np.sum(Kai)
print "Goodness of Fit =", goodnessoffit
#################################################################################################
## Question number 4
likelyhood = (np.min(Xsq)**2/2)
print "Likelyhood =",(np.round(likelyhood , 3))
print " Question 4:"
Ntrue = np.ones(np.size(N))
Afake = np.zeros(1000)
for k in range(1000):
    noise = np.random.normal(0, SN)
    Nmeasured = Ntrue + noise
    for i in range (step):
        A = np.linspace(0, 1, 100)
        for j in range (step):  
            Nth = 1 + A[j]*np.exp(-(E-E0[i])**2)
            Xsq[i][j] = np.sum((Nth-Nmeasured)**2/SN**2)
    imin, jmin = np.where(Xsq == np.min(Xsq))
    E0min = E0[imin[0]]
    Amin = A[jmin[0]] 
    Afake[k] = Amin
Percentnoise = np.sum(Afake >= g)/np.sum(Afake)
print "Approximate chance of A being noise =", np.round(Percentnoise*100, 3),"%"
plt.figure(1)
plt.errorbar(E, N, SN, fmt = 'o')
plt.figure(2)
plt.errorbar(E, N, SN, fmt = 'o')
plt.figure(3)
plt.hist(Afake)
plt.title("Histagram of random A values ")
plt.xlabel("Amin for Random Data Sets")
plt.ylabel("Number of Occurances")