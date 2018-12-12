# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 19:17:27 2018

@author: phili
"""
#moon flight ~ 40,000Km/H 
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
#Initial Condidtions
m_earth = 5.97e24
m_moon = 7.35e22
thetamoon = np.deg2rad(0)
G_const = 6.67384e-11 
r_earth = 6.371e6
etom = 384.4e6 # real value is 384.4e6 Average Distance from earth to moon
r_moon = 1.737e6
moon_orbit1 = r_moon + 1e5
moon_orbit2 = r_moon + 5e6
Velocitytoorbit = 600
theta_0 = np.deg2rad(0)
def phi(x, y):
    return np.arctan2((moon_orbit2 - y), ((etom-r_earth)-x))
x_0 = (r_earth)*np.cos(theta_0) 
y_0 = (r_earth)*np.sin(theta_0)
#v_phi_0 = 10500
v_x_0 = 20 #v_phi_0*np.cos(phi(x_0, y_0))
v_y_0 = 12000# v_phi_0*np.sin(phi(x_0, y_0))
r_0 = 6.372e8
t_0 = 0.0 # Initial time
t_f = 500000 # Final time
stepsize = 10000000 # fraction of dt 
t = np.linspace( t_0 , t_f , stepsize +1 )
dt = (t_0 + t_f)/stepsize #fractional t for dt
x_p = np.zeros( stepsize + 1 )
y_p = np.zeros( stepsize + 1 )
v_p_y = np.zeros( stepsize +1 )
v_p_x = np.zeros( stepsize +1 )
t = np.zeros( stepsize + 1)
tflyby= np.zeros( stepsize + 1)
#rmmoon = np.zeros( stepsize + 1)
#rmmoon = []
#thetamoon2 = np.zeros( stepsize + 1)
tflyby= 0
#thetamoon2 = []
x_p[0] = x_0
y_p[0] = y_0
v_p_y[0] = v_x_0
v_p_x[0] = v_y_0
t[0] = t_0
v = 0
m1 = 10000
print "Launch Speed : ", np.round(np.sqrt((v_p_x[0]*3.6)**2 + (v_p_y[0]*3.6)**2 ), 2) , "Km/H"
#definitions for functions
#def rocket(m): 
#    return v_phi_0*np.log(m/m1)
def theta(x, y):
    return (np.arctan2(y , x))
def rmoon(x,y):
    return np.sqrt((x-etom*np.cos(thetamoon))**2 + (y - etom*np.sin(thetamoon))**2)
def r(x, y):
    return np.sqrt(x**2 + y**2)
def Accy(x, y): # r must be greater than r_earth
    return ((m_earth*G_const)/((r( x , y )**3)))*y + ((m_moon*G_const)/((rmoon( x , y )**3)))*((y - etom*np.sin(thetamoon)))  
def Accx(x, y): # r must be greater than r_earth
    return ((m_earth*G_const)/((r( x , y )**3)))*x + ((m_moon*G_const)/((rmoon( x , y )**3)))*((x - etom*np.cos(thetamoon))) 
def Accr(x, y):
    return np.sqrt(Accy( x, y )**2 + Accx(x , y)**2)

#print "Y Gravity = ", Accy(x_0, y_0)
#print "X Gravity =" ,Accx(x_0, y_0)
#print "Radial Gravity = ", Accr(x_0, y_0)
#iteration = 100
for i in range ( 1 , stepsize + 1 ):
    x_p[i] = x_p[ i - 1 ] + v_p_x[ i - 1 ]*dt -(0.5)*Accx( x_p[ i - 1 ] , y_p[ i - 1 ])*dt**2  
    y_p[i] = y_p[ i - 1 ] + v_p_y[ i - 1 ]*dt -(0.5)*Accy( x_p[ i - 1 ] , y_p[ i - 1 ])*dt**2
    v_p_y[i] = v_p_y[ i - 1 ] - Accy( x_p[ i - 1 ] , y_p[ i - 1 ])*dt 
    v_p_x[i] = v_p_x[ i - 1 ] - Accx( x_p[ i - 1 ] , y_p[ i - 1 ])*dt
    t[i] = t[i-1] + dt
    if r(x_p[i],y_p[i]) < r_earth:
        print "Hit Earth"
        print "Time of Earth Impact :", dt*i, "s"
        stop_i = i
        print "Impact speed :", np.round(np.sqrt(((v_p_x[stop_i]*3.6)**2) + ((v_p_y[stop_i]*3.6)**2)), 2), "Km/H"
        break
    elif rmoon(x_p[i],y_p[i]) >= moon_orbit1 and rmoon(x_p[i],y_p[i]) <= moon_orbit2 + 2*r_moon:
        tflyby += dt
        stop_i = i
        if tflyby >= 1200: # 20 minutes
            break
#            m_earth = 0  # I was going to describe an orbital path, still a work in progress probably going to make a new loop
#            rmoon(x_p[i], y_p[i])  >= r_moon + moon_orbit1
#            x_p[i] = np.sqrt((x_p[i-1]-etom*np.cos(thetamoon))**2 + (y_p[i-1] - etom*np.sin(thetamoon))**2)*np.cos(0.0001745329251994*dt) # frequency of a 10 hour orbit
#            y_p[i] = np.sqrt((x_p[i-1]-etom*np.cos(thetamoon))**2 + (y_p[i-1] - etom*np.sin(thetamoon))**2)*np.sin(0.0001745329251994*dt)
            # earths effect is negligible 
            # 20 minutes
#        rmmoon = np.append(rmoon(x_p[stop_i],y_p[stop_i]))
#        thetamoon2 = np.append(np.arctan2( y_p[stop_i]-etom, x_p[stop_i]))
#        v += np.sqrt((v_p_x[i]*3.6)**2 + (v_p_y[i]*3.6)**2) 
       
    elif rmoon(x_p[i],y_p[i]) < r_moon:
        print "Hit Moon"
        print "Time of Moon Impact :", dt*i, "s"
        stop_i = i
        print "Impact speed :", np.round(np.sqrt(((v_p_x[stop_i]*3.6)**2) + ((v_p_y[stop_i]*3.6)**2)), 2), "Km/H"
        break
if tflyby > 0: 
    print "Total time in fly by:", tflyby, "s", "," , tflyby/60 , "Min", "," , tflyby/3600 , "hr" 
if tflyby >= 1200:
    print "Orbital Course Correction", "Entered Moon's Orbit at" , stop_i*dt/3600, "Hr"
    


plt.figure(1)
plt.polar(np.rad2deg(theta(x_p[:stop_i], y_p[:stop_i])), r(x_p[:stop_i], y_p[:stop_i]), '--')
ax = pl.subplot(111, polar=True)
ax.set_yticklabels([])
earth1 = pl.Circle((0, 0), r_earth, transform=ax.transData._b, color="red", alpha=0.4)
moon1 = pl.Circle((etom*np.cos(thetamoon), etom*np.sin(thetamoon)), r_moon, transform=ax.transData._b, color="blue", alpha=0.4)
moonorbit1 = pl.Circle((etom*np.cos(thetamoon), etom*np.sin(thetamoon)), r_moon + 5e6, transform=ax.transData._b, alpha=0.4)
ax.add_artist(earth1)
ax.add_artist(moon1)
ax.add_artist(moonorbit1)
plt.title("Projectile full View")
plt.show()

## Tried to make the polar plot show only the moon. Worked with Paul and neither of us could get it to shift. So we tired to 
## to get it to feed new coordnates and make a new centered plot but it also did not work. 
#plt.figure(2)
#plt.polar(np.rad2deg(thetamoon2), rmmoon, '--')
#ax = pl.subplot(111, polar=True)
#ax.set_yticklabels([])
#ax.set_rlim(0, 5*r_moon)
#moon2 = pl.Circle((0,0), r_moon, transform=ax.transData._b, color="blue", alpha=0.4)
#moonorbit2 = pl.Circle((0,0), r_moon + 5e6, transform=ax.transData._b, alpha=0.4)
#ax.add_artist(moon2)
#ax.add_artist(moonorbit2)
#plt.title("Projectile Low Moon View")
#plt.show()

plt.figure(3)
plt.polar(np.rad2deg(theta(x_p[:stop_i], y_p[:stop_i])), r(x_p[:stop_i], y_p[:stop_i]), '--')
ax = pl.subplot(111, polar=True)
ax.set_yticklabels([])
ax.set_rlim(0,5*r_earth)
earth3 = pl.Circle((0, 0), r_earth, transform=ax.transData._b, color="red", alpha=0.4)
ax.add_artist(earth3)
plt.title("Low Earth View")
plt.show()



