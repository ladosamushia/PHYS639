# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:04:57 2018

@author: Blaine Fry
"""
# Phys 639
# model diffusion

"""
Problem: 1D Random Walk (lvl*)
model 1D diffusion for particles with equal likelihood of 
moving 1 space left or 1 space right
"""

import numpy as np
from matplotlib import pyplot as plt

# make a function to model diffusion
# this function will model one particle moving through N_steps iterations
# it can return the partical path, final position, or absolute value of the final position
def diffusion(N_steps,return_what): # to return abs(final position): 'abs_p'; to return final position: 'final position' ; to return path: 'position'
    position = [0]*(N_steps+1)
    r_or_l = [-1,1]
    for i in range(1,N_steps+1):  
        direction = np.random.choice(r_or_l)
        position[i] = position[i-1] + direction
    if return_what is 'position':
        return position
    if return_what is 'final_p':
        return position[N_steps]
    if return_what is 'abs_p':
        return (np.abs(position[N_steps]))
    
# plot some diffusion paths to see if things make sense
plt.figure(1)
plt.title('Figure 1: Simple Diffusion Path')
plt.ylabel('Particle Position (units)')
plt.xlabel('Number of Steps')
for i in range(10):
    plt.plot(diffusion(100,'position'),'.-')
# It makes sense to me; all particles start at position 0,
# then wander around from there.

# do some loop shennanigans to find the average displacement for a range of N_steps
avg_abs_p = [] # each value will be the average (over 1000 trials) absolute final displacement for a certain N_steps
for n in range(100): # make a range of N_steps
    abs_positions = [] # will store the absolute final positions for each trial at this N_steps = n
    for q in range(1000): # do 1000 trials for each N_steps
        abs_positions.append(diffusion(n,'abs_p')) # return the absolute value of the final position
    avg_abs_p.append(np.average(abs_positions))
# plot the stuff...
plt.figure(2)
plt.title('Figure 2: 1D diffusion w/ Equal Probabilities')
plt.plot(avg_abs_p,'m-',label='diffusion')
plt.ylabel('Average Displacement (units)')
plt.xlabel('Number of Steps')
plt.grid(True)
x = np.linspace(0,100,1000)
plt.plot(x,np.sqrt(x),'y-',label='y=$\sqrt{x}$')
plt.legend()
# Interesting! It seems like there's a 1/2 power (or close to it) functionality
# of displacement on number of steps. I wonder if it's different for a range of
# possible step sizes; surely there would be a distribution of particle velocities.
# I might investigate if I have some free time.

# I wonder what the distribution of final positions looks like. I'm guessing
# a bell curve around 0...
final_positions = []
for i in range(1000):
    final_positions.append(diffusion(10,'final_p'))
plt.figure(3)
plt.title('Figure 3: Distribution of Final Positions for 10 Steps')
plt.hist(final_positions)
plt.grid(True)
plt.ylabel('Frequency')
plt.xlabel('Final Position (units)')
# It seems I guessed more or less correctly!

"""
Problem: 1D Biased Random Walk (lvl*)
Same as before, but now the particle is 3 times as likely to move left
"""

# make a function to model diffusion
# this function will model one particle moving through N_steps iterations
# it can return the partical path, final position, or absolute value of the final position
def biased_diffusion(N_steps,return_what): # to return abs(final position): 'abs_p'; to return final position: 'final position' ; to return path: 'position'
    position = [0]*(N_steps+1)
    r_or_l = [-1,-1,-1,1] # 3 times as likely to move left
    for i in range(1,N_steps+1):  
        direction = np.random.choice(r_or_l)
        position[i] = position[i-1] + direction
    if return_what is 'position':
        return position
    if return_what is 'final_p':
        return position[N_steps]
    if return_what is 'abs_p':
        return (np.abs(position[N_steps]))

# plot some diffusion paths to see if things make sense
plt.figure(4)
plt.title('Figure 4: Biased Diffusion Path')
plt.ylabel('Particle Position (units)')
plt.xlabel('Number of Steps')
for i in range(10):
    plt.plot(biased_diffusion(100,'position'),'.-')
# the paths definitely look biased!

# do some loop shennanigans to find the average displacement for a range of N_steps
avg_abs_p = [] # each value will be the average (over 1000 trials) absolute final displacement for a certain N_steps
for n in range(100): # make a range of N_steps
    abs_positions = [] # will store the absolute final positions for each trial at this N_steps = n
    for q in range(1000): # do 1000 trials for each N_steps
        abs_positions.append(biased_diffusion(n,'abs_p')) # return the absolute value of the final position
    avg_abs_p.append(np.average(abs_positions))
plt.figure(5)
plt.title('Figure 5: 1D diffusion w/ Biased Probabilities')
plt.plot(avg_abs_p,'m-',label='diffusion')
plt.ylabel('Average Displacement (units)')
plt.xlabel('Number of Steps')
x = np.linspace(0,100,1000)
plt.plot(x,0.5*x,'y-',label='y=x/2')
plt.grid(True)
plt.legend()
# That's strange! Now it's a linear relationship! I'm guessing the slope has something to do
# with the relative probabilities of going either direction. maybe m = 1/(p(l)-p(r))
# that would be worth checking out too...


# and another histogram...
final_positions_b = []
for i in range(1000):
    final_positions_b.append(biased_diffusion(10,'final_p'))
plt.figure(6)
plt.title('Figure 6: Distribution of Final Positions (Biased) for 10 Steps')
plt.hist(final_positions_b)
plt.grid(True)
plt.ylabel('Frequency')
plt.xlabel('Final Position (units)')
# the center peak is shifted from 0. It's more choppy than the other histogram though.

"""
Problem: 3D Random Walk (lvl**)
the particle has a random chance of moving up, down, left, right, forwards, or backwards.
"""

from mpl_toolkits.mplot3d import Axes3D
# make a function to model 3D diffusion
# this function will model one particle moving through N_steps iterations
# particles start at the origin
# returns a list of 3D coordinates
def grid_diffusion_3D(N_steps): 
    x = [0]*(N_steps+1) # x position: left or right
    y = [0]*(N_steps+1) # y position: forward or back
    z = [0]*(N_steps+1) # z pozition: up or down
    u_d_l_r_f_b = ['up','down','left','right','forward','back']
    for i in range(1,N_steps+1):  
        direction = np.random.choice(u_d_l_r_f_b)
        if direction == 'up':
            x[i] = x[i-1]
            y[i] = y[i-1]
            z[i] = z[i-1] + 1
        if direction == 'down':
            x[i] = x[i-1]
            y[i] = y[i-1]
            z[i] = z[i-1]-1
        if direction == 'left':
            x[i] = x[i-1] - 1
            y[i] = y[i-1]
            z[i] = z[i-1]
        if direction == 'right':
            x[i] = x[i-1] + 1
            y[i] = y[i-1]
            z[i] = z[i-1]
        if direction == 'forward':
            x[i] = x[i-1]
            y[i] = y[i-1] + 1
            z[i] = z[i-1]
        if direction == 'back':
            x[i] = x[i-1]
            y[i] = y[i-1] - 1
            z[i] = z[i-1]
    return x,y,z

# let's plot a couple particles moving only a few steps
fig = plt.figure(7)
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3D Grid Diffusion Model')
ax.set_xlabel('X position')
ax.set_ylabel('Y position')
ax.set_zlabel('Z position')
for i in range(3):
    x_position,y_position,z_position = grid_diffusion_3D(10)
    ax.plot(x_position,y_position,z_position,'.-')
# Cool! Everything seems to be working as planned. The particles never
# moved multiple directions at once, and things seem random.

# let's plot a particle moving through lots of steps
fig = plt.figure(8)
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3D Grid Diffusion Model')
ax.set_xlabel('X position')
ax.set_ylabel('Y position')
ax.set_zlabel('Z position')
for i in range(1):
    x_position,y_position,z_position = grid_diffusion_3D(1000)
    ax.plot(x_position,y_position,z_position,'.-')
# it reminds me of a fractal! I'm not sure what I expected, but it's cool

# figure out the average distance from the origin for each step
store_radial_displacements = []
N_trials = 100
iterations = 1000
for i in range(N_trials):
    x_p,y_p,z_p = grid_diffusion_3D(iterations)
    radial_displacement = [0]*(iterations+1)
    for i in range(1,iterations+1):
        radial_displacement[i] = np.sqrt((x_p[i])*(x_p[i])+(y_p[i])*(y_p[i])+(z_p[i])*(z_p[i]))
    store_radial_displacements.append(radial_displacement)
avg_radial_displacements = [0]*(iterations+1)
for i in range(1,iterations+1):
    for ii in range(N_trials):
        avg_radial_displacements[i] += store_radial_displacements[ii][i]     
    avg_radial_displacements[i] = avg_radial_displacements[i]/N_trials

plt.figure(9)
plt.title('3D Grid Diffusion Distance From Origin')
plt.ylabel('Distance From Origin (units)')
plt.xlabel('Number of Steps')
plt.plot(avg_radial_displacements,'.')
plt.grid(True)
# It looks like another (1/2) power relationship! Similar to the 1D case, it seems
# like there's some coeffecient that causes it to deviate slightly from y = sqrt(x)

"""
Problem: 3D Random Walk with Random Direction (lvl***)
"""

# theta = inclination
# phi = azimuth
# r = radius
# 0<theta>pi
# 0<phi>2pi
# x,z,y = r*sin(theta)*cos(phi)
# y,x,z = r*sin(theta)*sin(phi)
# z,y,x = r*cos(theta)

def continuous_diffusion_3D(N_steps): 
    x = [0]*(N_steps+1) # x position: left or right
    y = [0]*(N_steps+1) # y position: forward or back
    z = [0]*(N_steps+1) # z pozition: up or down
    potential_theta = np.linspace(0,180,num=1000) # potential inclination angles in degrees
    potential_phi = np.linspace(0,360,num=2000) # potential azimuth angle in degrees # I think there should be 2000... in order to keep angular divisions equal
    potential_axes = ['A','B','C'] # randomly generated angles will tend to cluster around the poles, so polar coordinate systems are randomly assigned each time
    for i in range(1,N_steps+1):
        theta_deg = np.random.choice(potential_theta)
        phi_deg = np.random.choice(potential_phi)
        axes = np.random.choice(potential_axes)
        v = 1
        theta = np.deg2rad(theta_deg)
        phi = np.deg2rad(phi_deg)
        if axes == 'A':
            dx = v*np.sin(theta)*np.cos(phi)
            dy = v*np.sin(theta)*np.sin(phi)
            dz = v*np.cos(theta)
        if axes == 'B':
            dz = v*np.sin(theta)*np.cos(phi)
            dx = v*np.sin(theta)*np.sin(phi)
            dy = v*np.cos(theta)
        if axes == 'C':
            dy = v*np.sin(theta)*np.cos(phi)
            dz = v*np.sin(theta)*np.sin(phi)
            dx = v*np.cos(theta)
        x[i] = x[i-1] + dx
        y[i] = y[i-1] + dy
        z[i] = z[i-1] + dz
    return x,y,z

# plot a few particles moving through a small number of steps
fig = plt.figure(10)
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3D Continuous Diffusion Model')
ax.set_xlabel('X position')
ax.set_ylabel('Y position')
ax.set_zlabel('Z position')
for i in range(3):
    x_position,y_position,z_position = continuous_diffusion_3D(10)
    ax.plot(x_position,y_position,z_position,'.-')
# It's easy to see the angles on this scale. It seems like it's working!

# plot a particle moving through lots of steps
fig = plt.figure(11)
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3D Continuous Diffusion Model')
ax.set_xlabel('X position')
ax.set_ylabel('Y position')
ax.set_zlabel('Z position')
for i in range(1):
    x_position,y_position,z_position = continuous_diffusion_3D(1000)
    ax.plot(x_position,y_position,z_position,'.-')
# this one reminds me more of the subterranean part of an anthill
# definitely looks like diffusion... not super different from the grid model
# maybe the grid model is a decent approximation on large scales...

# figure out the average distance from the origin for each step
store_radial_displacements_b = []
N_trials = 100
iterations = 1000
for i in range(N_trials):
    x_pb,y_pb,z_pb = continuous_diffusion_3D(iterations)
    radial_displacement_b = [0]*(iterations+1)
    for i in range(1,iterations+1):
        radial_displacement_b[i] = np.sqrt((x_pb[i])*(x_pb[i])+(y_pb[i])*(y_pb[i])+(z_pb[i])*(z_pb[i]))
    store_radial_displacements_b.append(radial_displacement_b)
avg_radial_displacements_b = [0]*(iterations+1)
for i in range(1,iterations+1):
    for ii in range(N_trials):
        avg_radial_displacements_b[i] += store_radial_displacements_b[ii][i]     
    avg_radial_displacements_b[i] = avg_radial_displacements_b[i]/N_trials

plt.figure(12)
plt.title('3D Diffusion Distance From Origin')
plt.ylabel('Distance From Origin (units)')
plt.xlabel('Number of Steps')
plt.plot(avg_radial_displacements_b,'.')
plt.grid(True)
# this plot looks familiar... very simliar to 1D diffusion and 3D grid diffusion
