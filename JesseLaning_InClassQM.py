import numpy as np
import matplotlib.pyplot as plt
import math

n_steps = 1000
h_bar = 1
m = 1
x = np.linspace(-0.5, 0.5, n_steps)
dx = x[1] - x[0]
V = np.zeros(n_steps)

A = np.zeros((n_steps, n_steps))

# for i in range(n_steps):
#     if i > 449 and i < 550:
#         V[i] = 50000

# for i in range(n_steps):
#     V[i] = (i - n_steps/2)**2 * dx * 0.5
#     if i > 449 and i < 550:
#         V[i] = 100_000

for i in range(n_steps):
    if i > 500:
        V[i] = 50

dx2_inv = 1/(dx**2)

for i in range(n_steps):
    for j in range(n_steps):
        if i == j:
            A[i][j] = dx2_inv + V[j]
        if i == j - 1 or i == j + 1:
            A[i][j] = -dx2_inv * 0.5

E, psi_t = np.linalg.eigh(A)
psi = np.transpose(psi_t)

for i in range(5):
    plt.plot(psi[i], label=str(E[i]))
plt.legend()
plt.show()
