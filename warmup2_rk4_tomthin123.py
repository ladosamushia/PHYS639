import matplotlib.pyplot as plt 
import numpy as np
tini=0#initial time
tfin=10#final time
Nsteps=1000# accuracy 
N0=0.1#initail population
alpha=.9#growth rate
beta=.4#death rate
N=np.zeros(Nsteps+1)#initializing population(solution) array
N[0]=N0
h=abs(tini-tfin)/Nsteps#stepsize crucial for stability
t=np.linspace(tini,tfin,Nsteps+1)#time array
#defining the function f in y'=f(y,t) of IVP
#Rk4 is a much stable scheme for this type of non-linear ode's
def f(x):
    y=x*alpha-beta*(x**2)
    return y
for i in range(1,Nsteps):
    k1=h*f(N[i-1])
    k2=h*f(N[i-1]+k1/2)
    k3=h*f(N[i-1]+k2/2)
    k4=h*f(N[i-1]+k3)
    N[i]=N[i-1]+1/6*(k1+2*k2+2*k3+k4)
    #print(N[i],t[i])
plt.plot(t[0:len(t)-1],N[0:len(t)-1])#getting rid of one extra point
plt.xlabel('time')
plt.ylabel('population')  
plt.show()
# solution here is for N with time goes stble with these parameters above but since the ode is
#non-linear hence couldn't say much it can change drastically with alpha, beta and initial value.