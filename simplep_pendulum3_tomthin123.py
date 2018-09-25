#angle Vs time
import matplotlib.pyplot as plt 
import numpy as np
tini=0
tfin=20
Nsteps=5000
y0=0#initial position
vy0=1#initial velocity
g=9.8
l=.5#length of pendulum
q=.8#drag coefficient
F0=1.5#Forced parameter max amplitude
om=4.42#set near to natural frequency for resonance
vy=np.zeros(Nsteps+1)
y=np.zeros(Nsteps+1)
y[0]=y0
vy[0]=vy0
h=abs(tini-tfin)/Nsteps
t=np.linspace(tini,tfin,Nsteps+1)
def s(omeg):
    def f(x1,x2,x3):
        y1=-(g/l)*np.sin(x1)-q*x2+F0*np.sin(omeg*x3)
        y2=x2
        #y3=-(g/l)*x1
        return y1,y2
    for i in range(1,Nsteps):
        #k's is the runge kutta coefficients for omega 
        #l's is the runge-kutta coefficients for angle(theta) w/o approx.
        #d's is the runge-kutta coefficients for angle(theta) with approx.
        k1=h*f(y[i-1],vy[i-1],t[i-1])[0]
        l1=h*f(0,vy[i-1],0)[1]
        k2=h*f(y[i-1]+l1/2,vy[i-1]+k1/2,t[i-1]+h/2)[0]
        l2=h*f(0,vy[i-1]+k1/2,0)[1]
        k3=h*f(y[i-1]+l2/2,vy[i-1]+k2/2,t[i-1]+h/2)[0]
        l3=h*f(0,vy[i-1]+k2/2,0)[1]
        k4=h*f(y[i-1]+l3,vy[i-1]+k3,t[i-1]+h)[0]
        l4=h*f(0,vy[i-1]+k3,0)[1]
        y[i]=y[i-1]+1/6*(l1+2*l2+2*l3+l4)#angle vs time array
        vy[i]=vy[i-1]+1/6*(k1+2*k2+2*k3+k4) #omega vs time array
    return y
forcing_freq=np.linspace(0,10,50)
y00=np.zeros(50+1)
for j in range(0,len(forcing_freq)):
    y00[j]=np.amax(s(forcing_freq[j]))
plt.figure(1)
plt.plot(t[0:len(t)-1],s(om)[0:len(t)-1],label=('angle vs time w/o approx.+damping+forcing'))
plt.xlabel('time(s)')
plt.ylabel('angle(radians)')
plt.legend(loc='upper right')  
plt.figure(2)
plt.plot(forcing_freq[0:len(forcing_freq)-1],y00[0:len(forcing_freq)-1],label=('max. amplitude Vs frequency [max expected around=4.42]'))
plt.xlabel('forcing freqeuncy(1/s)')
plt.ylabel('angle_max(radians)')
plt.legend(loc='upper right')
plt.show()
