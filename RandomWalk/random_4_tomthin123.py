import numpy.random as random  
import matplotlib.pyplot as plt
import numpy as np
theta=(np.linspace(0,180,1000))*(np.pi/180)
phi=(np.linspace(0,360,1000))*(np.pi/180)
#np.size(aa[aa==1])
Nexp=0
n=1000
step_max=100
r=1
#fpos=np.zeros(n+1)
ss=np.zeros(step_max+1)
Nstep_array=np.linspace(0,step_max+1,step_max+1)
def dist(x):
    c1=x*x
    s=(c1[:,0]+c1[:,1]+c1[:,2])
    su=np.sqrt(s)
    return su

#print(posNstep.size)
while Nexp<=n:
    Nsteps=1#set number of steps to zero
    posNstep=np.zeros((step_max+1,3))
    while Nsteps<=step_max: 
        th=random.choice(theta)#this is define wrt new basis after each step
        ph=random.choice(phi)#this is define wrt new basis after each step
        x=r*np.sin(th)*np.cos(ph)
        y=r*np.sin(th)*np.sin(ph)
        z=r*np.cos(th)
        #shifting the basis to find the coordinates wrt (0,0,0)
        posNstep[Nsteps,0]=posNstep[Nsteps-1,0]+x
        posNstep[Nsteps,1]=posNstep[Nsteps-1,1]+y
        posNstep[Nsteps,2]=posNstep[Nsteps-1,2]+z
        Nsteps=Nsteps+1
    ss=dist(posNstep)+ss
    Nexp=Nexp+1
    #print(Nexp)
plt.plot(Nstep_array,ss/Nexp,label="Number of Steps Vs Avg. Distance")   
plt.xlabel('#steps')
plt.ylabel('Average distance')
plt.show()