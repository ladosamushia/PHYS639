
import numpy as np
import matplotlib.pyplot as plt

Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))

# for i in range(Ngrid):
#     for j in range(Ngrid):
#         if i >= 40 and i <=60 and j >=40 and j <=60:
#             phi[i][j] = 100
#         elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
#             phi[i][j] = 0
#         else:
#             phi[i][j] = 0

# plt.imshow(phi)

Niterations = 500
for k in range(Niterations):
    print(k)
    for i in range(Ngrid):
        for j in range(Ngrid):
            #print(i,j)
            if i >= 50 and i <= 51 and j >= 35 and j <=75:
                phi_new[i][j] = 1
            elif i >=51  and i <= 75 and j >= 36 and j <=37:
                phi_new[i][j] = -1
            elif i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi_new[i][j] = 0
            else:
                phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4.0
            
    plt.pause(0.000000005)
    phi = np.copy(phi_new)
    plt.clf()
    plt.imshow(phi)
Ex,Ey = np.gradient(phi_new)
plt.figure()
plt.quiver(Ey[::5],Ex[::5],scale=1.5)
plt.show()