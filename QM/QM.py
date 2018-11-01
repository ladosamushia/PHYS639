# -*- coding: utf-8 -*-
"""
Created on Thu Nov 01 13:05:50 2018

@author: Blaine Fry
"""
# Phys 639
# QM in 1D

from matplotlib import pyplot as plt
import numpy as np

"""
make a Schrodinger solver to use for the problems:
"""

# establish a spacial interval:
a = 0.0 # left boundary of square well
b = 1.0 # right boundary of square well
N_steps = 10**3
dx = (b-a)/N_steps
x = np.arange(a,b,dx)

def schrodinger_square(potential_energy,init_deriv_range,fig_num,fig_title):
    # make lists in which to store solutions
    discovered_E_lvls = []
    discovered_wave_funcs = []
    # solve the ODEs, varying d_psi and E to find solutions that work
    for e in range(1,12400):
        E = (0.01)*e # set energy value
        for d in init_deriv_range:
            # make lists in which to store solution values at each point
            psi = [0]*N_steps # wavefunction
            d_psi = [0]*N_steps # derivative of wavefunction
            d_d_psi = [0]*N_steps # second derivative of wavefunction
            # initialize
            psi[0] = 0.0
            d_d_psi[0] = (-2.0)*(E-potential_energy[0])*psi[0]
            d_psi[0] = (0.1)*d
            # propagate the solutions
            for i in range(1,N_steps):
                d_psi[i] = d_psi[i-1] + d_d_psi[i-1]*dx
                psi[i] = psi[i-1] + d_psi[i-1]*dx
                d_d_psi[i] = (-2.0)*(E-potential_energy[i])*psi[i]
            # check if it satisfies boundary conditions
            if psi[N_steps-1] < 0.00005 and psi[N_steps-1] > -0.00005:
                discovered_E_lvls.append(E)
                discovered_wave_funcs.append(psi)
                break
    
    # clean up discovered energy levels... get rid of psuedo duplicates
    # make a function that can find items close to a value
    def find_close(my_list, value):
        close = []
        for i in my_list:
            if np.abs(value-i) < 0.2*value:
                close.append(i)
        return close
    # work through some stuff to clean the list
    cleaned_list = []
    compressed_list = []
    for i in range(len(discovered_E_lvls)):
        # find values that are close to each other... will produce duplicates
        compressed_list.append(find_close(discovered_E_lvls,discovered_E_lvls[i]))
    # remove duplicates
    for i in range(len(compressed_list)-1):
        if compressed_list[i] == compressed_list[i+1]:
            compressed_list[i] = []
    while [] in compressed_list:
        compressed_list.remove([])
    for i in range(len(compressed_list)):
        cleaned_list.append(np.average(compressed_list[i]))
    E_lvls = np.round(cleaned_list,decimals=2)
    
    # select one wave function for each energy level
    # need something that can find nearest value
    def find_nearest(my_list, value):
        array = np.asarray(my_list)
        idx = np.abs(array - value).argmin()
        return idx
    # plot stuff
    for i in E_lvls:
        # select wave functions
        idx = find_nearest(discovered_E_lvls,i)
        plt.figure(fig_num)
        plt.title(fig_title)
        plt.xlabel('X')
        plt.ylabel('Psi(x)')    
        plt.plot(x,discovered_wave_funcs[idx],label='E = ' + str(i))
        plt.grid()
        plt.legend()

"""
Problem: Infinite Potential Well (lvl*)
Solve Schrodinger's Equation in an infinite square well
where (-0.5)*Psi_double_dot = E*Psi
i.e. U(x) = 0
"""

U1 = [0]*1000
schrodinger_square(U1,[1],1,'Square Well')

"""
Problem: Wall inside a well (lvl**)
As before, but there's a wall of finite potential energy inside the well
"""

j=2
for m in [10,100,1000]:
    # define a potential energy function
    U2 = [0]*N_steps
    for i in range(N_steps):
        if x[i] >= 0.45 and x[i] <= 0.55:
            U2[i] = m 
    schrodinger_square(U2,[1],j,'Wall Height = ' + str(m))
    j+=1
    