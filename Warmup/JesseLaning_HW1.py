# 1
# dN/dt = N/tau

import math
import matplotlib.pyplot as plt

n_steps = 10000
n0 = 10
tau = 703.8
dt = tau * 10 / n_steps

def derivative(n):
	return -n/tau
	
n = n0
vals = []
vals.append(n)

for i in range(n_steps):
	n = n + derivative(n) * dt
	vals.append(n)

x = []
for v in range(len(vals)):
	x.append(v * dt)

plt.plot(x, vals)
plt.show()

# 2# dN/dt = aN-bN^2

import math
import matplotlib.pyplot as plt

n_steps = 10000
n0 = 10
dt = 1 / n_steps

def diff_ab(a, b):
	x = []
	y = []
	
	def derivative(n):
		return a * n - b * n * n
	
	n = n0
	y.append(n)
	
	for i in range(n_steps):
		n = n + derivative(n) * dt
		y.append(n)
	
	for v in range(len(y)):
		x.append(v * dt)
	
	return x, y

	
for i in range(1, 16, 5):
	for j in range(1, 16, 5):
		plot = diff_ab(i, j)
		plt.plot(plot[0], plot[1])
		
plt.show()

# 3
import math
import matplotlib.pyplot as plt

def diff_tau(ta, tb):
	n0a = 10
	n0b = 20
	num_steps = 10000
	max = 15
	dta = max / num_steps
	dtb = max / num_steps

	na = n0a
	nb = n0b

	na_vals = [na]
	nb_vals = [nb]

	xa = [0]
	xb = [0]

	def dna(na, nb):
		return -na / ta

	def dnb(na, nb):
		return (na / ta) - (nb / tb)


	for i in range(num_steps):
		xa.append((i + 1) * dta)
		xb.append((i + 1) * dtb)
		old_na = na
		na = na + dna(na, nb) * dta
		nb = nb + dnb(old_na, nb) * dtb
		na_vals.append(na)
		nb_vals.append(nb)
		
	return xa, na_vals, xb, nb_vals

for i in range(1, 16, 5):
	for j in range(1, 16, 5):
		plot = diff_tau(i, j)
		plt.plot(plot[0], plot[1], '--')
		plt.plot(plot[2], plot[3])
		
plt.show()


# 4
import math
import matplotlib.pyplot as plt

n0a = 10
n0b = 20
num_steps = 10000
max = 15
dta = max / num_steps
dtb = max / num_steps
tau = 3

na = n0a
nb = n0b

na_vals = [na]
nb_vals = [nb]

xa = [0]
xb = [0]

def dna(na, nb):
	return (nb - na) / tau

def dnb(na, nb):
	return (na - nb) / tau


for i in range(num_steps):
	xa.append((i + 1) * dta)
	xb.append((i + 1) * dtb)
	old_na = na
	na = na + dna(na, nb) * dta
	nb = nb + dnb(old_na, nb) * dtb
	na_vals.append(na)
	nb_vals.append(nb)

plt.plot(xa, na_vals)
plt.plot(xb, nb_vals)
plt.show()