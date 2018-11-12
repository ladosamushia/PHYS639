# Written 11-11-18 with the assistance of Phillip Lucas, and WAAAAY too many of the phys/math help tutors*
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from matplotlib.colors import Normalize

phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))
iterations = 1000
Ngrid = 100

B = 4

for i in range(Ngrid):
    for j in range(Ngrid):
        if B == 1 :
            if i >= 40 and i <=60 and j >=40 and j <=60:
                phi[i][j] = 1
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi[i][j] = 0
            else:
                phi[i][j] = 0
        if B == 2:  # C
            if i >= 25 and i <= 75 and j == 49:
                phi[i][j] = 1
            elif i >= 25 and i <= 75 and j == 51: 
                phi[i][j] = -1
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi[i][j] = 0
            else:
                phi[i][j] = 0 
        if B == 3:  # Plates 
            if i >= 25 and i <= 75 and j == 25:
                phi[i][j] = 1
            elif j >= 40 and j <= 90 and i == 50: 
                phi[i][j] = -1
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi[i][j] = 0
            else:
                phi[i][j] = 0 
        if B == 4:  # Circular C
            if (i-50)**2 + (j-50)**2 <= 25: 
                phi[i][j] = 1
            elif (i-50)**2 + (j-50)**2 >= 450 and (i-50)**2 + (j-50)**2 <= 500: 
                phi[i][j] = -1
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi[i][j] = 0
            else:
                phi[i][j] = 0
plt.imshow(phi)
for k in range(iterations):
    for i in range(Ngrid):
        for j in range(Ngrid):
            if B == 1:
                if i >= 40 and i <=60 and j >=40 and j <=60:
                    phi_new[i][j] = 100
                elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                    phi_new[i][j] = 0
                else:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
            if B == 2:  # C 
                if i >= 25 and i <=75 and j == 49:
                    phi_new[i][j] = 1
                elif i >= 25 and i <=75 and j == 51: 
                    phi_new[i][j] = -1
                elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                    phi_new[i][j] = 0
                else:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
            if B == 3:  # Plates
                if i >= 25 and i <=75 and j == 25:
                    phi_new[i][j] = 1
                elif j >= 40 and j <= 90 and i == 50: 
                    phi_new[i][j] = -1
                elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                    phi_new[i][j] = 0
                else:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
            if B == 4:  # Circular C
                if (i-50)**2 + (j-50)**2 <= 25:
                    phi_new[i][j] = 1
                elif (i-50)**2 + (j-50)**2 >= 450 and (i-50)**2 + (j-50)**2 <=500: 
                    phi_new[i][j] = -1
                elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                    phi_new[i][j] = 0
                else:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0 
    phi = np.copy(phi_new)
    Ex, Ey = np.gradient(phi)
    if B == 1: 
        plt.figure(1)
        plt.title("Cube")
    if B == 2: 
        plt.figure(1)
        plt.title("Plate Capacitor")
    if B == 3: 
        plt.figure(1)
        plt.title("Perpendicular Plates")
    if B == 4: 
        plt.figure(1)
        plt.title("Concentric Circlular Capacitors")
plt.figure(1)
plt.imshow(phi)
plt.figure(3)
plt.plot(Ex, Ey)
