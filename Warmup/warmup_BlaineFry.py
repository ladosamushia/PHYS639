# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 16:02:41 2018

@author: Blaine Fry
"""

# Phys 639 Warmup Homework
"""
note: I'm currently in diff EQ, and it's early in the course
 so pardon if I don't offer analytical solutions
"""
"""
Problem: Radioactive Decay *
Describe the radioactive decay of Uranium-235 (Tau = 703.8 million years)
"""

import numpy as np
import matplotlib.pyplot as plt

# Define Parameters
N0 = 10 # intial U-235 population in terms of Avagadro's #
tau = 703.8 # half life in millions of years
t_i = 0 # initial time
t_f = 10*tau # final time
Nsteps = 10**4 # number of time values used to solve ODE

# Generate values to fill the time interval
t = np.linspace(t_i,t_f,Nsteps+1)
dt = (t_f - t_i)/Nsteps
N = np.zeros(Nsteps + 1)
N[0] = N0 # set initial value
for i in range(1,Nsteps + 1): #starts at 1 bc N[0] is initialized to N0
    dN = -N[i-1]/tau
    N[i] = N[i-1] + dN*dt
    
# draw line for Tau as validity check
y_tau = np.linspace(0,10,Nsteps)
x_tau = [tau]*Nsteps

# plot stuff
plt.figure(1)
plt.plot(t,N,'g.', label = 'numerical solution')
plt.plot(t,N0*np.exp(-t/tau),'y-', label = 'analytical solution')
plt.plot(x_tau, y_tau, 'r-', label = 'time = tau')
plt.title('Uraniam-235 Decay (fig. 1)')
plt.xlabel('time in millions of years')
plt.ylabel('Uranium Population / N_A')
plt.grid()
plt.legend()

# The numerical solution matches with the analytical solution
# exponential decay is shown as one would expect
# when t = tau, 1/e of the population remains, as expected from the analytic solution

"""
Problem: Population Growth ** 
Describe a rodent population predicted by the ODE: dN/dt = (alpha)N - (beta)N**2
"""

# set up time range
t_i = 0. # initial time
t_f = 0.4 # final time
Nsteps = 10**4 # number of sub intervals used for numerical ODE solution

# if we want to experiment with different values for N0, alpha, & beta
# we should make a function we can call on those different values
def rodent_population(init_pop, alpha, beta, figure_number):
    # set up the ODE
    t = np.linspace(t_i,t_f,Nsteps+1) # describe time interval
    dt = (t_f - t_i)/Nsteps # small change in time
    N = np.zeros(Nsteps + 1) # array in which to store population values
    N[0] = init_pop # set initial value
    # solve the ODE
    for i in range(1,Nsteps + 1): #starts at 1 bc N[0] is initialized to N0
        dN = alpha*N[i-1] - beta*N[i-1]*N[i-1]
        N[i] = N[i-1] + dN*dt
    # plot everything
    plt.figure(figure_number)
    plt.title('Rodent Populations (fig. ' + str(figure_number) + ')')
    plt.ylabel('Number of Rodents')
    plt.xlabel('Time (arb.)')
    plt.ylim(0,50)
    plt.plot(t,N, label = 'N0 = ' + str(init_pop) + '  alpha = ' + str(alpha) + '  beta = ' + str(beta))    
    plt.legend()
    plt.grid(True)
    return

# time for tests and sanity checks
rodent_population(10,10,0,2) # immortal rodents
rodent_population(10,0,10,2) # sterile rodents
rodent_population(0,10,1,2) # no rodents
# each situation seems to make sense. rodents die or grow accordingly, and ...
# ... none appear spontaneously (see figure 2)

# let's try some values
rodent_population(20,20,2,3)
rodent_population(20,60,4,3)
rodent_population(20,200,10,3)
rodent_population(20,100,4,3)
rodent_population(20,60,2,3)
# as an empirical result, notice that the populations converge... 
# ...to a value of alpha/beta (see figure 3)

# now vary the initial populations
rodent_population(10,60,4,4)
rodent_population(20,60,4,4)
rodent_population(30,60,4,4)
rodent_population(40,60,4,4)
# again emperically, note that the initial population doesn't effect ...
# ... where the population stabilizes. (see figure 4)

"""
Problem: Coupled Radioactive Decay 1 ***
B decays into A, and A decays into something else, as governed by a
system of differential equations
"""

# set up time range
t_i = 0. # initial time
t_f = 100. # final time
Nsteps = 10**4 # number of sub intervals used for numerical ODE solution

# make a function that solves the coupled diff eqs
def coupled_decay_1(init_pop_A,init_pop_B,tau_A,tau_B,figure_number):
    # set up the ODE
    t = np.linspace(t_i,t_f,Nsteps+1) # describe time interval
    dt = (t_f - t_i)/Nsteps # small change in time
    N_A = np.zeros(Nsteps + 1) # array in which to store population values
    N_B = np.zeros(Nsteps + 1)
    N_A[0] = init_pop_A # set initial value
    N_B[0] = init_pop_B
    # solve the ODE
    for i in range(1,Nsteps + 1): #starts at 1 bc N[0] is initialized to N0
        dN_A = (-1)*(N_A[i-1])/(tau_A)
        N_A[i] = N_A[i-1] + dN_A*dt
        dN_B = (-1)*dN_A - (N_B[i-1])/(tau_B)
        N_B[i] = N_B[i-1] + dN_B*dt
    # plot the results
    plt.figure(figure_number)
    plt.title('Coupled Decay 1 (fig.' + str(figure_number) + ')')
    plt.ylabel('element populations')
    plt.xlabel('time (arb.)')
    plt.plot(t,N_A, label = 'A: tau_A = ' + str(tau_A))
    plt.plot(t,N_B, label = 'B: tau_B = ' + str(tau_B))
    plt.grid(True)
    plt.legend()
    return

# let's test each element individually
coupled_decay_1(50,0,10,100,5) # no B initially (figure 5)
coupled_decay_1(0,50,10,100,6) # no A initially (figure 6)
# hmmm..... something's not right. these solutions show that A decays to B ...
# ... not the other way around as stated in the question.
# but other than that, things seem reasonable.
    
# now to vary tau_A
coupled_decay_1(50,0,10,150,7)
coupled_decay_1(50,0,20,150,7)
coupled_decay_1(50,0,40,150,7)
# the results make sense; larger tau_A means A takes longer to decay
# ...and that B won't grow as fast (note I made tau_B large so it would stick around)

"""
Problem: Coupled Radioactive Decay 2 ***
similar to above, but described by different equations
"""

# set up time range
t_i = 0. # initial time
t_f = 100. # final time
Nsteps = 10**4 # number of sub intervals used for numerical ODE solution

# make a function that solves the coupled diff eqs
def coupled_decay_2(init_pop_A,init_pop_B,tau,figure_number):
    # set up the ODE
    t = np.linspace(t_i,t_f,Nsteps+1) # describe time interval
    dt = (t_f - t_i)/Nsteps # small change in time
    N_A = np.zeros(Nsteps + 1) # array in which to store population values
    N_B = np.zeros(Nsteps + 1)
    N_A[0] = init_pop_A # set initial value
    N_B[0] = init_pop_B
    # solve the ODE
    for i in range(1,Nsteps + 1): #starts at 1 bc N[0] is initialized to N0
        dN_A = (N_B[i-1])/tau - (N_A[i-1])/tau
        N_A[i] = N_A[i-1] + dN_A*dt
        dN_B = (N_A[i-1])/tau - (N_B[i-1])/tau
        N_B[i] = N_B[i-1] + dN_B*dt
    # plot the results
    plt.figure(figure_number)
    plt.title('Coupled Decay 2 (fig.' + str(figure_number) + ')')
    plt.ylabel('element populations')
    plt.xlabel('time (arb.)')
    plt.plot(t,N_A, label = 'A')
    plt.plot(t,N_B, label = 'B')
    plt.grid(True)
    plt.legend()
    return

# let's just try it out bc I'm not sure what to expect...
coupled_decay_2(50,50,10,8) # figure 8
# huh... I guess that makes sense. dN/dt would be zero when N_A = N_B
# so let's try different starting values
coupled_decay_2(0,50,10,9) # figure 9
coupled_decay_2(50,0,10,10) # figure 10
# the populations seem to converge to an equillibrium, and ...
# ... it doesn't matter which starts higher

# what is the equillibrium value? judging from figs 9 & 10,
# I'm guessing the average of the intial populations
# so let's test it...
coupled_decay_2(100,50,15,11)
predicted_value = [75]*(Nsteps + 1)
t = np.linspace(t_i,t_f,Nsteps+1)
plt.figure(11)
plt.plot(t,predicted_value,'k-.', label = 'predicted equillibrium')
plt.legend()
# yep, works for that one (figure 11)
coupled_decay_2(0,300,15,12)
predicted_value = [150]*(Nsteps + 1)
t = np.linspace(t_i,t_f,Nsteps+1)
plt.figure(12)
plt.plot(t,predicted_value,'k-.', label = 'predicted equillibrium')
plt.legend()
# yep, works for that one too! (figure 12)

# so I've demonstrated emperically that the populations of A an B reach
# an equillibrium value of (1/2)*(A + B), and that it doens't matter
# which started higher.