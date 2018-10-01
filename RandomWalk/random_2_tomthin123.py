import numpy.random as random  
import matplotlib.pyplot as plt
import numpy as np
aa=[-1,-1,-1,1]
#np.size(aa[aa==1])
Nexp=0
n=1000
step_max=100
fpos=np.zeros(n+1)
posNstep=np.zeros(step_max+1)
Nstep_array=np.linspace(0,step_max+1,101)
print(posNstep.size)
while Nexp<=n:
    pos=0#set the position to zero again
    Nsteps=0#set number of steps to zero
    while Nsteps<=step_max: 
        c=random.choice(aa)
        pos=pos+c
        posNstep[Nsteps]+=abs(pos)
        Nsteps=Nsteps+1
    fpos[Nexp]=abs(pos)
    Nexp=Nexp+1
    #print(Nexp)
#print(np.mean(fpos))
print(posNstep)
posNstep=posNstep/Nexp
print(posNstep)
plt.plot(Nstep_array,posNstep,label="Number of Steps Vs avg. abs Position")   
plt.xlabel('Steps')
plt.ylabel('Average Abs position')
plt.show()