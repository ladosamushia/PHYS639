# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 2018

Projectile Motion 2-D part 1

Creator Philip Lucas, some debugging assisted by Jesse Laning 
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt
# all units in Kg,m,s 
g = 9.81 # acceleratio in y
x_0 = int(input("Initial x position will be in m :")) # Initial "x" Position
y_0 =  int(input("Intial height will be in m :")) # Initial "y" Position
v_0 =  4000 #int(input("Enter Velocity will be in m/s :")) # Initial velocity
t_0 = 0.0 # Initial time
t_f = 10000 # Final time
stepsize = 1000000 # fraction of dt 
t = np.linspace( t_0 , t_f , stepsize +1 )
dt = (t_0 + t_f)/stepsize #fractional t for dt
degree = int(input("Launch Angle in degrees :")) # Inital angle in degree
theta = (degree*m.pi)/180.0 # Initial Angle in radians

print "   "
print "Part 1.1.0 : Without Drag"
print "   "

#x and y component velocities
v_0_x =  (v_0)*np.cos( theta )
v_0_y = (v_0)*np.sin( theta )
#arrays for positions and velocities 
x_p = np.zeros( stepsize + 1 )
y_p = np.zeros( stepsize + 1 )
v_p_y = np.zeros( stepsize +1 )
v_p_x = np.zeros( stepsize +1 )
#establishing intial conditions
v_p_y[0] = v_0_y
v_p_x[0] = v_0_x
x_p[0]= x_0
y_p[0] = y_0
stop_i = 0
for i in range ( 1 , stepsize + 1 ):
    x_p[i] = x_p[ i - 1 ] + v_0_x*dt
    y_p[i] = y_p[ i - 1 ] + v_p_y[ i - 1 ]*dt -(0.5)*g*dt**2
    v_p_y[i] = v_p_y[ i - 1 ] - g*dt
    if y_p[i] <= 0:
        print"Final Height : " , ((y_p[i] + y_p[i-1])/2), "m"
        print "Final Displacement : " , x_p[i], "m"
        print "Time of impact :", dt*i, "s"
        print "   "
        stop_i = i #once projectile hits the grond it sould stop
        break
    if y_p[i-2] < y_p[i-1]  and y_p[i] < y_p[i-1]:
        print "Maximum Altitude :" , y_p[i-1], "m"  # max height
        print "X Displacement at Maximum Altitude :" , x_p[i-1] , "m"
        print "Time to Maximum Altitude :" ,  dt*i , "s"

plt.plot(x_p[:stop_i], y_p[:stop_i], '--')
plt.xlabel (" X position (m) ")
plt.ylabel (" Y position (m) ")
#%%
"""

Projectile Motion part 2 with drag

"""""
print "Part 1.2.0: With Constant Drag" 
print "   "
a_0_x_drag = ( 0.0004*(v_0)**2 )*np.cos( theta )
a_0_y_drag = ( 0.0004*(v_0)**2 )*np.sin( theta )
#arrays for positions and velocities 
a_p_x_drag = np.zeros( stepsize + 1 )
a_p_y_drag = np.zeros( stepsize + 1 )
#establishing intial conditions
a_p_x_drag[0] = a_0_x_drag
a_p_y_drag[0] = a_0_y_drag
stop_i = 0
for i in range ( 1 , stepsize + 1 ):
    x_p[i] = x_p[ i - 1 ] + v_p_x[ i - 1 ]*dt -(0.5)*a_p_x_drag[ i - 1 ]*dt**2
    y_p[i] = y_p[ i - 1 ] + v_p_y[ i - 1 ]*dt -(0.5)*(g + a_p_y_drag[ i - 1 ])*dt**2
    if a_p_y_drag[ i -1 ] < 0:
        a_p_y_drag[ i -1 ] = -a_p_y_drag[ i -1 ]
    else:a_p_y_drag [ i -1 ] = a_p_y_drag[ i - 1 ]
    v_p_y[i] = v_p_y[ i - 1 ] - g*dt - a_p_y_drag[ i - 1 ]*dt
    v_p_x[i] = v_p_x[ i -1 ] - a_p_x_drag[ i - 1 ]*dt
    if y_p[i] <= 0:
        print"Final Height : " , ((y_p[i] + y_p[i-1])/2), "m"
        print "Final Displacement : " , x_p[i], "m"
        print "Time of impact :", dt*i, "s"
        print "   "
        stop_i = i #once projectile hits the ground it sould stop
        break
    if y_p[i-2] < y_p[i-1]  and y_p[i] < y_p[i-1]:
        print "Maximum Altitude :" , y_p[i-1], "m"  # max height
        print "X Displacement at Maximum Altitude :" , x_p[i-1], "m"
        print "Time to Maximum Altitude :" ,  dt*i, "s"

plt.plot(x_p[:stop_i], y_p[:stop_i], 'b')
plt.xlabel (" X position (m) ")
plt.ylabel (" Y position (m) ")
#%%
"""

Projectile Motion part 2 with drag

"""
print "Part 1.3.0: With Variable Drag" 
print "   "
a_0_x_drag = ( 0.0004*(v_0)**2 )*np.cos( theta )
a_0_y_drag = ( 0.0004*(v_0)**2 )*np.sin( theta )
#arrays for positions and velocities 
a_p_x_drag = np.zeros( stepsize + 1 )
a_p_y_drag = np.zeros( stepsize + 1 )
#establishing intial conditions
a_p_x_drag[0] = a_0_x_drag
a_p_y_drag[0] = a_0_y_drag
stop_i = 0
for i in range ( 1 , stepsize + 1 ):
    x_p[i] = x_p[ i - 1 ] + v_p_x[ i - 1 ]*dt -(0.5)*a_p_x_drag[ i - 1 ]*dt**2
    y_p[i] = y_p[ i - 1 ] + v_p_y[ i - 1 ]*dt -(0.5)*(g + a_p_y_drag[ i - 1 ])*dt**2
    if a_p_y_drag[ i -1 ] < 0:
        a_p_y_drag[ i -1 ] = -a_p_y_drag[ i -1 ]
    else:a_p_y_drag [ i -1 ] = a_p_y_drag[ i - 1 ]
    v_p_y[i] = v_p_y[ i - 1 ] - g*dt - a_p_y_drag[ i - 1 ]*(((1-(1.22e-5)*(y_0 + v_p_y[i-1]*dt))**(5/2)))*dt
    v_p_x[i] = v_p_x[ i -1 ] - a_p_x_drag[ i - 1 ]*(((1-(1.22e-5)*y_p[i-1])**(5/2)))*dt
    if y_p[i] <= 0:
        print"Final Height : " , ((y_p[i] + y_p[i-1])/2), "m"
        print "Final Displacement : " , x_p[i], "m"
        print "Time of impact :", dt*i, "s"
        print "   "
        stop_i = i #once projectile hits the grond it sould stop
        break
    if y_p[i-2] < y_p[i-1]  and y_p[i] < y_p[i-1]:
        print "Maximum Altitude :" , y_p[i-1], "m"  # max height
        print "X Displacement at Maximum Altitude :" , x_p[i-1], "m"
        print "Time to Maximum Altitude :" ,  dt*i, "s"

plt.plot(x_p[:stop_i], y_p[:stop_i], 'pink')
plt.xlabel (" X position (m) ")
plt.ylabel (" Y position (m) ")
#%%

"""

Projectile Motion part 4 with Drag and Varible Gravity 

"""""
print "Part 1.4.1 : With Varible Gravity g as a function of altitude "
print "   "
# all units in Kg,m,s 
r_earth = 6371000.00 #radius of earth in m
m_earth= 5.972e24 #mass of earth in Kg
G_constant = 6.67408e-11 # Gravitational constant in MKS
G_0 = (m_earth*G_constant)/( ( r_earth + y_0 )**2 )
#establishing intial conditions
v_0_x =  (v_0)*np.cos( theta )
v_0_y = (v_0)*np.sin( theta )
#arrays for positions and velocities 
x_p = np.zeros( stepsize + 1 )
y_p = np.zeros( stepsize + 1 )
v_p_y = np.zeros( stepsize +1 )
v_p_x = np.zeros( stepsize +1 )
#establishing intial conditions
v_p_y[0] = v_0_y
v_p_x[0] = v_0_x
x_p[0]= x_0
y_p[0] = y_0
G = np.zeros( stepsize + 1 )
G[0]= G_0
stop_i = 0
for i in range ( 1 , stepsize + 1 ):
    # next step seems to work it makes g larger at lower y_p and larger at higher y_p
    # print excluded to show this because of how many G[i] are produced
    # to see this print G[i]
    G[i] = m_earth*G_constant/( ( r_earth + y_p[ i -1] + v_p_y[ i -1 ]*dt )**2 )
   # print(G[i],y_p[i-1]+v_p_y[i-1]*dt)
    x_p[i] = x_p[ i - 1 ] + v_p_x[ i - 1 ]*dt
    y_p[i] = y_p[ i - 1 ] + v_p_y[ i - 1 ]*dt -(0.5)*(G[ i - 1  ])*dt**2
    v_p_y[i] = v_p_y[ i - 1 ] - G[i-1]*dt 
    v_p_x[i] = v_p_x[ i -1 ]
    if y_p[i] <= 0:
        print"Final Height : " , ((y_p[i] + y_p[i-1])/2), "m"
        print "Final Displacement : " , x_p[i], "m"
        print "Time of impact :", dt*i, "s"
        print "   "
        stop_i = i #once projectile hits the ground it sould stop
        break
    if y_p[i-2] < y_p[i-1]  and y_p[i] < y_p[i-1]:
        print "Maximum Altitude :" , y_p[i-1], "m"  # max height
        print "X Displacement at Maximum Altitude :" , x_p[i-1], "m"
        print "Time to Maximum Altitude :" ,  dt*i, "s"

plt.plot(x_p[:stop_i], y_p[:stop_i], 'g')
plt.xlabel (" X position (m) ")
plt.ylabel (" Y position (m) ")
#%%%
"""

Projectile Motion part 4 with Drag and Varible Gravity 

"""""
print " "
print "Part 1.4.2: With Variable Drag and Varible Gravity g as a function of altitude "
print "   "
for i in range ( 1 , stepsize + 1 ):
    # next step seems to work it makes g larger at lower y_p and larger at higher y_p
    # print excluded to show this because of how many G[i] are produced
    # to see this print G[i]
    G[i] = m_earth*G_constant/( ( r_earth + y_p[ i -1] + v_p_y[ i -1 ]*dt )**2 ) 
    x_p[i] = x_p[ i - 1 ] + v_p_x[ i - 1 ]*dt -(0.5)*a_p_x_drag[ i - 1 ]*dt**2
    y_p[i] = y_p[ i - 1 ] + v_p_y[ i - 1 ]*dt -(0.5)*(G[ i  ] + a_p_y_drag[ i - 1 ])*dt**2
    if a_p_y_drag[ i -1 ] < 0:
        a_p_y_drag[ i -1 ] = -a_p_y_drag[ i -1 ]
    else:a_p_y_drag [ i -1 ] = a_p_y_drag[ i - 1 ]
    v_p_y[i] = v_p_y[ i - 1 ] - g*dt - a_p_y_drag[ i - 1 ]*(((1-(1.22e-5)*(y_0 + v_p_y[i-1]*dt))**(5/2)))*dt
    v_p_x[i] = v_p_x[ i -1 ] - a_p_x_drag[ i - 1 ]*(((1-(1.22e-5)*y_p[i-1])**(5/2)))*dt
    if y_p[i] <= 0 and y_p[i - 1] >= 0:
        print"Final Height : " , ((y_p[i] + y_p[i-1])/2), "m"
        print "Final Displacement : " , x_p[i], "m"
        print "Time of impact :", dt*i, "s"
        print "   "
        stop_i = i #once projectile hits the ground it sould stop
        break
    if y_p[i-2] < y_p[i-1]  and y_p[i] < y_p[i-1]:
        print "Maximum Altitude :" , y_p[i-1], "m"  # max height
        print "X Displacement at Maximum Altitude :" , x_p[i-1], "m"
        print "Time to Maximum Altitude:" ,  dt*i, "s"

plt.plot(x_p[:stop_i], y_p[:stop_i], 'r--')
plt.xlabel (" X position (m) ")
plt.ylabel (" Y position (m) ")
