# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:28:41 2018

@author: Mikelobe
"""

import numpy as np
import matplotlib.pyplot as plt

#Simple Projectile Motion

x0=0 #initial position
y0=0
t0=0 #initial time
v0y=200 #initial velocity
v0x=60
tfin=100
Nsteps=1000000
Fx=0 #force in x
Fy=-9.8 #force in y
m=1 #mass
t=np.linspace(t0,tfin,Nsteps+1)
x=np.zeros(Nsteps+1)
x[0]=x0
y=np.zeros(Nsteps+1)
y[0]=y0
vx=np.zeros(Nsteps+1)
vx[0]=v0x
vy=np.zeros(Nsteps+1)
vy[0]=v0y
dt=(tfin-t0)/Nsteps #slight changes in time
for i in range(1,Nsteps+1): #loop for projectile motion
    x[i]=x[i-1]+vx[i-1]*dt
    vx[i]=vx[i-1]+(Fx/m)*dt
    y[i]=y[i-1]+vy[i-1]*dt
    vy[i]=vy[i-1]+(Fy/m)*dt
    if y[i]<0: #how the loop knows when to stop
        print('Total time', i*dt) #print max value of time
        break
plt.plot(x,y,'g.') #plot the loop
print('max in x=',np.max(x),'max in y=',np.max(y)) #print max values of x and y

#Air Resistance


t=np.linspace(t0,tfin,Nsteps+1)
x=np.zeros(Nsteps+1)
x[0]=x0
y=np.zeros(Nsteps+1)
y[0]=y0
vx=np.zeros(Nsteps+1)
vx[0]=v0x
vy=np.zeros(Nsteps+1)
vy[0]=v0y
dt=(tfin-t0)/Nsteps
for i in range(1,Nsteps+1):
    x[i]=x[i-1]+vx[i-1]*dt
    vx[i]=vx[i-1]+(Fx/m)*dt
    y[i]=y[i-1]+vy[i-1]*dt
    vy[i]=vy[i-1]+(Fy/m)*dt
    Fx=-0.0004*vx[i-1]**2
    Fy=-9.8-(0.0004*vy[i-1]**2)
    if y[i]<0:
        print('Total time', i*dt)
        break
plt.plot(x,y,'b.')
print('max in x=',np.max(x),'max in y=',np.max(y))

#Change in Air Resistance


t=np.linspace(t0,tfin,Nsteps+1)
x=np.zeros(Nsteps+1)
x[0]=x0
y=np.zeros(Nsteps+1)
y[0]=y0
vx=np.zeros(Nsteps+1)
vx[0]=v0x
vy=np.zeros(Nsteps+1)
vy[0]=v0y
dt=(tfin-t0)/Nsteps
for i in range(1,Nsteps+1):
    x[i]=x[i-1]+vx[i-1]*dt
    vx[i]=vx[i-1]+(Fx/m)*dt
    y[i]=y[i-1]+vy[i-1]*dt
    vy[i]=vy[i-1]+(Fy/m)*dt
    Fx=-((0.0004*vx[i-1]**2)*(1-(0.000022*y[i-1]))**(2.5))
    Fy=-9.8-((0.0004*vy[i-1]**2)*(1-(0.000022*y[i-1]))**(2.5))
    if y[i]<0:
        print('Total time', i*dt)
        break
plt.plot(x,y,'y.')
print('max in x=',np.max(x),'max in y=',np.max(y))


#Changes in Gravity

t=np.linspace(t0,tfin,Nsteps+1)
x=np.zeros(Nsteps+1)
x[0]=x0
y=np.zeros(Nsteps+1)
y[0]=y0
vx=np.zeros(Nsteps+1)
vx[0]=v0x
vy=np.zeros(Nsteps+1)
vy[0]=v0y
dt=(tfin-t0)/Nsteps
for i in range(1,Nsteps+1):
    x[i]=x[i-1]+vx[i-1]*dt
    vx[i]=vx[i-1]+(Fx/m)*dt
    y[i]=y[i-1]+vy[i-1]*dt
    vy[i]=vy[i-1]+(Fy/m)*dt
    Fx=-((0.0004*vx[i-1]**2)*(1-(0.000022*y[i-1]))**(2.5))
    Fy=-9.8-((0.0004*vy[i-1]**2)*(1-(0.000022*y[i-1]))**(2.5))
    if y[i]<0:
        print('Total time', i*dt)
        break
plt.plot(x,y,'r.')
print('max in x=',np.max(x),'max in y=',np.max(y))