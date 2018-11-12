import numpy as np
import matplotlib.pyplot as plt

N_grid = 50
N_steps = 500

phi_a = np.zeros((N_grid,N_grid))
phi_b = np.zeros((N_grid,N_grid))
phi_c = np.zeros((N_grid,N_grid))
phi_1 = np.zeros((N_grid,N_grid))
phi_2 = np.zeros((N_grid,N_grid))
phi_3 = np.zeros((N_grid,N_grid))


for k in range(N_steps):
    for i in range(N_grid):
        for j in range(N_grid):
            #first star
            if (i>=20) and (i<=30) and (j>=20) and (j<=30) :
                phi_1[i][j] = 1.0
            elif (i==0) or (j==0) or (i==N_grid-1) or (j==N_grid-1) :
                phi_1[i][j] = 0.0
            else:
                phi_1[i][j] = (phi_a[i-1][j] + phi_a[i+1][j] + phi_a[i][j-1] + phi_a[i][j+1])/ 4.00

            #second star
            if (j>=20) and (j<=30) and (i==30) :
                phi_2[i][j] = 1.0
            elif (j>=20) and (j<=30) and (i == 20) :
                phi_2[i][j] = -1.0
            elif (i==0) or (j==0) or (i==N_grid-1) or (j==N_grid-1) :
                phi_2[i][j] = 0.0
            else:
                phi_2[i][j] = (phi_b[i-1][j] + phi_b[i+1][j] + phi_b[i][j-1] + phi_b[i][j+1])/ 4.00

            #third star
            if (j>=20) and (j<=30) and (i==30) :
                phi_3[i][j] = 1.0
            elif (i>=15) and (i<=25) and (j==25) :
                phi_3[i][j] = -1.0
            elif (i==0) or (j==0) or (i==N_grid-1) or (j==N_grid-1) :
                phi_3[i][j] = 0.0
            else:
                phi_3[i][j] = (phi_c[i-1][j] + phi_c[i+1][j] + phi_c[i][j-1] + phi_c[i][j+1])/ 4.00
                
    phi_a = np.copy(phi_1)
    phi_b = np.copy(phi_2)
    phi_c = np.copy(phi_3)

plt.figure(1)
plt.imshow(phi_a)
plt.figure(2)
plt.imshow(phi_b)
plt.figure(3)
plt.imshow(phi_c)