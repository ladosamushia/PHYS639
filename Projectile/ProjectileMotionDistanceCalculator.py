# ProjectileMotionDistanceCalculator.py
# Author: Michael Crisp
# Date 4 November 2018
# Description: A simple program to calculate how far a projectile will fly
#              before hitting the ground, ignoring all dissipating forces besides
#              gravity. 

import numpy as np
import matplotlib.pyplot as plt

#Initial conditions
x_0 = 0
y_0 = 0
v_0 = 255 
a = -9.8
m = 10
launchAngle = np.pi/6

#For Euler approximation
steps = 10000000
t_0 = 0
t_f = 10000
dt = (t_0 + t_f) / steps

#initial velocities componentized
vx_0 = v_0 * np.cos(launchAngle)
vy_0 = v_0 * np.sin(launchAngle)


#these will contain the velocities and positions as they change in time
x_vels = [vx_0]
y_vels = [vy_0]
x_pos = [x_0]
y_pos = [y_0]

while y_0 >= 0:
   
    x_vels.append(vx_0) #gravity contributes nothing
    vy_0 += a*dt
    y_vels.append(vy_0)
   
    x_0 += vx_0*dt
    y_0 += vy_0*dt
    x_pos.append(x_0)
    y_pos.append(y_0)
    

#Plots to represent projectile motion.
plt.plot(x_pos, y_pos)
plt.xlabel('X-Distance (m)')
plt.ylabel('Y-Distance (m)')

#Explicitly revealing calculations.
print('Object travels', np.max(x_pos), 'meters.')
print('Object reaches maximum height of', np.max(y_pos), 'meters.')    
