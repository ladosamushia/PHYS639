#James Corona
#Final Project
#PHYS 639

import numpy as np

Nparts = 1000
Nshells = 5
R = 10
L = 100

x, y, z = np.zeros(Nparts), np.zeros(Nparts), np.zeros(Nparts)
for i in range(Nparts):
    x[i], y[i], z[i] = np.random.uniform(0, L), np.random.uniform(0, L), np.random.uniform(0, L)

PartsPerShell = np.zeros((Nparts, Nshells))
for i in range(Nparts):
    for j in range(i + 1, Nparts):
        dist = np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2)
        if dist < R:
            index = int(dist * Nshells / R)
            PartsPerShell[i][index] += 1
            PartsPerShell[j][index] += 1
            
AvgParts = np.mean(PartsPerShell, axis = 0)

print(AvgParts)
