# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 2018

Projectile Motion 2-D part 1

Creator Philip Lucas, some debugging assisted by Jesse Laning 
"""
print "Part 1: Without Drag"
print "   "
import numpy as np
import math as m
import matplotlib.pyplot as plt
# all units in Kg,m,s 
g = 9.81 # acceleratio in y
m_0 = 1000.0 # mass in Kg
x_0 = 0.0 # Initial "x" Position
y_0 = 0.0 # Initial "y" Position
v_0 = 100.0 # Initial velocity
t_0 = 0.0 # Initial time
t_f = 100 # Final time
stepsize = 10000 # fraction of dt 
t = np.linspace( t_0 , t_f , stepsize +1 )
dt = (t_0 + t_f)/stepsize #fractional t for dt
degree = 45.0 # Inital angle in degree
theta = (degree*m.pi)/180.0 # Initial Angle in radians
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

plt.plot(x_p[:stop_i], y_p[:stop_i], 'r')
plt.xlabel (" X position (m) ")
plt.ylabel (" Y position (m) ")
#%%
"""

Projectile Motion part 2 with drag

"""""
print "Part 2: with Drag" 
print "   "
import numpy as np
import math as m
import matplotlib.pyplot as plt
# all units in Kg,m,s 
g = 9.81 # acceleratio in y
m_0 = 100.0 # mass in Kg
x_0 = 0.0 # Initial "x" Position
y_0 = 0.0 # Initial "y" Position
v_0 = 100.0 # Initial velocity
t_0 = 0.0 # Initial time
t_f = 100 # Final time
stepsize = 10000 # fraction of dt 
t = np.linspace( t_0 , t_f , stepsize +1 )
dt = (t_0 + t_f)/stepsize #fractional t for dt
degree = 45.0 # Inital angle in degree
theta = (degree*m.pi)/180.0 # Initial Angle in radians
#x and y component velocities
v_0_x =  (v_0)*np.cos( theta )
v_0_y = (v_0)*np.sin( theta )
a_0_x_drag = ( 0.04*(v_0)**2 )*np.cos( theta )
a_0_y_drag = ( 0.04*(v_0)**2 )*np.sin( theta )
#arrays for positions and velocities 
x_p = np.zeros( stepsize + 1 )
y_p = np.zeros( stepsize + 1 )
v_p_y = np.zeros( stepsize +1 )
v_p_x = np.zeros( stepsize +1 )
a_p_x_drag = np.zeros( stepsize + 1 )
a_p_y_drag = np.zeros( stepsize + 1 )
#establishing intial conditions
a_p_x_drag[0] = a_0_x_drag
a_p_y_drag[0] = a_0_y_drag
v_p_y[0] = v_0_y
v_p_x[0] = v_0_x
x_p[0]= x_0
y_p[0] = y_0
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
        print"Final Height with Drag : " , ((y_p[i] + y_p[i-1])/2), "m"
        print "Final Displacement with Drag : " , x_p[i], "m"
        print "Time of impact with Drag :", dt*i, "s"
        print "   "
        stop_i = i #once projectile hits the grond it sould stop
        break
    if y_p[i-2] < y_p[i-1]  and y_p[i] < y_p[i-1]:
        print "Maximum Altitude with Drag :" , y_p[i-1], "m"  # max height
        print "X Displacement at Maximum Altitude with Drag :" , x_p[i-1], "m"
        print "Time to Maximum Altitude with Drag :" ,  dt*i, "s"

plt.plot(x_p[:stop_i], y_p[:stop_i], 'g')
plt.xlabel (" X position (m) ")
plt.ylabel (" Y position (m) ")
#%%
"""

Projectile Motion part 3 with Variable drag

"""""
#%%%
"""

Projectile Motion part 4 with Drag and Varible Gravity 

"""""
print "Part 4: with Drag and Varible Gravity g as a function of altitude "
print "   "
import numpy as np
import math as m
import matplotlib.pyplot as plt
# all units in Kg,m,s 
r_earth = 6371000.0 #radius of earth in m
m_earth= 5.972e24 #mass of earth in Kg
G_constant = 6.67408e-11 # Gravitational constant in MKS
m_0 = 100.0 # mass in Kg
x_0 = 0.0 # Initial "x" Position
y_0 = 0.0 # Initial "y" Position
v_0 = 100.0 # Initial velocity
t_0 = 0.0 # Initial time
t_f = 100 # Final time
G_0 = (m_earth*G_constant)/( ( r_earth + y_0 )**2 )
stepsize = 10000 # fraction of dt 
t = np.linspace( t_0 , t_f , stepsize +1 )
dt = (t_0 + t_f)/stepsize #fractional t for dt
degree = 45.0 # Inital angle in degree
theta = (degree*m.pi)/180.0 # Initial Angle in radians
#x and y component velocities
v_0_x =  (v_0)*np.cos( theta )
v_0_y = (v_0)*np.sin( theta )
a_0_x_drag = ( 0.04*(v_0)**2 )*np.cos( theta )
a_0_y_drag = ( 0.04*(v_0)**2 )*np.sin( theta )
#arrays for positions and velocities 
x_p = np.zeros( stepsize + 1 )
y_p = np.zeros( stepsize + 1 )
v_p_y = np.zeros( stepsize +1 )
v_p_x = np.zeros( stepsize +1 )
a_p_x_drag = np.zeros( stepsize + 1 )
a_p_y_drag = np.zeros( stepsize + 1 )
G = np.zeros( stepsize + 1 )
dy = np.zeros( stepsize + 1 )
#establishing intial conditions
a_p_x_drag[0] = a_0_x_drag
a_p_y_drag[0] = a_0_y_drag
G[0]= G_0
dy = (v_0_y*dt)
v_p_y[0] = v_0_y
v_p_x[0] = v_0_x
x_p[0]= x_0
y_p[0] = y_0
stop_i = 0
for i in range ( 1 , stepsize + 1 ):
    # next step seems to work it makes g larger at lower y_p and larger at higher y_p
    # print excluded to show this because of how many G[i] are produced
    # to see this print G[i]
    G[i] = G[ i ] + m_earth*G_constant/( ( r_earth + y_p[ i -1] + v_p_y[ i -1 ]*dt )**2 ) 
    print G[i]
    x_p[i] = x_p[ i - 1 ] + v_p_x[ i - 1 ]*dt -(0.5)*a_p_x_drag[ i - 1 ]*dt**2
    y_p[i] = y_p[ i - 1 ] + v_p_y[ i - 1 ]*dt -(0.5)*(G[ i - 1 ] + a_p_y_drag[ i - 1 ])*dt**2
    if a_p_y_drag[ i -1 ] < 0:
        a_p_y_drag[ i -1 ] = -a_p_y_drag[ i -1 ]
    else:a_p_y_drag [ i -1 ] = a_p_y_drag[ i - 1 ]
    v_p_y[i] = v_p_y[ i - 1 ] - g*dt - a_p_y_drag[ i - 1 ]*dt
    v_p_x[i] = v_p_x[ i -1 ] - a_p_x_drag[ i - 1 ]*dt
    if y_p[i] <= 0:
        print"Final Height with Drag and variable g(r): " , ((y_p[i] + y_p[i-1])/2), "m"
        print "Final Displacement with Drag and variable g(r): " , x_p[i], "m"
        print "Time of impact with Drag and variable g(r):", dt*i, "s"
        print "   "
        stop_i = i #once projectile hits the grond it sould stop
        break
    if y_p[i-2] < y_p[i-1]  and y_p[i] < y_p[i-1]:
        print "Maximum Altitude with Drag and varible g(r) :" , y_p[i-1], "m"  # max height
        print "X Displacement at Maximum Altitude with Drag and variable g(r) :" , x_p[i-1], "m"
        print "Time to Maximum Altitude with Drag and variable g(r) :" ,  dt*i, "s"

plt.plot(x_p[:stop_i], y_p[:stop_i], 'y')
plt.xlabel (" X position (m) ")
plt.ylabel (" Y position (m) ")