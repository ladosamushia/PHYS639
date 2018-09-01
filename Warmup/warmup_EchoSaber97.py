#James Corona
#Warmup Homework
#PHYS 639

import numpy as np
import matplotlib.pyplot as plt

##############################################################################

#Problem: Radioactive Decay

N0 = 10
tau = 703.8
tini = 0
tfin = 10 * tau
Nsteps = 10000

t = np.linspace(tini, tfin, Nsteps + 1)
N = np.zeros(Nsteps + 1)
N[0] = N0
dt = (tfin - tini) / Nsteps

for i in range(1, Nsteps + 1):
    dN = - N[i - 1] / tau
    N[i] = N[i - 1] + dN * dt

plt.figure()
plt.title('Radioactive Decay')
plt.plot(t, N, 'bo')
plt.plot(t, N0 * np.exp(-t /tau), 'r-')
plt.xlabel('Time')
plt.ylabel('Number of Atoms')

#As seen from the graph, the system behaves exactly as expected. The number of
#atoms approaches zero asymptotically.

##############################################################################

#Problem: Population Growth

N0 = 100
alpha = 1.01
beta = .01
tini = 0
tfin = 100
Nsteps = 10000

t = np.linspace(tini, tfin, Nsteps + 1)
N = np.zeros(Nsteps + 1)
N[0] = N0
dt = (tfin - tini) / Nsteps

for i in range(1, Nsteps + 1):
    dN = alpha * N[i - 1] - beta * N[i - 1] ** 2
    N[i] = N[i - 1] + dN * dt

plt.figure()
plt.title('Population Growth')
plt.plot(t, N, 'r-')
plt.xlabel('Time')
plt.ylabel('Number of Specimen')

#As seen from the graph, the number of specimen changes until it reaches some
#value. This value corresponds to when the rate of life (alpha * N) is equal
#to the rate of death (beta * (N ** 2)).

##############################################################################

#Problem: Coupled Radioactive Decay 1

NA0 = 100
NB0 = 200
tauA = 5
tauB = 15
tini = 0
tfin = 100
Nsteps = 10000

t = np.linspace(tini, tfin, Nsteps + 1)
NA = np.zeros(Nsteps + 1)
NB = np.zeros(Nsteps + 1)
NA[0] = NA0
NB[0] = NB0
dt = (tfin - tini) / Nsteps

for i in range(1, Nsteps + 1):
    dNA = -NA[i - 1] / tauA
    dNB = NA[i - 1] / tauA - NB[i - 1] / tauB
    NA[i] = NA[i - 1] + dNA * dt
    NB[i] = NB[i - 1] + dNB * dt

plt.figure()
plt.title('Coupled Radioactive Decay 1')
plt.plot(t, NA, 'r-')
plt.plot(t, NB, 'b-')
plt.xlabel('Time')
plt.ylabel('Number of Atoms')

#As seen from the graph, A behaves simply as a single element undergoing
#radioactive decay. B decays very similarly to A, but takes longer and even
#increases at first in this particular case due to the large NA0.

##############################################################################

#Problem: Coupled Radioactive Decay 2

NA0 = 100
NB0 = 10
tauA = 10
tauB = 5
tini = 0
tfin = 100
Nsteps = 10000

t = np.linspace(tini, tfin, Nsteps + 1)
NA = np.zeros(Nsteps + 1)
NB = np.zeros(Nsteps + 1)
NA[0] = NA0
NB[0] = NB0
dt = (tfin - tini) / Nsteps

for i in range(1, Nsteps + 1):
    dNA = NB[i - 1] / tauB - NA[i - 1] / tauA
    dNB = NA[i - 1] / tauA - NB[i - 1] / tauB
    NA[i] = NA[i - 1] + dNA * dt
    NB[i] = NB[i - 1] + dNB * dt

plt.figure()
plt.title('Coupled Radioactive Decay 2')
plt.plot(t, NA, 'r-')
plt.plot(t, NB, 'b-')
plt.xlabel('Time')
plt.ylabel('Number of Atoms')

#As seen from the graph, one element will increase and the other will decrease
#until they each reach a particular value. This value corresponds to when the
#rates (NA / tauA) and (NB / tauB) are equal. In a physical sense, the
#elements are losing atoms as fast as they are gaining them.

##############################################################################