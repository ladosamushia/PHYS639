#James Corona
#Projectile Motion
#PHYS 639

import numpy as np

##############################################################################

#Problem: Simple Projectile Motion

x = 0
y = 0
vx = 1000
vy = 1000
g = -9.81
t = 0
dt = 0.001

while y > 0 or t == 0:
    x += vx * dt
    y += vy * dt
    vy += g * dt
    t += dt

print('Simple Projectile Motion')
print('Distance: %.2f' %(x))
print()

#As expected, the distance the projectile travels in this problem will be
#significantly greater than the other distances.

##############################################################################

#Problem: Air Resistance

x = 0
y = 0
vx = 1000
vy = 1000
g = -9.81
t = 0
dt = 0.001

def airx(vx, vy):
    return -0.00004 * vx * np.sqrt(vx ** 2 + vy ** 2)

def airy(vx, vy):
    return -0.00004 * vy * np.sqrt(vx ** 2 + vy ** 2)

while y > 0 or t == 0:
    x += vx * dt
    y += vy * dt
    vx += airx(vx, vy) * dt
    vy += (g + airy(vx, vy)) * dt
    t += dt

print('Air Resistance')
print('Distance: %.2f' %(x))
print()

#As expected, the distance the projectile travels in this problem will be
#less than the other distances.

##############################################################################

#Problem: Changing Air Resistance

x = 0
y = 0
vx = 1000
vy = 1000
g = -9.81
t = 0
dt = 0.001

def airx(vx, vy, y):
    return -0.00004 * vx * np.sqrt(vx ** 2 + vy ** 2) * (1 - 2.2E-5 * y) ** (5 / 2)

def airy(vx, vy, y):
    return -0.00004 * vy * np.sqrt(vx ** 2 + vy ** 2) * (1 - 2.2E-5 * y) ** (5 / 2)

while y > 0 or t == 0:
    x += vx * dt
    y += vy * dt
    vx += airx(vx, vy, y) * dt
    vy += (g + airy(vx, vy, y)) * dt
    t += dt

print('Changing Air Resistance')
print('Distance: %.2f' %(x))
print()

#Due to the lessening of air resistance with altitude, the distance will be
#greater than in the previous problem.

##############################################################################

#Problem: Changing Gravity

x = 0
y = 0
vx = 1000
vy = 1000
t = 0
dt = 0.001

def airx(vx, vy, y):
    return -0.00004 * vx * np.sqrt(vx ** 2 + vy ** 2) * (1 - 2.2E-5 * y) ** (5 / 2)

def airy(vx, vy, y):
    return -0.00004 * vy * np.sqrt(vx ** 2 + vy ** 2) * (1 - 2.2E-5 * y) ** (5 / 2)

def g(y):
    return -(6.67408E-11) * (5.972E24) / ((y + 6.3781E6) ** 2)

while y > 0 or t == 0:
    x += vx * dt
    y += vy * dt
    vx += airx(vx, vy, y) * dt
    vy += (g(y) + airy(vx, vy, y)) * dt
    t += dt

print('Changing Gravity')
print('Distance: %.2f' %(x))
print()

#Due to the lessening of the gravitational force with altitude, the distance
#will be slightly greater than in the previous problem.

##############################################################################

#Problem: "Battleship"

shipx = 5
shipy = 10
radius = 0.1
dt = 0.01
dtheta = 0.1
dv = 0.1
hit = False
v = 0

def airx(vx, vy, y):
    return -0.00004 * vx * np.sqrt(vx ** 2 + vy ** 2) * (1 - 2.2E-5 * y) ** (5 / 2)

def airy(vx, vy, y):
    return -0.00004 * vy * np.sqrt(vx ** 2 + vy ** 2) * (1 - 2.2E-5 * y) ** (5 / 2)

def g(y):
    return -(6.67408E-11) * (5.972E24) / ((y + 6.3781E6) ** 2)

while hit == False:
    theta = 0
    while theta < (np.pi / 2):
        x = 0
        y = 0
        t = 0
        vx = v * np.cos(theta)
        vy = v * np.sin(theta)
        while y > 0 or t == 0:
            x += vx * dt
            y += vy * dt
            vx += airx(vx, vy, y) * dt
            vy += (g(y) + airy(vx, vy, y)) * dt
            t += dt
            if np.sqrt((x - shipx) ** 2 + (y - shipy) ** 2) <= radius:
                hit = True
            if hit == True:
                break
        if hit == True:
            break
        theta += dtheta
    if hit == True:
        break
    v += dv

print('"Battleship"')
print('Speed: %.1f Angle: %.1f' %(v, theta))
print()

#In order to find the minumum initial velocity needed to reach the target, I
#start at v = 0 and increase by dv. For each v, I test with many angles
#from 0 to 90 degrees. If the projectile ever comes within a radius of the
#target, the loops are broken and the most recent initial velocity and angle
#are printed. Also, I set the origin at the canon for convenience.

##############################################################################