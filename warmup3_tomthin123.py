import numpy as np 
import matplotlib.pyplot as plt 
#% matplotlib inline for jupyter notebook
N10=10#initial value for isotope-A
N20=5#initial value for isotope-B
ta=7#halflife for isotope-A
tb=3#halflife for isotope-B
tini=0#initial time
tfin=10#final time
Nsteps=1000
t=np.linspace(tini,tfin,Nsteps+1)#time array
N1=np.zeros(Nsteps+1)#number(solution) of atom isotope-A 
N2=np.zeros(Nsteps+1)#number(solution) of atom isotope-B
N1[0]=N10
N2[0]=N20
dt=(tfin-tini)/Nsteps#stepsize for marching
for i in range(1,Nsteps):
    dN1=-N1[i-1]/ta
    dN2=(N1[i-1]/ta)-(N2[i-1]/tb)
    N1[i]=N1[i-1]+dN1*dt
    N2[i]=N2[i-1]+dN2*dt
plt.plot(t[0:len(t)-1],N1[0:len(N1)-1])#getting rid of one extra point
plt.plot(t[0:len(t)-1],N2[0:len(N2)-1])#getting rid of one extra point
plt.xlabel('time')
plt.ylabel('Number of atoms')  
plt.show()  
#solution for NA is decreasing exponentially as expected from analytical solution and NB also 
#decreses as expected because it is NB' is linearly dependent on -NB and NA which is also decreasing. 