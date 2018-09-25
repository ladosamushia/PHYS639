#angle Vs time

import matplotlib.pyplot as plt 
import numpy as np
tini=0
tfin=15
Nsteps=1000
y0=0#initial position
vy0=1#initial velocity
g=9.8
l=.5#length of pendulum
q=.8#drag coefficient
vy=np.zeros(Nsteps+1)
y=np.zeros(Nsteps+1)
y[0]=y0
vy[0]=vy0
vys=np.zeros(Nsteps+1)
ys=np.zeros(Nsteps+1)
ys[0]=y0
vys[0]=vy0
h=abs(tini-tfin)/Nsteps
t=np.linspace(tini,tfin,Nsteps+1)
def f(x1,x2):
    y1=-(g/l)*np.sin(x1)-q*x2
    y2=x2
    #y3=-(g/l)*x1
    return y1,y2
for i in range(1,Nsteps):
    #k's is the runge kutta coefficients for omega 
    #l's is the runge-kutta coefficients for angle(theta) w/o approx.
    
    k1=h*f(y[i-1],vy[i-1])[0]
    l1=h*f(0,vy[i-1])[1]
    k2=h*f(y[i-1]+l1/2,vy[i-1]+k1/2)[0]
    l2=h*f(0,vy[i-1]+k1/2)[1]
    k3=h*f(y[i-1]+l2/2,vy[i-1]+k2/2)[0]
    l3=h*f(0,vy[i-1]+k2/2)[1]
    k4=h*f(y[i-1]+l3,vy[i-1]+k3)[0]
    l4=h*f(0,vy[i-1]+k3)[1]
    y[i]=y[i-1]+1/6*(l1+2*l2+2*l3+l4)#angle vs time array
    vy[i]=vy[i-1]+1/6*(k1+2*k2+2*k3+k4) #omega vs time array
    
plt.plot(t[0:len(t)-1],y[0:len(t)-1],label=('angle vs time w/o approx. and damping'))
#plt.plot(t[0:len(t)-1],ys[0:len(t)-1],'.',label=('angle vs time with approx.'))
plt.xlabel('time(s)')
plt.ylabel('angle(radians)')
plt.legend(loc='upper right')  
plt.show()
