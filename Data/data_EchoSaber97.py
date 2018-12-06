#James Corona
#Data Analysis
#PHYS 639

import numpy as np
import matplotlib.pyplot as plt

##############################################################################

#Problem: Best-Fit Values

steps = 100

data = np.loadtxt('DataAnalysis.txt')

Ein= data[:,0]
Nin = data[:,1]
Ndel = data[:,2]

ki2 = np.zeros((steps, steps))
E0 = np.linspace(0, 20, steps)

for i in range(steps):
    A = np.linspace(0, 1, steps)
    for j in range(steps):
        N_th = 1 + A[j] * np.exp(-(Ein - E0[i]) ** 2)
        ki2[i][j] = np.sum((N_th - Nin) ** 2 / Ndel ** 2)

imin, jmin = np.where(ki2 == np.min(ki2))

E0min = E0[imin[0]]
Amin = A[jmin[0]]
ki2min = np.min(ki2)
Nmin = 1 + Amin * np.exp(-(Ein - E0min) ** 2)

plt.errorbar(Ein, Nin, Ndel, fmt = 'o')
plt.plot(Ein, Nmin)
plt.xlabel('Energy')
plt.ylabel('Number of Photons')
plt.show()

print('A =', Amin)
print('E0 =', E0min)
print('ki2 =', ki2min)

##############################################################################

#Problem: Error-Bars

dada=(ki2[imin, jmin + 1] + ki2[imin, jmin - 1] - 2 * ki2[imin, jmin]) / (A[jmin + 1] - A[jmin])
dede=(ki2[imin + 1, jmin] + ki2[imin - 1, jmin] - 2 * ki2[imin, jmin]) / (E0[imin + 1] - E0[imin])
dade=(ki2[imin - 1, jmin - 1] + ki2[imin + 1, jmin + 1] - ki2[imin - 1, jmin + 1] - ki2[imin + 1, jmin - 1]) \
/ (4 * (A[jmin + 1] - A[jmin]) * (E0[imin + 1] - E0[imin]))

Hess=np.zeros((2,2))
Hess[0][0], Hess[0][1], Hess[1][0], Hess[1][1] = dada / 2, dade / 2, dade / 2, dede / 2

C = np.linalg.inv(Hess)
sigmas = np.sqrt(C.diagonal())

print('\nError:', sigmas)

##############################################################################