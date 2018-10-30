import numpy as np
import matplotlib.pyplot as plt
import math

n_steps = 1000
h_bar = 1
m = 1
x = np.linspace(-0.5, 0.5, n_steps)
dx = x[1] - x[0]
V = np.zeros(n_steps)

# potential for an infinite well
A = np.zeros((n_steps, n_steps))

# potential for an infinite well with a wall in the middle
# for i in range(n_steps):
#     if i > 449 and i < 550:
#         V[i] = 50000

# potential for a simple harmonic oscillator with a wall in the middle
# for i in range(n_steps):
#     V[i] = (i - n_steps/2)**2 * dx * 0.5
#     if i > 449 and i < 550:
#         V[i] = 100_000

# potential for an infinite well with a finite well after 500 steps
# for i in range(n_steps):
#     if i > 500:
#         V[i] = 50

# compute our 1/(dx*dx) so we don't have to keep calculating it and we can just use this variable
dx2_inv = 1/(dx**2)

# calculate our matrix
for i in range(n_steps):
    for j in range(n_steps):
        if i == j:
            A[i][j] = dx2_inv + V[j]
        if i == j - 1 or i == j + 1:
            A[i][j] = -dx2_inv * 0.5

# compute eigen values and eigen vectors
E, psi_t = np.linalg.eigh(A)
# take the transpose of psi_t to the wavefunction vectors can accessed as psi[n]
psi = np.transpose(psi_t)

for i in range(5):
    plt.plot(psi[i], label=str(E[i]))
plt.legend()
plt.show()
