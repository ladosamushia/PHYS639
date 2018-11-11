"""
Created on Fri Nov 2 2018 By Philip Lucas

Using and Building on In-Class Lecture and Demo for Laplace solutions By Dr. Lado Samushia
Assisted by Dr. Washburn, Dylan Parker and the Math Help room to try and make 3-D plots.
So far it hasn't worked. 
Potentials solved by approximating Laplace and Poisson Equations Via relaxation method. 
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from matplotlib.colors import Normalize
Niterations = 10000 # more than 10000 seems to take forever on my hardware exceed at your own risk. 
Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))
B = 4 # to determine which line to run
Q = 0.99 # don't use "1" it breaks the  all other values appear to work
# for values of "B" 1 = cube 1 = Capacitor 3 = perp plate capacitor 
# 4 = circulate
for i in range(Ngrid):
    for j in range(Ngrid):
        if B == 1 : # charged box in a gounded box
            if i >= 40 and i <=60 and j >=40 and j <=60:
                phi[i][j] = 1
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi[i][j] = 0
            else:
                phi[i][j] = 0
        if B == 2:  #Capacitor 
            if i >= 25 and i <= 75 and j == 49:
                phi[i][j] = 1
            elif i >= 25 and i <= 75 and j == 51: 
                phi[i][j] = -1
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi[i][j] = 0
            else:
                phi[i][j] = 0 
        if B == 3:  # perp plates 
            if i >= 25 and i <= 75 and j == 25:
                phi[i][j] = 1
            elif j >= 40 and j <= 90 and i == 50: 
                phi[i][j] = -1
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi[i][j] = 0
            else:
                phi[i][j] = 0 
        if B == 4:  #circle capacitor 
            if (i-50)**2 + (j-50)**2 <= 25: 
                phi[i][j] = 1
            elif (i-50)**2 + (j-50)**2 >= 450 and (i-50)**2 + (j-50)**2 <= 500: 
                phi[i][j] = -1
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi[i][j] = 0
            else:
                phi[i][j] = 0
        if B == 5: # Center particle
            if i == 50 and j == 50:
                phi[i][j] = -Q/4 
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi[i][j] = 0
            else:
                phi[i][j] = 0
        if B == 6:  # Edge Particle
            if i >= 1 and j == 50:
                phi[i][j] = -Q/4 
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi[i][j] = 0
            else:
                phi[i][j] = 0 
        if B == 7:  # two points 
            if i == 45 and j == 45:
                phi[i][j] = -Q/4
            elif i == 55 and j == 55: 
                phi[i][j] = Q/4
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi[i][j] = 0
            else:
                phi[i][j] = 0 
plt.imshow(phi)
for k in range(Niterations):
    for i in range(Ngrid):
        for j in range(Ngrid):
            if B == 1:
                if i >= 40 and i <=60 and j >=40 and j <=60:
                    phi_new[i][j] = 100
                elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                    phi_new[i][j] = 0
                else:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
            if B == 2:  #Capacitor 
                if i >= 25 and i <=75 and j == 49:
                    phi_new[i][j] = 1
                elif i >= 25 and i <=75 and j == 51: 
                    phi_new[i][j] = -1
                elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                    phi_new[i][j] = 0
                else:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
            if B == 3:  #perp plate
                if i >= 25 and i <=75 and j == 25:
                    phi_new[i][j] = 1
                elif j >= 40 and j <= 90 and i == 50: 
                    phi_new[i][j] = -1
                elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                    phi_new[i][j] = 0
                else:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
            if B == 4:  #circle capacitor 
                if (i-50)**2 + (j-50)**2 <= 25:
                    phi_new[i][j] = 1
                elif (i-50)**2 + (j-50)**2 >= 450 and (i-50)**2 + (j-50)**2 <=500: 
                    phi_new[i][j] = -1
                elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                    phi_new[i][j] = 0
                else:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0 
            if B == 5: # one particle center
                if i == 50 and j == 50:
                    phi_new[i][j] = -Q/4 + (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
                elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                    phi_new[i][j] = 0
                else:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
            if B == 6:  # Edge particle
                if i == 1 and j == 50:
                    phi_new[i][j] = -Q/4 + (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
                elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                    phi_new[i][j] = 0
                else:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
            if B == 7:  # two particles
                if i == 45 and j == 45:
                    phi_new[i][j] = -Q/4 + (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
                elif i == 55 and j == 55: 
                    phi_new[i][j] = Q/4 + (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
                elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                    phi_new[i][j] = 0
                else:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
    phi = np.copy(phi_new)
    Ex, Ey = np.gradient(phi) # ended up not using due to arrow function making too many overlaping vectors even with skipping arrows
    if B == 1: 
        plt.figure(1)
        plt.title("Centered Cube of Constant Voltage")
    if B == 2: 
        plt.figure(1)
        plt.title("Plate Capacitor")
    if B == 3: 
        plt.figure(1)
        plt.title("Perp Plates of Constant Voltage")
    if B == 4: 
        plt.figure(1)
        plt.title("Concentric Circle Capacitor")
    if B == 5: 
        plt.figure(1)
        plt.title("Single Charge")
    if B == 6: 
        plt.figure(1)
        plt.title("Charge by a groudned wall")
    if B == 7: 
        plt.figure(1)
        plt.title("Two opposite charges")
plt.figure(1)
plt.imshow(phi)
plt.figure(3)
plt.plot(phi)
# I tried to make an elevation plot of the voltages but I couldn't get it to work. The closest I got was 
# a 2-D projection on a 3-D grid. 

# this code could be stream lined with functions but I did not have time to work out those kinks. 
# as a result there is a lot of repetition with "B" determining which lines to run. 