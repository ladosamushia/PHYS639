import matplotlib.pyplot as plt 
import numpy as np
tini=0
tfin=15
Nsteps=1000
x0=0
y0=0
vy0=25
vx0=5
a=-9.8
vy=np.zeros(Nsteps+1)
vx=np.zeros(Nsteps+1)
x=np.zeros(Nsteps+1)
y=np.zeros(Nsteps+1)
x[0]=x0
y[0]=y0
vy[0]=vy0
vx[0]=vx0
h=abs(tini-tfin)/Nsteps
t=np.linspace(tini,tfin,Nsteps+1)
def f(x1):
    y1=a
    y2=x1
    y3=x2
    return y1,y2,y3
x2=vx0#eqn for x(t)
for i in range(1,Nsteps):
#calculating v(t)
    k1=h*f(vy[i-1])[0]
    k2=h*f(vy[i-1]+k1/2)[0]
    k3=h*f(vy[i-1]+k2/2)[0]
    k4=h*f(vy[i-1]+k3)[0]
    vy[i]=vy[i-1]+1/6*(k1+2*k2+2*k3+k4)
    
#calculating y(t) 
    l1=h*f(vy[i-1])[1]
    l2=h*f(vy[i-1]+k1/2)[1]
    l3=h*f(vy[i-1]+k2/2)[1]
    l4=h*f(vy[i-1]+k3)[1]
    y[i]=y[i-1]+1/6*(l1+2*l2+2*l3+l4)
#calulating x(t)
    r1=h*f(x[i-1])[2]
    r2=h*f(x[i-1]+r1/2)[2]
    r3=h*f(x[i-1]+r2/2)[2]
    r4=h*f(x[i-1]+r3)[2]
    x[i]=x[i-1]+1/6*(r1+2*r2+2*r3+r4)    

#plt.figure(1)       
#plt.plot(t[0:len(t)-1],y[0:len(t)-1])
#plt.plot(t[0:len(t)-1],x[0:len(t)-1])
#plt.xlabel('t')
#plt.ylabel('y')  
#showing the projectile motion 
plt.figure(1)
plt.plot(x[0:len(t)-1],y[0:len(t)-1])
plt.axvline(x=0)
plt.axhline(y=0)
plt.xlabel('x')
plt.ylabel('y') 
plt.show()
