# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 12:36:38 2018
@author: Aus
PHYS 639: Projectile Motion
"""

import matplotlib.pyplot as plt

# initial conditions

x0 = 0
y0 = 0
y = 20
v0x = 500
v0y = 500
tini = 0
dt = .01

def displacement(x0,y0,v0x,v0y,ax,ay,dt): #subset of equations to find delta(x)
    
    x = x0 + v0x*dt
    y = y0 + v0y*dt
    Vx = v0x + ax*dt
    Vy = v0y + ay*dt
    return([x,y,Vx,Vy])
    
x = x0
y = y0
Vx = v0x
Vy = v0y
while y>=0: #calculate displacement while y is greater than zero.
   
    ay = -0.00004*(Vx**2+Vy**2)-9.8
    ax =  -0.00004*(Vx**2+Vy**2)
    [x,y,Vx,Vy] = displacement(x,y,Vx,Vy,ax,ay,dt)
    plt.plot(x,y,'.g')
    
    
    
# -----------------------------------------------------

x0 = 0
y0 = 0
y = 20
tini = 0
ax = 0

def displacement(x0,y0,v0x,v0y,ax,ay,dt): #subset of equations to find delta(x)
    
    x = x0 + v0x*dt
    y = y0 + v0y*dt 
    Vx = v0x + ax*dt
    Vy = v0y + ay*dt
    return([x,y,Vx,Vy])
    
x = x0
y = y0
Vx = v0x
Vy = v0y
ax=0
ay=-9.8
while y>=0: #calculate displacement while y is greater than zero.
    [x,y,Vx,Vy] = displacement(x,y,Vx,Vy,ax,ay,dt)
    plt.hold(True)
    plt.plot(x,y,'.b')
    
    


x0 = 0
y0 = 0
y = 20
tini = 0
ax = 0

def displacement(x0,y0,v0x,v0y,ax,ay,dt): #subset of equations to find delta(x)
    
    x = x0 + v0x*dt
    y = y0 + v0y*dt 
    Vx = v0x + ax*dt
    Vy = v0y + ay*dt
    return([x,y,Vx,Vy])
    
x = x0
y = y0
Vx = v0x
Vy = v0y
while y>=0: #calculate displacement while y is greater than zero.
    ay = -0.00004*(Vx**2+Vy**2)*(1-2.2e-5*y)**(5/2) - 9.8
    ax =  -0.00004*(Vx**2+Vy**2)*(1-2.2e-5*y)**(5/2)
    [x,y,Vx,Vy] = displacement(x,y,Vx,Vy,ax,ay,dt)
    plt.hold(True)
    plt.plot(x,y,'.r')
    



    
    
    
    
    
    
    
    
    