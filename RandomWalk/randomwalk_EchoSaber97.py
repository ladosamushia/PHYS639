#James Corona
#Random Walk
#PHYS 639

import numpy as np
import matplotlib.pyplot as plt

##############################################################################

#Problem: 1D Random Walk

Nsteps = 100
trials = 1000

def AvgDist(steps, trials):
    mod = []
    for i in range(trials):
        x = 0
        for j in range(steps):
            x += np.random.choice([1, -1])
        mod.append(np.abs(x))
    return np.mean(mod)

dist = []

for steps in range(Nsteps):
    dist.append(AvgDist(steps, trials))

plt.figure()
plt.title('1D Random Walk')
plt.xlabel('Number of Steps')
plt.ylabel('Average Distance')
plt.plot(range(Nsteps), dist, 'b')

#Since there is an equal probability that the particle moves left or right, it
#would be reasonable to suspect that the average distance as a function of the
#number of steps increases slowly. The graph supports this idea.

##############################################################################

#Problem: 1D Biased Random Walk

Nsteps = 100
trials = 1000

def AvgDist(steps, trials):
    mod = []
    for i in range(trials):
        x = 0
        for j in range(steps):
            x += np.random.choice([1, -1, -1, -1])
        mod.append(np.abs(x))
    return np.mean(mod)

dist = []

for steps in range(Nsteps):
    dist.append(AvgDist(steps, trials))

plt.figure()
plt.title('1D Biased Random Walk')
plt.xlabel('Number of Steps')
plt.ylabel('Average Distance')
plt.plot(range(Nsteps), dist, 'r')

#On average, the particle moves to the left on 3/4 of the steps and to the
#right on 1/4 of the steps. So, if the particle moves 4 steps, the expected
#value of abs(x) = 2. In general, the expected value of abs(x) = steps / 2.

##############################################################################

#Problem: 3D Random Walk

Nsteps = 100
trials = 1000

def AvgDist(steps, trials):
    mod = []
    for i in range(trials):
        x, y, z = (0, 0, 0)
        for j in range(steps):
            direction = np.random.choice(range(6))
            if direction == 0:
                x += 1
            elif direction == 1:
                x -= 1
            elif direction == 2:
                y += 1
            elif direction == 3:
                y -= 1
            elif direction == 4:
                z += 1
            else:
                z -= 1
        mod.append(np.sqrt(x ** 2 + y ** 2 + z ** 2))
    return np.mean(mod)

dist = []

for steps in range(Nsteps):
    dist.append(AvgDist(steps, trials))

plt.figure()
plt.title('3D Random Walk')
plt.xlabel('Number of Steps')
plt.ylabel('Average Distance')
plt.plot(range(Nsteps), dist, 'g')

#The graph is smoother and increases slightly faster than in the 1D case.
#Otherwise, the 1D case and 3D case appear the same.

##############################################################################