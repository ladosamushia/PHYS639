#Problem 1 random walk
import numpy.random as random
import numpy as np
import matplotlib.pyplot as plt
n=100 #number of steps
trial=1000 #number of trials
#need to define function for average distance
def avgd(step,trial):
    D=[]#modulus array for data
    
    for i in range(trial):#loop for trial and step respectively
        x=0#start at origin
        
        for j in range(step):
            x+=random.choice([-1,1])#random step either 1 or -1
        
        D.append(np.abs(x))
    return np.mean(D)#gives average distance

d=[]

for step in range(n):
    d.append(avgd(step, trial))
    
plt.figure(1)
plt.title('Random Walk on the Whole line')
plt.xlabel('Steps')
plt.ylabel('Average distance traveled')
plt.plot(range(n),d)
#Because everytime you step you essentially flip a coin there is, for any step,
#an equal probability to move in either direction along the line. It would make
#sense that the average distance traveled increased with the number of steps, as
#it would be unlikely, in aggragate, to remain in the same position.
#The plot I managed to make appears to have a logarithmic form.
###########################################
#problem 2 Weighted random walk, that is 3 times more likely for negative movement than positive.
#same values as before for ease
n=100
trial=1000
def avgd(step,trial):
    D=[]
    
    for i in range(trial):
        x=0
        
        for j in range(step):
            x+=random.choice([-1,-1,-1,1])#Here is the weight, three negatives vs. 1 positive
        
        D.append(np.abs(x))
    return np.mean(D)

d=[]

for step in range(n):
    d.append(avgd(step,trial))

plt.figure(2)
plt.plot(range(n),d)
plt.title('Weighted walk on the whole line')
plt.xlabel('steps')
plt.ylabel('average distance traveled')
#The heavy weight on a negative movement allows for the far greater average distance traveled 
#in comparison to the first graph.
#The graph appears to be of a linear form.
######################################################################
#problem 3 3d random walk
#This problem will have the same basic form as above
n=100
trial=1000

def avgd(step,trial):
    D=[]
    for i in range(trial):
        (x,y,z)=(0,0,0)
        for j in range(step):
            #3step=random.choice([0,1,2,3,4,5])
            bigstep=random.choice(range(6))
            if bigstep == 0:#x-axis positive step
                x+=1
            elif bigstep == 1:#x negative step
                x-=1
            elif bigstep == 2: #y pos. step
                y+=1
            elif bigstep == 3:#y neg
                y-=1
            elif bigstep == 4:#z pos
                z+=1
            elif bigstep == 5:#z neg
                z-=1
        D.append(np.sqrt(x**2+y**2+z**2))#distance in 3space
    return np.mean(D)

plt.figure(3)
plt.plot(range(n),d)
plt.xlabel('Step')
plt.ylabel('avg. dist.')
plt.title('3space shuffle')
#Basically copy of previous problem. I ran it in another window and the graph
#remains the same