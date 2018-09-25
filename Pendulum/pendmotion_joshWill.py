import math
import numpy as np
import matplotlib.pyplot as plt

#simple pendulum

#Start with initial conditions
m=1#mass
L=1
vi=0#initial velocity
q=1#numerical value
g=9.81
theta=np.rad2deg(45)#initial angle in rad
vtheta=0#initial angular velocity in rad
t0=0#time start
tf=10#time stop
n=10000#steps
t=np.linspace(t0,tf,n)#range of t
F=-m*g*np.sin(theta)#grav. force in theta
w=30*np.pi/180

dt=.001
theta=np.zeros(n)#range of theta
theta[0]=(20*np.pi)/180

for i in range(1,n):
    atheta=-((g/L)*np.sin(theta[i-1]))#angular acc.
    vtheta+=atheta*dt
    theta[i]=theta[i-1]+vtheta*dt#arr. of theta
    
plt.figure(1) 
plt.plot(t,theta)
plt.title('shm')
#Produces the expected sinusoidal function

#plot small angle approx
plt.figure(2)
plt.plot(t,theta[0]*np.cos(t*((g/L)**.5)),label='Sm. angle approx.')
plt.title('Sm.angle approx')

#Part two pendulum boogaloo, add dampening
for i in range(1,n):
    atheta=-((g/L)*np.sin(theta[i-1]))#angular acc.
    vtheta+=atheta*dt
    theta[i]=theta[i-1]+vtheta*dt#arr. of theta
    if theta[i] > (np.pi/2):
        theta[i]=theta[i]-np.pi
    elif theta[i] < -(np.pi/2):
        theta[i]=theta[i]+np.pi #we don't want theta greater then +-90 deg
        
#attempt to plot
plt.figure(3)
plt.plot(t,theta)
plt.title('Damped pend')

for i in range(1,n):
    Fext=5*np.sin(w)
    atheta=-((g/L)*np.sin(theta[i-1]))-(q*vtheta)+Fext
    vtheta+=atheta*dt
    theta[i]=theta[i-1]+vtheta*dt
    if theta[i] > (90*np.pi/180): #If theta is greater than 90 degrees
        theta[i] = theta[i] - np.pi
    elif theta[i] < -(90*np.pi/180):
        theta[i] = theta[i] + np.pi
        
plt.figure(4)
plt.plot(t, theta)
plt.title('Driving pend')

#Plots seem to corroborate expected behavior
#max iff w=(g/L)**5, yeilds expected results

#plot freq v amp d_freq v maxang

def sf(L):#simple pend freq.
    amp=np.linspace(.05*np.pi,.95*np.pi,100)#amp values data
    freqs=[]#data array for frequency
    for theta in amp:
        v=0
        g=9.81
        t0=0
        tf=10
        dt=.001
        root=0
        theta1=theta#separate this from other to not confuse self
        time=np.linspace(t0,tf,int(tf/dt))
        thetas=[]
        for t in time:
            thetas.append(theta)
            theta+=v*dt
            v+=(-(g/L)*np.sin(theta)-q*v)*dt
            if theta < 0 and theta1 < 0:
                freq=np.pi/(t-root)
                root=t
            theta1=theta
            
    freqs.append(freq)
       
    plt.figure(5)
    plt.title('Simp.Pend.')
    plt.plot(amp,freq)#not plotting
    
    sf(1)
    
def d_freq(L,q):
    amp=np.linspace(.05*np.pi,.95*np.pi,100)
    freqs=[]
    for theta in amp:
        v=0
        g=9.81
        t0=0
        tf=10
        dt=.001
        root=0
        theta1=theta
        time=np.linspace(t0,tf,int(tf/dt))
        thetas=[]
        for t in time:
            thetas.append(theta)
            theta+=v*dt
            v+=(-(g/L)*np.sin(theta)-q*v)*dt
            if theta < 0 and theta1 > 0:
                freq=np.pi/(t-root)
                root = t
            theta1 = theta
            
    freqs.append(freq)
    plt.figure(6)
    plt.plot(amp,freq)
    plt.title('simple pendulum, amp vs freq')
        
#last 2 plots not working.