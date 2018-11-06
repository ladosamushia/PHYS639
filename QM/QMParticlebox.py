# Created by Parker Stoops with help from Jesse
# Nov. 5th 2018
# Particle in an infinite square well
#
#
import numpy as np
import matplotlib.pyplot as plt



length = 1000
x = np.linspace(-0.5, 0.5, length)
dx = x[1] - x[0]
V = np.zeros(length)


A = np.zeros((length, length))
dx2_inv = 1/(dx**2)
for k in range(length):
    for n in range(length):
        if k == n - 1 or k == n + 1:
            A[k][n] = -dx2_inv * 0.5
        if k == n:
            A[k][n] = dx2_inv + V[n]
            
E, psi_t = np.linalg.eigh(A)

psi = -np.transpose(psi_t)

for k in range(5):
    plt.plot(psi[k], label=str(E[k]))
plt.legend()
plt.show()