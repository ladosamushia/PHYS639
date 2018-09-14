import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

#Problem 1 is commented out

#1) Uranium-235 decay
#2) Population Growth
#initalial Condidtions
N0 = 100
#tau = 703.8
tau = 1
alpha = 10
beta = .2
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
   
plt.figure()
plt.plot(t,N,'go')
#plt.plot(t,N0*np.exp(-t/tau),"yz")
plt.xlabel('Time')
plt.ylabel('Number of Entries')

#In Problem 1, the graph represents the the half-life decay of Uranium-235
#In Problem 2, alpha and beta represent the birth and death rates of a population
#as aplph(birth rate) increases, the value that the decay approaches raises
#as beta(death rate)increases, the time that the decay takes decreases
#*****************************************
#initial Conditions

tfin = 100
tini = 0
Nsteps = 10000

#Inital for radioactive decay 1
#tauA = 10
#tauB = 20
#Nao = 100
#Nbo = 200
#Inital for radioactive decay 2
tauA = 20
tauB = 50
Nao = 100
Nbo = 50

t = np.linspace(tini, tfin, Nsteps + 1)
Na = np.zeros(Nsteps + 1)
Nb = np.zeros(Nsteps + 1)
Na[0] = Nao
Nb[0] = Nbo
dt = (tfin - tini) / Nsteps

for i in range(1,Nsteps+1):
    #for radioactive decay 1
    #dNa = -Na[i-1]/tauA
    
    #for radioactive decay 2
    dNa = Nb[i-1]/tauB-Na[i-1]/tauA
    
    dNb = Na[i-1]/tauA-Nb[i-1]/tauB
    Na[i] = Na[i-1]+dNa*dt
    Nb[i] = Nb[i-1]+dNb*dt

plt.figure()
plt.plot(t,Na,'r-')
plt.plot(t,Nb,'b-')
plt.title('Radioactive Decay')
plt.xlabel('Time')
plt.ylabel('Number of Entries')

#In the 
