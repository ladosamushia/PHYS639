import numpy as np 
import matplotlib.pyplot as plt 
#% matplotlib inline for jupyter notebook
N0=10
tau=703.8
tini=0
tfin=10*tau
Nsteps=1000
t=np.linspace(tini,tfin,Nsteps+1)
N=np.zeros(Nsteps+1)
N[0]=N0
dt=(tfin-tini)/Nsteps
for i in range(1,Nsteps):
    dN=-N[i-1]/tau
    N[i]=N[i-1]+dN*dt
plt.plot(t,N,'go')
plt.plot(t,N0*np.exp(-t/tau),'y-')
plt.xlabel('time')
plt.ylabel('Number of atoms')  
plt.show()  
#here we can see that the particles are being decayed exponentially as expectd from the analytical 
#solution
