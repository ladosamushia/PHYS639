# Written By Parker Stoops
#
#Problem 1 Uranium vs. Time 
#Differential Equation dN/dt = -N/(tau)

import numpy as np
import matplotlib.pyplot as plt

N0 = 10
tau = 703.8 #half life
tini = 0 #the intial time
tfin = 10 * tau 

StepsN = 100000


t = np.linspace(tini, tfin, StepsN + 1)
N = np.zeros(StepsN + 1)
N[0] = N0
dt = (tfin - tini) / StepsN
for a in range(1, StepsN + 1):
    dN = - N[a - 1] / tau
    N[a] = N[a - 1] + dN * dt
    
plt.figure(1)
plt.title('Rad Decay')
plt.plot(t, N, 'b-')
plt.plot(t, N0 * np.exp(-t /tau), 'g+')


