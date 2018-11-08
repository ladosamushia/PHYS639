#James Corona
#Laplace Equation
#PHYS 639

import numpy as np
import matplotlib.pyplot as plt

##############################################################################

#Problem: Square in a Box

Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))

Niterations = 1000
for k in range(Niterations):
    for i in range(Ngrid):
        for j in range(Ngrid):
            if 40 <= i <= 60 and 40 <= j <= 60:
                phi_new[i][j] = 1
            elif i == 0 or j == 0 or i == Ngrid - 1 or j == Ngrid - 1:
                phi_new[i][j] = 0
            else:
                phi_new[i][j] = (phi[i - 1][j] + phi[i + 1][j] + phi[i][j - 1] + phi[i][j + 1]) / 4.0
    phi = np.copy(phi_new)

plt.figure()
plt.imshow(phi)

##############################################################################

#Problem: Parallel Plate Capacitor

Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))

Niterations = 1000
for k in range(Niterations):
    for i in range(Ngrid):
        for j in range(Ngrid):
            if i == 45 and 30 <= j <= 70:
                phi_new[i][j] = 1
            elif i == 55 and 30 <= j <= 70:
                phi_new[i][j] = -1
            elif i == 0 or j == 0 or i == Ngrid - 1 or j == Ngrid - 1:
                phi_new[i][j] = 0
            else:
                phi_new[i][j] = (phi[i - 1][j] + phi[i + 1][j] + phi[i][j - 1] + phi[i][j + 1]) / 4.0
    phi = np.copy(phi_new)

plt.figure()
plt.imshow(phi)

##############################################################################

#Problem: Perpendicular Plates

Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))

Niterations = 1000
for k in range(Niterations):
    for i in range(Ngrid):
        for j in range(Ngrid):
            if i == 50 and 25 <= j <= 65:
                phi_new[i][j] = 1
            elif 30 <= i <= 70 and j == 75:
                phi_new[i][j] = -1
            elif i == 0 or j == 0 or i == Ngrid - 1 or j == Ngrid - 1:
                phi_new[i][j] = 0
            else:
                phi_new[i][j] = (phi[i - 1][j] + phi[i + 1][j] + phi[i][j - 1] + phi[i][j + 1]) / 4.0
    phi = np.copy(phi_new)

plt.figure()
plt.imshow(phi)

##############################################################################

#Problem: Charge in a Box 1

Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))

charge = np.zeros((Ngrid,Ngrid))
charge[50][50] = 1

Niterations = 1000
for k in range(Niterations):
    for i in range(Ngrid):
        for j in range(Ngrid):
            if i == 0 or j == 0 or i == Ngrid - 1 or j == Ngrid - 1:
                phi_new[i][j] = 0
            else:
                phi_new[i][j] = (phi[i - 1][j] + phi[i + 1][j] + phi[i][j - 1] + phi[i][j + 1] + charge[i][j]) / 4.0
    phi = np.copy(phi_new)

plt.figure()
plt.imshow(phi)

##############################################################################

#Problem: Charge in a Box 2

Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))

charge = np.zeros((Ngrid,Ngrid))
charge[50][95] = 1

Niterations = 1000
for k in range(Niterations):
    for i in range(Ngrid):
        for j in range(Ngrid):
            if i == 0 or j == 0 or i == Ngrid - 1 or j == Ngrid - 1:
                phi_new[i][j] = 0
            else:
                phi_new[i][j] = (phi[i - 1][j] + phi[i + 1][j] + phi[i][j - 1] + phi[i][j + 1] + charge[i][j]) / 4.0
    phi = np.copy(phi_new)

plt.figure()
plt.imshow(phi)

##############################################################################

#Problem: Dipole in a Box

Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))

charge = np.zeros((Ngrid,Ngrid))
charge[50][48] = 1
charge[50][52] = -1

Niterations = 1000
for k in range(Niterations):
    for i in range(Ngrid):
        for j in range(Ngrid):
            if i == 0 or j == 0 or i == Ngrid - 1 or j == Ngrid - 1:
                phi_new[i][j] = 0
            else:
                phi_new[i][j] = (phi[i - 1][j] + phi[i + 1][j] + phi[i][j - 1] + phi[i][j + 1] + charge[i][j]) / 4.0
    phi = np.copy(phi_new)

plt.figure()
plt.imshow(phi)

##############################################################################
