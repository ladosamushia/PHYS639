import numpy as np
import math
import numpy.random as random
import matplotlib.pyplot as plt
import scipy

grid = [100, 100]
hgrid = [grid[0] / 2, grid[1] / 2]

maxx = hgrid[0]
maxy = hgrid[1]
minx = -maxx
miny = -maxy

def addv(v1, v2):
	return [sum(x) for x in zip(v1, v2)]

def inGrid(pos):
	return pos[0] >= minx and pos[0] <= maxx and pos[1] >= miny and pos[1] <= maxy

def throughHole(pos):
	return pos[0] < minx and abs(pos[1]) <= 20

def calc_entropy(v, n_particles):
	s = 0
	for a in v:
		if a > 0:
			p = a / n_particles
			s += p * math.log(p)
	return -s

def diffuse(n_steps, dead=False, entropy=False):
	n_particles = 400
	n_steps = n_steps
	particles = np.zeros((n_particles, 2))
	dead_particles = []
	count = []
	s = []
	
	c = 100

	for i in range(n_steps):
		coordinates = np.random.randn(2)
		coordinates /= np.linalg.norm(coordinates, axis=0)
		particle = random.randint(n_particles)
		new_pos = addv(particles[particle], list(coordinates))
		if inGrid(new_pos):
			particles[particle] = new_pos
		
		if entropy:
			if not dead:
				h2d = np.ndarray.flatten(np.histogram2d(*zip(*particles), bins=(10, 10))[0])
				s.append(calc_entropy(h2d, n_particles))
		else:
			if dead:
				if particle not in dead_particles:
					if throughHole(new_pos):
						dead_particles.append(particle)
				count.append(n_particles - len(dead_particles))
			else:
				if (i + 1) % c == 0:
					c *= 10
					plt.scatter(*zip(*particles), marker='.', label="steps=" + str(i + 1), zorder=(n_steps - i)/n_steps)
	
	if entropy:
		if not dead:
			return s
	else:
		if dead:
			return count

n_steps = 10**8 # 10**8 takes forever but produces good results
n_experiments = 50

diffuse(n_steps)

plt.title("particles over time")
plt.ylabel("y")
plt.xlabel("x")
plt.legend(ncol=1)
plt.axis([minx, maxx, miny, maxy])
plt.show()

plt.title("n particles in box")
plt.ylabel("n particles")
plt.xlabel("time")
plt.plot(diffuse(n_steps, True))
plt.show()

counts = np.zeros(n_steps)
for i in range(n_experiments):
	d = diffuse(n_steps, True)
	for j in range(len(d)):
		counts[j] += d[j] / n_experiments

plt.plot(counts)
plt.title("avg n particles in box")
plt.ylabel("avg n particles")
plt.xlabel("time")
plt.show()

plt.plot(diffuse(n_steps, entropy=True))
plt.title("entropy vs time")
plt.ylabel("entropy")
plt.xlabel("time")
plt.show()

s_counts = np.zeros(n_steps)
for i in range(n_experiments):
	s = diffuse(n_steps, entropy=True)
	for j in range(len(s)):
		s_counts[j] += s[j] / n_experiments

plt.plot(s_counts)
plt.title("avg entropy vs time")
plt.ylabel("avg entropy")
plt.xlabel("time")
plt.show()