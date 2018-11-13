
import numpy as np
import matplotlib.pyplot as plt

Ngrid = 100
phi = np.zeros((Ngrid,Ngrid))
phi_new = np.zeros((Ngrid,Ngrid))
Q=np.zeros((Ngrid,Ngrid))
#dipole Point charges of opposite signs
Q[49,49]=1
Q[49,53]=-1
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
            #print("i,j:",i,j,k)
            
            if i == 0 or j == 0 or i == Ngrid-1 or j == Ngrid-1:
                phi_new[i][j] = 0
            else:
                phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1]+Q[i][j])/4.0
            
    #plt.pause(0.000000005)
    phi = np.copy(phi_new)
    plt.clf()
    plt.imshow(phi)
Ex,Ey = np.gradient(phi_new)
plt.figure()
plt.quiver(Ey[::5],Ex[::5],scale=1.5)
plt.show()