#created by Parker Stoops
#
#
#201x201 grid with the intial particle being at the center
#


import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

part=400 # number of particles
grid=151
steps=10000000
x=np.zeros(part)
y=np.zeros(part)

partsnbox = []
a=0
for i in range(steps):
    if i == 0:
        plt.figure(0)
        plt.plot(x,y,'.')
        plt.axis([-75,75,-75,75])
    part_sel= random.randint(part)
    direction = random.randint(4)
    if part_sel not in x2:
        if direction == 0 and x[part_sel] >= -grid/2:
            x[part_sel] -=1
        if direction == 1 and x[part_sel] <= grid/2:
            x[part_sel] +=1
        if direction == 2 and y[part_sel] >= -grid/2:
            y[part_sel] -=1
        if direction == 3 and y[part_sel] <= grid/2:
            y[part_sel] +=1
        if x[part_sel] <= -grid/2 and direction == 0 and y[part_sel] >= -20 and y[part_sel] <= 20:
            x[part_sel] -=1
    if i%2000000==0:
        plt.figure((i/2000000)+1)
        plt.plot(x,y,'.')
        plt.axis([-75,75,-75,75])
    if x[part_sel] < -grid/2:
        x2.append(part_sel)
        x[part_sel]=None
        a+=1
    partsnbox.append(part - a)


plt.figure(6)
plt.plot(partsnbox,'.')
plt.axis([0,steps,0,part])

