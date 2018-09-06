import numpy as np 
import matplotlib.pyplot as plt 
#% matplotlib inline for jupyter notebook
N10=10
N20=5
ta=7
tb=3
tini=0
tfin=10
Nsteps=1000
t=np.linspace(tini,tfin,Nsteps+1)
N1=np.zeros(Nsteps+1)
N2=np.zeros(Nsteps+1)
N1[0]=N10
N2[0]=N20
dt=(tfin-tini)/Nsteps
for i in range(1,Nsteps):
    dN1=(N2[i-1]/tb)-(N1[i-1]/ta)
    dN2=(N1[i-1]/ta)-(N2[i-1]/tb)
    N1[i]=N1[i-1]+dN1*dt
    N2[i]=N2[i-1]+dN2*dt
plt.plot(t[0:len(t)-1],N1[0:len(N1)-1])#getting rid of one extra point
plt.plot(t[0:len(t)-1],N2[0:len(N2)-1])#getting rid of one extra point
plt.xlabel('time')
plt.ylabel('Number of atoms')  
plt.show()  
#here the odes' are coupled hence we see that the as NA increses the NB decreases and vice-versa.
