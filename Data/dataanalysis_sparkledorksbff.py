# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:04:20 2018

@author: jessi
"""

#Jessica Pietrowski
#Problem 1:  Best-fit values

import numpy as np
import matplotlib.pyplot as plt

C = np.loadtxt("C:\Users\jessi\OneDrive\Documents\Documents\College Assignments\Computations in Physics\Data Analysis\erroranalysis.txt") #Load the text file for our code
E = C[:,0] #Define the values of E
N = C[:,1] #Define the values of N
delta = C[:,2] #Define the error in our measurement

#Now to plot the data
plt.figure(1)
plt.errorbar(E,N,delta,fmt='o')
plt.xlabel('Energy')
plt.ylabel('Number of Photons')

chi2 = np.zeros((100,100)) #Define an empty grid for chi2 values

E0 = np.linspace(0,20,100) #We want our E0 values to range from 0 to 20 in 100 steps
A = np.linspace(0,1,100) #We want our A values to range from 0 to 1 in 100 steps
for i in range(100):
    for j in range(100):
        Nth = 1 + A[j]*np.exp(-(E-E0[i])**2) #This is our theoretical N value
        chi2[i][j] = np.sum(((N-Nth)**2)/(delta**2)) #Solve for chi2 values
    
print('minimum chi2 = ', np.min(chi2)) #The minimum chi2 value can help us find the best fit values for A and E0
chi2min = np.min(chi2) #Print the value of chi2min
chi2max = np.exp(-chi2min/2) #Maximum value of chi2
imin, jmin = np.where(chi2 == np.min(chi2)) #minimum values of i and j
E0min = E0[imin[0]] #Minimum E0 value
Amin = A[jmin[0]] #Minimum A value
print('The minimum is at E0 = ', E0min, 'A = ', Amin)
plt.figure(2)
plt.imshow(chi2)

plt.figure(1)
plt.plot(E,1+Amin*np.exp(-(E-E0min)**2)) #Here is the likelihood function so we can see how our answers compare
#Everything makes sense to me.  We have a nice-looking distribution, and the data plot looks good.

#Now to try and make the error bars:  part 2 of the homework
for i in range(20):
    for j in range(100):
        F = np.sum(((N - 1 - A[j]*np.exp(-(E-E0[i])**2)))/(2*delta**2)) #define a function F with A and E0
        dFA = np.sum(((N - 1 - A[j]*np.exp(-(E-E0[i])**2)))/delta**2) #Derivative of F with respect to A
        ddFA = np.sum(np.exp(-2(E-E0[i])**2)/delta**2) #Second derivative of F with respect to A
        dFAE = np.sum((-2*A[j]*E*np.exp(-(E-E0[i])**2))/delta**2) #Derivative of F with respect to A and E0
        dFE = np.sum((N - 1 - (-2*A[j]*E*np.exp(-(E-E0[i])**2)))/(2*delta**2)) #Deriative of F with respect to E0
        ddFE = np.sum((-A[j]*np.exp(-(E-E0[i])**2) + 2*A[j]*E*np.exp(-(E-E0[i])**2))/(delta**2)) #Second derivative of F with respect to E0
        Matrix = np.array([ddFA, dFAE],[dFAE,ddFE]) #Create a matrix of derivative values
        print(Matrix)
        Inv = np.linalg.inv(Matrix) #the errorbars for our data should be the inverse values of the matrix
        print(Inv)
    
plt.figure(3)
plt.errorbar(Amin,E0min,Inv[0,0],Inv[1,1],fmt='o')
#I am having trouble running the code.  It makes sense to me, but I don't understand what error I'm running into
#When I take out the code for problem 2, my code runs fine

#Moving on to part 4 since we aren't having any luck with the second derivatives
#Let's create a fake data set and see how it looks - what is the distribution like, and how often do we get A* values that are as large as the real data?
Afakedata = np.zeros(1000) #make an array for fakedata values
Ntrue = np.ones(np.size(N)) #This is the array for our true values of N
for k in range(1000):
    print(k) #Print k so we know how long it takes us to make our plots
    noise = np.random.normal(0, delta) #Noise function
    Nmeasured = Ntrue + noise #The measured N value
    #repeat the measurement on fake data
    for i in range(100):
        for j in range(100):
            Nth = 1 + A[j]*np.exp(-(E-E0[i])**2) #Theoretical N value
            chi2[i][j] = np.sum((Nth-Nmeasured)**2/delta**2) #chi2 for our fake data
        chi2min = np.min(chi2) #minimum chi2 value for our fake data
        imin, jmin = np.where(chi2 == np.min(chi2)) #new imin and jmin value
        E0min = E0[imin[0]] #New E0 min value
        Amin = A[jmin[0]] #New A min value
        Afakedata[k] = Amin

plt.figure(4)
plt.errorbar(E, Nmeasured, delta, fmt='o')
#This looks good.  We get values of A* that are as large as the actual data a reasonable amount of the time.  The plots actually look rather similar.

