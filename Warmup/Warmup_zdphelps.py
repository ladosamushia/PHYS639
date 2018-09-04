import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline #only in jupiter

#Problem 1 is commented out

#initalial Condidtions
N0 = 10
#tau = 703.8
tau = 1
alpha = 2
beta = 2
tini = 0
tfin = 10*tau
Nsteps = 10000

#incrimenting integral
t = np.linspace(tini,tfin,Nsteps+1)
N = np.zeros(Nsteps+1)
N[0] = N0
dt = (tfin - tini)/Nsteps

#Stepping through function
for i in range(1,Nsteps):
   # dN = - N[i-1]/tau
    dN = alpha*N[i-1] - beta*(N[i-1]**2)
    N[i] = N[i-1] + dN*dt

    #Display on Graph
    #was not  able to check plot due to jupyter not responding
plt.plot(t,N,'go')
#plt.plot(t,N0*np.exp(-t/tau),"yz")
plt.xlabel('time')
plt.ylabel('Number of atoms')
