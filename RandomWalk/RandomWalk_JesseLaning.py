import numpy as np
import math
import numpy.random as random
import matplotlib.pyplot as plt

n_experiments = 1000

def random_walk(steps, experiments, p=[0.5, 0.5]):
	sum = 0
	for i in range(experiments):
		sum += np.abs(np.sum(random.choice([-1, 1], steps, p=p)))
	return sum / experiments

def random_walk_3d_grid(steps, experiments, p=[0.5, 0.5]):
	sum = 0
	for i in range(experiments):
		coordinates = [0, 0, 0]
		for i in range(steps):
			coordinates[random.randint(3)] += random.choice([-1, 1], p=p)
		sum += np.linalg.norm(coordinates)
	return sum / experiments

def random_walk_3d_random(steps, experiments):
	sum = 0
	for i in range(experiments):
		coordinates = np.random.randn(3, steps)
		coordinates /= np.linalg.norm(coordinates, axis=0)
		sum += np.linalg.norm(np.sum(coordinates, axis=1))
	return sum / experiments

steps = range(1, 101)
avgs_50_50 = np.zeros(len(steps))
avgs_75_25 = np.zeros(len(steps))
avgs_3D_grid = np.zeros(len(steps))
avgs_3D_random = np.zeros(len(steps))

for i in steps:
	avgs_50_50[i - 1] = random_walk(i, n_experiments)
	avgs_75_25[i - 1] = random_walk(i, n_experiments, p=[0.75, 0.25])
	avgs_3D_grid[i - 1] = random_walk_3d_grid(i, n_experiments)
	avgs_3D_random[i - 1] = random_walk_3d_random(i, n_experiments)

plt.plot(steps, avgs_50_50, label="50/50")
plt.plot(steps, avgs_75_25, label="75/25")
plt.plot(steps, avgs_3D_grid, label="3D Grid")
plt.plot(steps, avgs_3D_random, label="3D Random")
plt.legend(ncol=1)

plt.show()