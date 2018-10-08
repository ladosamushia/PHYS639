#James Corona
#Diffusion
#PHYS 639

import numpy as np
import matplotlib.pyplot as plt

#Given the number of steps I am currently using, the code may take a couple
#minutes to run.

##############################################################################

#Problem: Cream in Coffee

N = 400
L = 200
steps = 3E6
plot = 1E6

x = [L / 2] * N
y = [L / 2] * N

for i in range(int(steps)):
    p = np.random.randint(N)
    move = np.random.randint(4)
    if move == 0 and x[p] > 0:
        x[p] -= 1
    elif move == 1 and x[p] < L:
        x[p] += 1
    elif move == 2 and y[p] > 0:
        y[p] -= 1
    elif move == 3 and y[p] < L:
        y[p] += 1
    if (i + 1) % int(plot) == 0:
        plt.figure()
        plt.title('Cream in Coffee: Steps = %.2E' %(i + 1))
        plt.plot(x, y, '.')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.xlim(0, L)
        plt.ylim(0, L)

#'plot' determines how often to plot the distribution, based on the number of
#steps taken.

##############################################################################

#Problem: Hole in the Box 1

N = 400
L = 200
steps = 5E6
hole = 40

x = [L / 2] * N
y = [L / 2] * N
Nlist = [N]
Ncurrent = N

for i in range(int(steps)):
    p = np.random.randint(N)
    move = np.random.randint(4)
    if move == 0 and x[p] > 0:
        x[p] -= 1
    elif move == 1 and x[p] < L:
        x[p] += 1
    elif move == 2 and y[p] > 0:
        y[p] -= 1
    elif move == 3 and y[p] < L:
        y[p] += 1
    if x[p] == 0 and (L - hole) / 2 <= y[p] <= (L + hole) / 2:
        x[p] = 1E10
        Ncurrent -= 1
    Nlist.append(Ncurrent)

plt.figure()
plt.title('Hole in the Box 1')
plt.plot(range(int(steps + 1)), Nlist, 'r')
plt.xlabel('Number of Steps')
plt.ylabel('Number of Particles in Box')

#When a particle lands on the hole, it is essentially sent off to infinity.
#The program continues to simulate the particles not in the box. Otherwise,
#the particles in the box would start to move faster as their numbers declined.
#So, Number of Steps is directly proportional to time.

##############################################################################

#Problem: Hole in the Box 2

N = 400
L = 200
steps = 5E6
hole = 40
experiments = 10

Nlists = []
Navg =[]

for i in range(int(experiments)):
    
    x = [L / 2] * N
    y = [L / 2] * N
    Nlist = [N]
    Ncurrent = N
    
    for j in range(int(steps)):
        p = np.random.randint(N)
        move = np.random.randint(4)
        if move == 0 and x[p] > 0:
            x[p] -= 1
        elif move == 1 and x[p] < L:
            x[p] += 1
        elif move == 2 and y[p] > 0:
            y[p] -= 1
        elif move == 3 and y[p] < L:
            y[p] += 1
        if x[p] == 0 and (L - hole) / 2 <= y[p] <= (L + hole) / 2:
            x[p] = 1E10
            Ncurrent -= 1
        Nlist.append(Ncurrent)
        
    Nlists.append(Nlist)

for i in range(int(steps + 1)):
    ilist = []
    for j in Nlists:
        ilist.append(j[i])
    iavg = np.mean(ilist)
    Navg.append(iavg)

plt.figure()
plt.title('Hole in the Box 2')
plt.plot(range(int(steps + 1)), Navg, 'g')
plt.xlabel('Number of Steps')
plt.ylabel('Number of Particles in Box')

#As expected, the result is very similar to the previous problem. However,
#since the plot is of an average, it is smoother.

##############################################################################