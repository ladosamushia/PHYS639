import numpy.random as random  
import matplotlib.pyplot as plt
import numpy as np
di=np.array(['x','y','z'])
x=[-1,1]
y=[-1,1]
z=[-1,1]
#np.size(aa[aa==1])
Nexp=0
n=1000
step_max=100
fpos=np.zeros(n+1)

Nstep_array=np.linspace(0,step_max+1,step_max+1)
#print(posNstep.size)
#print(Nstep_array.size)
def dist(x):
    c1=x*x
    s=(c1[:,0]+c1[:,1]+c1[:,2])
    su=np.sqrt(s)
    return su 
ss=np.zeros(step_max+1)    
while Nexp<=n:
    posx=0#set the positionx to zero again
    posy=0#set the positiony to zero again
    posz=0#set the positionz to zero again
    Nsteps=1#set number of steps to zero
    posNstep=np.zeros((step_max+1,3))
    #print(type(ch),ch)
    while Nsteps<=step_max: 
        ch=random.choice(di)
        if ch=='x':
            nx=random.choice(x)
            posx=posx+nx
            posNstep[Nsteps,0]+=(posx)
            posNstep[Nsteps,1]=posNstep[Nsteps-1,1]
            posNstep[Nsteps,2]=posNstep[Nsteps-1,2]
        elif ch=='y':
            ny=random.choice(y)
            posy=posy+ny
            posNstep[Nsteps,0]=posNstep[Nsteps-1,0]
            posNstep[Nsteps,1]+=(posy)
            posNstep[Nsteps,2]=posNstep[Nsteps-1,2]
        elif ch=='z':
            nz=random.choice(z)
            posz=posz+nz
            posNstep[Nsteps,0]=posNstep[Nsteps-1,0]
            posNstep[Nsteps,1]=posNstep[Nsteps-1,1]
            posNstep[Nsteps,2]+=(posz)   
        Nsteps=Nsteps+1
    #fpos[Nexp]=abs(pos)
    ss=dist(posNstep)+ss
    Nexp=Nexp+1
    
plt.plot(Nstep_array,ss/Nexp,label="Number of Steps Vs Avg. distance from origin")   
plt.xlabel('# of Steps')
plt.ylabel('Average distance from (0,0) ')
plt.show()