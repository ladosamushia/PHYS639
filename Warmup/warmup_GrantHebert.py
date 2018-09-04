#Problem 1: Radioactive Decay (U-235)

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Parameters
N0 = 10 # Initial U-235 Sample (as a function of Avogadro's number)
tau = 703.8 # Half-life of U-235
tini = 0 # Initial time
tfin = 10*tau # Final time
Nsteps = 10000 # Number of steps taken between tini and tfin

# Functions
t = np.linspace(tini, tfin, Nsteps+1)
N = np.zeros(Nsteps+1)
N[0] = N0
dt = (tfin - tini)/Nsteps


for i in range(1,Nsteps+1):
	dN = -N[i-1]/tau
	N[i]= N[i-1] + dN*dt
	
	
# Plots
plt.plot(t,N,'go')
plt.plot(t,N0*np.exp(-t/tau),'y-')
plt.xlabel('time in millions years')
plt.ylabel('Number of atoms in N_A')

# As can be observed by the graph the program produces a plot that fits the expected decay of U-235







#Problem 2: Population Growth

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Parameters
N0 = 1 # Initial population
alpha = 1.02
beta = .04
tini = 0.0 # Initial time
tfin = 100.0 # Final time
Nsteps = 100000 # Number of steps taken betwen tini and tfin

# Functions
t = np.linspace(tini, tfin, Nsteps+1)
N = np.zeros(Nsteps+1)
N[0] = N0
dt = (tfin - tini)/Nsteps


for i in range(1,Nsteps+1):
    dN = alpha*N[i-1]-beta*(N[i-1])**2
    N[i]= N[i-1] + dN*dt

	
# Plot(s)
plt.plot(t,N,'go')
plt.xlabel('time in years')
plt.ylabel('population')

#As the graph shows, the population will reach a stability point when alpha*N = beta*(N**2)