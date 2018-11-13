#Created by Parker Stoops with help from Jesse Lanning

#Laplace problems

import numpy as np
import matplotlib.pyplot as plt

n_steps = 1000
n_grid = 100



def problem1():
    phi = np.zeros((n_grid, n_grid))
    phi_n = np.copy(phi)

    for i in range(n_grid):
        for j in range(n_grid):
            if 40 <= i < 70 and 40 <= j < 70:
                phi[i][j] = 100
            elif i == 0 or j == 0:
                phi[i][j] = 0
            else:
                phi[i][j] = ((i-50)**2 + (j-50)**2)**-1 * 10_000

    for k in range(n_steps):
        for i in range(n_grid):
            for j in range(n_grid):
                if 30 <= i < 60 and 30 <= j < 60:
                    phi_n[i][j] = 100
                elif 0 < i < n_grid - 1 and 0 < j < n_grid - 1:
                    phi_n[i][j] = (phi[i - 1][j] + phi[i + 1][j] +
                                   phi[i][j - 1] + phi[i][j + 1]) / 4
                else:
                    phi_n[i][j] = 0
        phi = np.copy(phi_n)
    plt.imshow(phi)
    plt.show()



def problem2():
    phi = np.zeros((n_grid, n_grid))
    phi_n = np.copy(phi)

    for i in range(25, 75):
        phi[i][49] = 1
        phi[i][51] = -1

    for k in range(n_steps):
        for i in range(n_grid):
            for j in range(n_grid):
                if 25 <= i < 75 and j == 49:
                    phi_n[i][j] = 1
                elif 25 <= i < 75 and j == 51:
                    phi_n[i][j] = -1
                elif 0 <= i < n_grid - 1 and 0 <= j < n_grid - 1:
                    phi_n[i][j] = (phi[i - 1][j] + phi[i + 1][j] +
                                   phi[i][j - 1] + phi[i][j + 1]) / 4
        phi = np.copy(phi_n)
    plt.imshow(phi)
    plt.show()



def problem3():
    phi = np.zeros((n_grid, n_grid))
    phi_n = np.copy(phi)

    for i in range(25, 75):
        phi[i][25] = 1

    for i in range(40, 90):
        phi[50][i] = -1

    for k in range(n_steps):
        for i in range(n_grid):
            for j in range(n_grid):
                if 25 <= i < 75 and j == 25:
                    phi_n[i][j] = 1
                elif i == 50 and 40 <= j < 90:
                    phi_n[i][j] = -1
                elif 0 <= i < n_grid - 1 and 0 <= j < n_grid - 1:
                    phi_n[i][j] = (phi[i - 1][j] + phi[i + 1][j] +
                                   phi[i][j - 1] + phi[i][j + 1]) / 4
        phi = np.copy(phi_n)
    plt.imshow(phi)
    plt.show()
problem1()
problem2()
problem3()