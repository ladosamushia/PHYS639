import numpy as np
import matplotlib.pyplot as plt

n_steps = 4000
h_bar = 1
m = 1


def solve(x_min, x_max, potential):
    x = np.linspace(x_min, x_max, n_steps)
    dx = x[1] - x[0]
    V = np.fromfunction(np.vectorize(potential), (n_steps,),
                        dx=dx, x_min=x_min, x_max=x_max)
    A = -(h_bar**2)/(2 * m) * (1 / dx**2) * (np.diag(np.ones(n_steps - 1), -1) - 2 *
                                             np.diag(np.ones(n_steps)) + np.diag(np.ones(n_steps - 1), 1)) + np.diag(V)
    energy, psi_transpose = np.linalg.eigh(A)
    psi = np.transpose(psi_transpose)
    return energy, psi


n_plot = 5

plt.figure()

# infinite square well
plt.subplot(2, 2, 1)
e, p = solve(0, 1, lambda x, x_min, x_max, dx: 0)
for i in range(n_plot):
    plt.plot(-p[i], label=str(round(e[i], 3)))
plt.legend()

# infinite square well with a wall
plt.subplot(2, 2, 2)
e, p = solve(0, 1, lambda x, x_min, x_max,
             dx: 10**3 if 1800 <= x < 2200 else 0)
for i in range(n_plot):
    plt.plot(-p[i], label=str(round(e[i], 3)))
plt.legend()

# simple harmonic oscillator
plt.subplot(2, 2, 3)
e, p = solve(-0.5, 0.5, lambda x, x_min, x_max, dx: 0.001 * (x - n_steps/2)**2)
for i in range(n_plot):
    plt.plot(p[i], label=str(round(e[i], 3)))
plt.legend()

# simple harmonic oscillator with a wall
plt.subplot(2, 2, 4)
e, p = solve(-0.5, 0.5, lambda x, x_min, x_max, dx: 10**3 if 1800 <=
             x < 2200 else 0.001 * (x - n_steps/2)**2)
for i in range(n_plot):
    plt.plot(p[i], label=str(round(e[i], 3)))
plt.legend()

plt.show()
