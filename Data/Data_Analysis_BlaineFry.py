# -*- coding: utf-8 -*-
"""
Created on Tue Dec 04 19:13:08 2018

@author: Blaine Fry
"""
# Phys 639

"""
Problem: Best Fit values (lvl*)
"""

import numpy as np
from matplotlib import pyplot as plt

# load experimental data
E,N,N_err = np.loadtxt('C:\\Users\\kilof\\OneDrive\\Documents\\Python Scripts\\DataAnalysis.txt',usecols=(0,1,2),unpack=True)

# plot data
plt.figure(1)
plt.title('Data Fitting')
plt.xlabel('E')
plt.ylabel('N')
plt.errorbar(E,N,yerr=N_err,fmt='bo',label='Raw Data')
plt.grid()


# loop over parameter values
N_steps = 1001
E0_max = 20
A_max = 3
E0_guesses = np.linspace(0,E0_max,num=N_steps)
A_guesses = np.linspace(0,A_max,num=N_steps)
chi_squared_values = np.zeros((N_steps,N_steps))
likelihood_values = np.zeros((N_steps,N_steps))
log_likelihood_values = np.zeros((N_steps,N_steps))
min_chi_squared = 10e5
for i in range(N_steps):
    E0_guess = E0_guesses[i] # set parameter value for this run
    for j in range(N_steps):
        A_guess = A_guesses[j] # set parameter value for this run
        # generate theory values from these guesses
        N_th = [] 
        for e in E:
            N_th.append(1 + A_guess*np.exp((-1)*(e-E0_guess)*(e-E0_guess)))
        # calculate chi-squared with these theory values
        chi_squared = 0
        for k in range(len(N)):
            chi_squared += ((N[k]-N_th[k])**2)/(N_err[k]**2)
        chi_squared_values[i][j] = chi_squared
        likelihood_values[i][j] = np.exp((-0.5)*chi_squared)
        log_likelihood_values[i][j] = (0.5)*chi_squared
        # keep track of minimum chi_squared
        if chi_squared < min_chi_squared:
            min_chi_squared = chi_squared
            E0_best = E0_guess
            A_best = A_guess

# Print out best fit values
print 'A_best = ' + str(A_best)
print 'E0_best = ' + str(E0_best)
print 'N = 1 + ' + str(A_best) + '*e^(-(E - ' + str(E0_best) + ')^2)'

# overplot best fit line
x = np.linspace(min(E),max(E),num=1001)
def best_fit(X):
    return 1 + A_best*np.exp((-1)*(X-E0_best)*(X-E0_best))
plt.figure(1)
plt.plot(x,best_fit(x),'r-',label='Best Fit')


# plot chi_squared and likelihoods
plt.figure(2)
plt.title('Chi-Squared Values')
plt.imshow(chi_squared_values)
plt.figure(3)
plt.title('Likelihood Values')
plt.imshow(likelihood_values)

"""
Problem: Error Bars (lvl*)
"""

# get error bars on best fit values
# define numerical approximations of second derivatives for calculation of Hessian Matrix
def d2A_log_likelihood(A,E0):
    A_list = A_guesses.tolist()
    xidx = A_list.index(A)
    E0_list = E0_guesses.tolist()
    yidx = E0_list.index(E0)
    return (log_likelihood_values[yidx][xidx+1] + log_likelihood_values[yidx][xidx-1] - 2*log_likelihood_values[yidx][xidx])/((A_list[xidx+1]-A_list[xidx])**2)
def d2E0_log_likelihood(A,E0):
    A_list = A_guesses.tolist()
    xidx = A_list.index(A)
    E0_list = E0_guesses.tolist()
    yidx = E0_list.index(E0)
    return (log_likelihood_values[yidx+1][xidx] + log_likelihood_values[yidx-1][xidx] - 2*log_likelihood_values[yidx][xidx])/((E0_list[xidx+1]-E0_list[xidx])**2)
def d2AE0_log_likelihood(A,E0):
    A_list = A_guesses.tolist()
    xidx = A_list.index(A)
    E0_list = E0_guesses.tolist()
    yidx = E0_list.index(E0)
    return (log_likelihood_values[yidx-1][xidx-1] + log_likelihood_values[yidx+1][xidx+1] - log_likelihood_values[yidx-1][xidx+1] - log_likelihood_values[yidx+1][xidx-1])/(4*(E0_list[xidx+1]-E0_list[xidx])*(A_list[xidx+1]-A_list[xidx]))

H = np.zeros((2,2))
H[0][0] = d2A_log_likelihood(A_best,E0_best)
H[0][1] = d2AE0_log_likelihood(A_best,E0_best)
H[1][0] = d2AE0_log_likelihood(A_best,E0_best)
H[1][1] = d2E0_log_likelihood(A_best,E0_best)

H_inv = np.linalg.inv(H)

A_err = np.sqrt(H_inv[0][0])
E0_err = np.sqrt(H_inv[1][1])

plt.figure(1)
plt.errorbar(E0_best,1+A_best,xerr=E0_err,yerr=A_err,fmt='ro',label='(E0_best,1 + A_best)')
plt.ylim(0,2)
plt.legend()
plt.grid()