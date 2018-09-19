import matplotlib.pyplot as plt 
import numpy as np
tini=0
tfin=15
Nsteps=1000
x0=0
y0=0
vy0=10
vx0=5
a=-9.8
b=1
b1=1
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

def f(x1,x2,x3):
    y1=a-b1*.00004*(x1**2)*(.000022*x3)**2.5
    y2=x1
    y3=x2
    y4=-b*.00004*(x2**2)*(.000022*x3)**2.5
    return y1,y2,y3,y4
for i in range(1,Nsteps):
#changing the drag direction
    if vy[i]<0:
        b1=-1
    if vx[i]<0:
        b=0   
#calculating vy(t)
    k1=h*f(vy[i-1],0,y[i-1])[0]
    l1=h*f(vy[i-1],0,0)[1]
    k2=h*f(vy[i-1]+k1/2,0,y[i-1]+l1/2)[0]
    l2=h*f(vy[i-1]+k1/2,0,0)[1]
    k3=h*f(vy[i-1]+k2/2,0,y[i-1]+l2/2)[0]
    l3=h*f(vy[i-1]+k2/2,0,0)[1]
    k4=h*f(vy[i-1]+k3,0,y[i-1]+l3)[0]
    l4=h*f(vy[i-1]+k3,0,0)[1]
    vy[i]=vy[i-1]+1/6*(k1+2*k2+2*k3+k4)
    
#calculating y(t) 
    y[i]=y[i-1]+1/6*(l1+2*l2+2*l3+l4)
#calulating vx(t)
    e1=h*f(0,vx[i-1],y[i-1])[3]
    e2=h*f(0,vx[i-1]+e1/2,y[i-1]+l1/2)[3]
    e3=h*f(0,vx[i-1]+e2/2,y[i-1]+l2/2)[3]
    e4=h*f(0,vx[i-1]+e3,y[i-1]+l3)[3]
    vx[i]=vx[i-1]+1/6*(e1+2*e2+2*e3+e4)    
#calulating x(t)
    r1=h*f(0,vx[i-1],0)[2]
    r2=h*f(0,vx[i-1]+e1/2,0)[2]
    r3=h*f(0,x[i-1]+e2/2,0)[2]
    r4=h*f(0,vx[i-1]+e3,0)[2]
    x[i]=x[i-1]+1/6*(r1+2*r2+2*r3+r4)
    #print(vy[i])
    if y[i]<0.05:
        break 
#plt.figure(1)       
#plt.plot(t[0:len(t)-1],y[0:len(t)-1])
#plt.plot(t[0:len(t)-1],x[0:len(t)-1])
#plt.xlabel('t')
#plt.ylabel('y')  
#showing the projectile motion 
plt.figure(1)
plt.plot(x[0:len(t)-1],y[0:len(t)-1],label='with drag scaled by air density effects')
plt.axvline(x=0)
plt.axhline(y=0)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right') 
plt.show()
