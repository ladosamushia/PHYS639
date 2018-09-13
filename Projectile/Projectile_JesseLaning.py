#1
import math
import matplotlib.pyplot as plt
import numpy as np

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
	
print(x, "m", "in", dts1[-1], "s")

plt.plot(xs1, ys1, 'r', label="kinematic")
plt.ylabel("height (m)")
plt.xlabel("distance (m)")
leg = plt.legend(ncol=1)
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

print(x, "m", "in", dts2[-1], "s")

plt.plot(xs1, ys1, 'r', label="kinematic")
plt.plot(xs2, ys2, 'g', label="drag")
plt.ylabel("height (m)")
plt.xlabel("distance (m)")
leg = plt.legend(ncol=1)
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
	return (1 - 2.2 * 10**(-5) * y)**(5/2) * -0.00004 * v * v / m

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

print(x, "m", "in", dts3[-1], "s")

plt.plot(xs1, ys1, 'r', label="kinematic")
plt.plot(xs2, ys2, 'g', label="drag")
plt.plot(xs3, ys3, 'b', label="air density")
plt.ylabel("height (m)")
plt.xlabel("distance (m)")
leg = plt.legend(ncol=1)
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
	return (1 - 2.2 * 10**(-5) * y)**(5/2) * -0.00004 * v * v / m

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
	
print(x, "m", "in", dts4[-1], "s")

plt.plot(xs1, ys1, 'r', label="kinematic")
plt.plot(xs2, ys2, 'g', label="drag")
plt.plot(xs3, ys3, 'b', label="air density")
plt.plot(xs4, ys4, 'm', label="gravity")
plt.ylabel("height (m)")
plt.xlabel("distance (m)")
leg = plt.legend(ncol=1)
plt.show()

#5
# this is probably not an optimal way and it takes a while
n_div = 10000
dt = 1/n_div

v0 = 750
m = 10
y = 0
x = 0

xs4 = [0]
ys4 = [0]
dts4 = [0]

M = 5.972 * 10**24
G = 6.67 * 10**-11
R = 6371 * 10**3

target_altitude = 200
target_distance = 10000

def drag(v, y):
	return (1 - 2.2 * 10**(-5) * y)**(5/2) * -0.00004 * v * v / m

def gravity(y):
	return -G * M / (R + y)**2

angles = list(np.linspace(40 * math.pi / 180, 50 * math.pi / 180, 101))

displacement = {}

# find the optimal angle
v0 = math.sqrt(target_distance * 4.9 / math.cos(math.pi / 4)) # the ideal v0 needed to send the projectile the target distance
for angle in angles:
	vx = v0 * math.cos(angle)
	vy = v0 * math.sin(angle)
	x = 0
	y = 0
	while y >= target_altitude or vy > 0:
		x = x + vx * dt + 0.5 * drag(vx, y) * dt * dt
		y = y + vy * dt + 0.5 * (gravity(y) + drag(vy, y)) * dt * dt
		if y < target_altitude and vy < 0:
			break
		vx = vx + drag(vx, y) * dt
		vy = vy + (gravity(y) + drag(vy, y)) * dt
	displacement[angle] = x

out_angle = angles[0]

for i in range(1, len(angles)):
	if displacement[angles[i]] > displacement[out_angle]:
		out_angle = angles[i]

d = displacement[out_angle]

# adjust the v0
while d > target_distance:
	v0 -= 0.1
	vx = v0 * math.cos(out_angle)
	vy = v0 * math.sin(out_angle)
	x = 0
	y = 0
	while y >= target_altitude or vy > 0:
		x = x + vx * dt + 0.5 * drag(vx, y) * dt * dt
		y = y + vy * dt + 0.5 * (gravity(y) + drag(vy, y)) * dt * dt
		if y < target_altitude and vy < 0:
			break
		vx = vx + drag(vx, y) * dt
		vy = vy + (gravity(y) + drag(vy, y)) * dt
	d = x

while d < target_distance:
	v0 += 0.1
	vx = v0 * math.cos(out_angle)
	vy = v0 * math.sin(out_angle)
	x = 0
	y = 0
	while y >= target_altitude or vy > 0:
		x = x + vx * dt + 0.5 * drag(vx, y) * dt * dt
		y = y + vy * dt + 0.5 * (gravity(y) + drag(vy, y)) * dt * dt
		if y < target_altitude and vy < 0:
			break
		vx = vx + drag(vx, y) * dt
		vy = vy + (gravity(y) + drag(vy, y)) * dt
	d = x

print("v0 =", v0)
print("angle =", out_angle * 180 / math.pi)
print("coordinates =", (x, y))