import math
import numpy as np
import matplotlib.pyplot as plt

pi = math.pi
g = -9.8

#1
v0 = 0
angle = 45
a0 = angle * pi / 180
m = 1
L = 1

dt = 1 / 100000
run_time = 5
n_steps = int(run_time / dt)

# F = m*g*sin(a)
# g * sin(a) = a = (d^2)l/(dt^2)
# (d^2)a/(dt^2) = g/L * sin(a)
# da/dt * L = dl/dt

a = a0
dda = g/L * math.sin(a)
da = dda * dt + v0 / L
sa = a0 # small angle alpha

# xs = []
# ys = []
# sxs = []
# sys = []
t = []
al = []
sal = []

for i in range(n_steps):
	a += da * dt
	da += dda * dt
	dda = g/L * math.sin(a)
	
	# xs.append(L * math.sin(a))
	# ys.append(L - L * math.cos(a))
	# sxs.append(L * math.sin(a0 * math.cos(math.sqrt(-g/L) * dt * i)))
	# sys.append(L - L * math.cos(a0 * math.cos(math.sqrt(-g/L) * dt * i)))
	al.append(a * 180 / pi)
	sal.append(a0 * math.cos(math.sqrt(-g/L) * dt * i) * 180 / pi)
	t.append(dt * i)


period_dt = 0
period_sa = 0

for i in range(1, len(al) - 1):
	if al[i - 1] < al[i] and al[i + 1] < al[i]:
		period_dt = t[i]
		break

for i in range(1, len(sal) - 1):
	if sal[i - 1] < sal[i] and sal[i + 1] < sal[i]:
		period_sa = t[i]
		break

# plt.plot(t, xs, label="x (dt)")
# plt.plot(t, ys, label="height off ground (dt)")
# plt.plot(t, sxs, label="x (small angle)")
# plt.plot(t, sys, label="height off ground (small angle)")
# leg = plt.legend(ncol=2)
# plt.xlabel("time")
# plt.ylabel("displacement")
# plt.title("a0=" + str(angle) + " deg")
# plt.show()
plt.plot(t, al, label="a (dt) T=" + str(period_dt))
plt.plot(t, sal, label="a (small angle) T=" + str(period_sa))
leg = plt.legend(ncol=1)
plt.xlabel("time")
plt.ylabel("a (deg)")
plt.title("a0=" + str(angle) + " deg")
plt.grid(color='k', linestyle='-', linewidth=1)
plt.show()

#2
v0 = 0
angle = 5
a0 = angle * pi / 180
m = 1
L = 1

dt = 1 / 100000
run_time = 15
n_steps = int(run_time / dt)

# F = m*g*sin(a)
# g * sin(a) = a = (d^2)l/(dt^2)
# (d^2)a/(dt^2) = g/L * sin(a) - q * da/dt
# da/dt * L = dl/dt

def diff_q(q):
	a = a0
	dda = g/L * math.sin(a)
	da = dda * dt + v0 / L

	t = []
	al = []

	for i in range(n_steps):
		a += da * dt
		da += dda * dt
		dda = g/L * math.sin(a) - q * da
		
		al.append(a * 180 / pi)
		t.append(dt * i)


	plt.plot(t, al, label="q=" + str(q))

for i in range(1, 6):
	diff_q(i)

plt.axhline(y=0, color='k')
plt.xlabel("time")
plt.ylabel("a (deg)")
plt.title("a0=" + str(angle) + " deg")
plt.legend(ncol=1)
plt.show()

#3
v0 = 0
angle = 5
a0 = angle * pi / 180
m = 1
L = 1

dt = 1 / 100000
run_time = 25
n_steps = int(run_time / dt)

# F = m*g*sin(a)
# g * sin(a) = a = (d^2)l/(dt^2)
# (d^2)a/(dt^2) = g/L * sin(a) - q * da/dt + F_ext
# da/dt * L = dl/dt

f_max = 1

def diff_omega(omega):
	a = a0
	dda = g/L * math.sin(a)
	da = dda * dt + v0 / L

	t = []
	al = []

	q = 0

	def f_ext(t):
		return f_max * math.sin(omega * t)

	for i in range(n_steps):
		a += da * dt
		da += dda * dt
		dda = g/L * math.sin(a) - q * da + f_ext(dt * i)
		
		al.append(a * 180 / pi)
		t.append(dt * i)

	plt.plot(t, al, label="omega=" + str(omega))

diff_omega(math.sqrt(-g/L))

for j in range(0, 6, 2):
	diff_omega(j)

plt.axhline(y=0, color='k')
plt.xlabel("time")
plt.ylabel("a (deg)")
plt.title("a0=" + str(angle) + " deg | f_max=" + str(f_max))
plt.legend(ncol=2)
plt.show()