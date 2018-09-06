#1
import math
import matplotlib.pyplot as plt

n_div = 10000
dt = 1/n_div

v0 = 750
m = 10
g = -9.8
y = 0
x = 0
angle = math.pi / 2.25  # 45 degrees

vx = v0 * math.cos(angle)
vy = v0 * math.sin(angle)

xs1 = [0]
ys1 = [0]
dts1 = [0]

while y >= 0:
	y = y + vy * dt + 0.5 * g * dt * dt
	if y < 0:
		break
	x = x + vx * dt
	vy = vy + g * dt
	xs1.append(x)
	ys1.append(y)
	dts1.append(dts1[-1] + dt)
	
print(x, "m")

plt.plot(xs1, ys1, 'r')
plt.show()

#2
n_div = 10000
dt = 1/n_div

v0 = 750
m = 10
g = -9.8
y = 0
x = 0
angle = math.pi / 2.25  # 45 degrees

vx = v0 * math.cos(angle)
vy = v0 * math.sin(angle)

xs2 = [0]
ys2 = [0]
dts2 = [0]

def drag(v):
	return -0.00004 * v * v / m
	
import time

while y >= 0:
	y = y + vy * dt + 0.5 * (g + drag(vy)) * dt * dt
	if y < 0:
		break
	x = x + vx * dt + 0.5 * drag(vx) * dt * dt
	vx = vx + drag(vx) * dt
	vy = vy + (g + drag(vy)) * dt
	xs2.append(x)
	ys2.append(y)
	dts2.append(dts2[-1] + dt)

print(x, "m")

plt.plot(xs1, ys1, 'r')
plt.plot(xs2, ys2, 'g')
plt.show()

#3
n_div = 10000
dt = 1/n_div

v0 = 750
m = 10
g = -9.8
y = 0
x = 0
angle = math.pi / 2.25  # 45 degrees

vx = v0 * math.cos(angle)
vy = v0 * math.sin(angle)

xs3 = [0]
ys3 = [0]
dts3 = [0]

def drag(v, y):
	return -(1 - 2.2 * 10**(-5) * y)**(5/2)

while y >= 0:
	x = x + vx * dt + 0.5 * drag(vx, y) * dt * dt
	y = y + vy * dt + 0.5 * (g + drag(vy, y)) * dt * dt
	if y < 0:
		break
	vx = vx + drag(vx, y) * dt
	vy = vy + (g + drag(vy, y)) * dt
	xs3.append(x)
	ys3.append(y)
	dts3.append(dts3[-1] + dt)

print(x, "m")

plt.plot(xs1, ys1, 'r')
plt.plot(xs2, ys2, 'g')
plt.plot(xs3, ys3, 'b')
plt.show()

#4
n_div = 10000
dt = 1/n_div

v0 = 750
m = 10
y = 0
x = 0
angle = math.pi / 2.25

vx = v0 * math.cos(angle)
vy = v0 * math.sin(angle)

xs4 = [0]
ys4 = [0]
dts4 = [0]

M = 5.972 * 10**24
G = 6.67 * 10**-11
R = 6371 * 10**3

def drag(v, y):
	return -(1 - 2.2 * 10**(-5) * y)**(5/2)

def gravity(y):
	return -G * M / (R + y)**2

while y >= 0:
	x = x + vx * dt + 0.5 * drag(vx, y) * dt * dt
	y = y + vy * dt + 0.5 * (gravity(y) + drag(vy, y)) * dt * dt
	if y < 0:
		break
	vx = vx + drag(vx, y) * dt
	vy = vy + (gravity(y) + drag(vy, y)) * dt
	xs4.append(x)
	ys4.append(y)
	dts4.append(dts4[-1] + dt)
	
print(x, "m")

plt.plot(xs1, ys1, 'r')
plt.plot(xs2, ys2, 'g')
plt.plot(xs3, ys3, 'b')
plt.plot(xs4, ys4, 'r--')
plt.show()