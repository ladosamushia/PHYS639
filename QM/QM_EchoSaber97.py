#James Corona
#Schroedinger's Equation
#PHYS 639

import numpy as np
import matplotlib.pyplot as plt

#Problem: Infinite Potential Well

steps = 1E4
N = 5

dE = 0.1
n = 1
E = dE
dx = 1 / steps
x = np.linspace(0, 1, int(steps) + 1)
finalpsi = [1, 2, 3]

while n <= N:
    
    psi = np.zeros(int(steps) + 1)
    dpsi = 1
    
    for i in range(int(steps)):
        psi[i + 1] = psi[i] + dpsi * dx
        dpsi -= 2 * E * psi[i + 1] * dx
    
    finalpsi.append(np.abs(psi[-1]))
    
    if finalpsi[-3] >= finalpsi[-2] <= finalpsi[-1]:
        print('Energy %d: %.1f' %(n, E - dE))
        plt.plot(x, psi)
        plt.xlabel('X')
        plt.ylabel('Psi')
        plt.title('Probability Distribution Functions')
        n += 1
    
    E += dE

#Program computes up to any number of energy levels N. Values for energy are
#all within 0.1 of exact values.
