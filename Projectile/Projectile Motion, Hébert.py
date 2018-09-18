import numpy as np
import matplotlib.pyplot as plt
# There are two different attempts at this problem, the first was my initial attempt in which I did achieve a functional parabola. After getting some advice from other in the class
# I did attempt a better version of the code (in which I did produce a parabolic trajectory) however up attempting to add in variable gravity and drag I have managed to mess everything
# up. Particularly with regard to the x positions where for some reason I'm ending up with a slanted parabolic path (see the Problem 1 Redesign graph for what I mean)
#Problem 1: Projectile Motion

# Parameters
x0 = 0 # Initial x-pos in m
y0 = 0 # Initial y-pos in m
theta = np.pi/2 # Inital angle in radians
tini = 0 # Initial time in s
tfin = 110 # Final time in s
g = -9.8 # Gravitational acceleration
mass = 10 # Mass in kg
Nsteps = 1000 # Number of steps between tini and tfin
v0 = 500 # Initial Velocity in m/s

# Functions
vx0 = (v0)*np.cos(theta)
vy0 = (v0)*np.sin(theta)
t = np.linspace(tini, tfin, Nsteps+1)
dt = (tfin-tini)/Nsteps

# Defining Arrays
x = np.zeros(Nsteps+1)
y = np.zeros(Nsteps+1)
vx = np.zeros(Nsteps+1)
vy = np.zeros(Nsteps+1)

# Initial Conditions
x[0] = x0
y[0] = y0
vy[0] = vy0
vx[0] = vx0

for i in range(1, Nsteps+1):
    vy[i] = vy[i-1] + g*dt
    vx[i] = vx[i-1]
    y[i] = y[i-1] + vy[i-1]*dt + 0.5*g*((dt)**2)
    x[i] = x[i-1] + vx[i-1]*dt
    if y[i] < 0:
        break
# Plots
plt.plot(x, y, 'go')
plt.xlabel ( "X Positiion (m)" )
plt.ylabel ( "Y Position (m)" )



import numpy as np
import matplotlib.pyplot as plt

#Problem 1 Redesign: Projectile Motion

def VGravity(Re,y,ay):
    ay = ay*((Re)**2/((Re+y)**2))
    return ay

# Parameters
x = 0.0 # Initial x-pos in m
y = 0.0 # Initial y-pos in m
theta = np.pi/2 # Inital angle in radians
mass = 10.0 # Mass in kg
v = 100.0 # Initial Velocity in m/s
Re = 6371000.0 # Radius of the Earth
ay = -9.8
ax = 0.0
t = 0.0
dt = 0.01

# Functions
vx = (v)*np.cos(theta)
vy = (v)*np.sin(theta)
drag = -0.0004*(vx**2 + vy**2)

# Defining Arrays
xray = np.array([x])
yray = np.array([y])

# Loop
while y >= 0:
    dx = drag*vx/np.sqrt(vx**2 + vy**2)
    dy = drag*vy/np.sqrt(vx**2 + vy**2)
    ax = ax + dx
    ay = ay + dy
    vy = vy + ay*dt
    vx = vx + ax*dt
    y = y + vy*dt
    x = x + vx*dt
    t = t + dt
    xray = np.append(xray,x)
    yray = np.append(yray, y)
print (xray)
    
# Plots
plt.plot(xray, yray, 'go')
plt.xlabel ( "X Positiion (m)" )
plt.ylabel ( "Y Position (m)" )