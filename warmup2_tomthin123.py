import numpy as np 
import matplotlib.pyplot as plt 
#% matplotlib inline for jupyter notebook
N0=100
alpha=1
beta=1
tini=0
tfin=10
Nsteps=10
t=np.linspace(tini,tfin,Nsteps+1)
N=np.zeros(Nsteps+1)
N[0]=N0
dt=(tfin-tini)/Nsteps
for i in range(1,Nsteps+1):
    dN=N[i-1]*alpha-(N[i-1]**2)*beta
    N[i]=N[i-1]+dN*dt
    print(N[i],dt)
plt.plot(t,N)
#plt.plot(t,N0*np.exp(-t/tau),'y-')
plt.xlabel('time')
plt.ylabel('number of specimen')  
plt.show()  