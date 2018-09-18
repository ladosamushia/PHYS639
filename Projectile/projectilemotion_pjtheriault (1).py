
# coding: utf-8

# In[12]:


#Written by Paul Theriault
import math
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#################################################################################################################################

#The purpose of this program is to simulate projectile motion
#DISCLAIMER: A and C can not both be 1
v0 = int(input('Please input an inital velocity: '))
a = float(input('Please input a launch angle in degrees between 0 and 90: '))
A = int(input('1/0 for Air Reistance where 1 is Yes and 0 is No: '))
B = int(input('1/0 for Changing Gravity where 1 is Yes and 0 is No: '))
C = int(input('1/0 for Changing Density of Air where 1 is Yes and 0 is No: '))

v = math.radians(a)
vx = v0*np.cos(v) #x velocity
vy = v0*np.sin(v) #y velocity
t = -vy/-9.8 #Time to reach apoapsis
y = vy*t-0.5*9.8*t**2 #Apoapsis
q = math.sqrt((2*y)/9.8) #time to fall back to ground

print('############################################################################')
print('Default Motion Ignoring Everything:')
print('Horizontal Range:', vx*(t+q), 'meters') #Range
print('Apoapsis:', y, 'meters') #Apoapsis
print('Time to Apoapsis:', t, 'seconds') #Time to reach apoapsis
print('Flight Time:', (t+q), 'seconds') #Total flight time

#Realized that I need a loop to generate all values to graph
#initial conditions
ti = 0 #inital time
xi = 0 #inital x position
yi = 0 #inital y position
ve = v0 #inital velocity
dt=0.01 #time step
xr = np.array([xi])
yr = np.array([yi])

# Loop that simulates motion until impact (runs for as long as y is larger than 0)
while yi >= 0:
  ax = 0 # No acceleration in x
  ay = -9.8 # Gravity

#################################################################################################################################
#The purpose of this section of code is to add air resistance as a function of velocity Fd = -0.00004*v^2
  if A==1 and C==0:
   Fd = -0.00004*(vx**2+vy**2)
   cos = vx/np.sqrt(vx**2+vy**2)
   sin = vy/np.sqrt(vx**2+vy**2)
   Fdx = Fd*cos
   Fdy = Fd*sin
   ax += Fdx
   ay += Fdy

#################################################################################################################################
#The purpose of this section of code is to add changing gravity with altitude
  if B==1:
   ay *= 6371000**2/(6371000+y)**2

#################################################################################################################################
#The purpose of this section of code is to add changing density of air with altitude
#Assumes drag scales with (1-2.2e-5*h)^(5/2) where h is altitude
  if C==1 and A==0:
   Fd = -0.00004*(vx**2+vy**2)*(1-2.2E-5*y)**(5/2)
   cos = vx/np.sqrt(vx**2+vy**2)
   sin = vy/np.sqrt(vx**2+vy**2)
   Fdx = Fd*cos
   Fdy = Fd*sin
   ax += Fdx
   ay += Fdy 
#I think this is the same as the drag section except now we multiply by a scaling factor

#################################################################################################################################
#Calculations
  xi = xi + vx*dt
  yi = yi + vy*dt
  vx = vx + ax*dt
  vy = vy + ay*dt
  t = t + dt
#Adds new value to the array
  xr = np.append(xr,xi)
  yr = np.append(yr,yi)
 
# Plot
plt.plot(xr,yr,label='Trajectory')
plt.legend()
plt.xlabel('Range (m)')
plt.ylabel('Altitude (m)')
print('############################################################################')
print('Motion that has been altered by user requests:')
print('Horizontal Range: ', np.max(xr), 'meters')
print('Apoapsis: ', np.max(yr), 'meters')
print('Time to Apoapsis ', 'work in progress') #not sure how to get the t value associated with maximum height.
print('Flight Time: ', t, 'seconds') #This time is off when trying to simulate Default Motion (chosing No or 0,0,0 to all).

#################################################################################################################################

#Final comments: Had trouble finding a way to to plot the default motion along side the altered motion.
#Lastly I noticed time in my simulated default motion is different than the actual time it takes. Not sure why this is.
#All values for user requested alterations to motion appear to make sense compared to each other and the default motion.

