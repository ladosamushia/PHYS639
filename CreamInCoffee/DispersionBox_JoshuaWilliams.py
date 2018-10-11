#problem 1 cream in coffee.
import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

npart=400#number of particles
L=200#box size
#d=1 #step distance
step=1000000
partl=[npart]
partn=npart

x=[L/2]*npart
y=[L/2]*npart

for i in range(int(step)):
    p=random.randint(npart)#selects a particle
    dash=random.randint(4)#moves it in the following directions
    #following defined in class
    if dash==0 and x[p]>0:
        x[p]-= 1#-xdir
    elif dash == 1 and x[p]<L:
        x[p]+=1#xdir
    elif dash == 2 and y[p] > 0:
        y[p]-=1
    elif dash == 3 and y[p] <L:
        y[p] += 1
    partl.append(partn)
    
plt.figure(1)
plt.title('Cream in coffee mug: Step = %.2E' %(i+1))
plt.plot(x,y,'.')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0,L)
plt.ylim(0,L)
#For 100000 steps the particles spread about a maximum of 50, but speads
#as one would expect for more steps. 

plt.figure(2)
plt.title('Population vs time')
plt.plot(range(int(step+1)),partl)
plt.ylabel('Pops')
plt.xlabel('Steps')
#This is more for the other problems. Pop remains at 400 as expected
#################################################
#Hole in box
npart=400#number of particles
L=200#box size
#d=1 #step distance
step=1000000
partl=[npart]
partn=npart

x=[L/2]*npart
y=[L/2]*npart
hole=40
for i in range(int(step)):
    p=random.randint(npart)#selects a particle
    dash=random.randint(4)#moves it in the following directions
    #following defined in class
    if dash==0 and x[p]>0:
        x[p]-= 1#-xdir
    elif dash == 1 and x[p]<L:
        x[p]+=1#xdir
    elif dash == 2 and y[p] > 0:
        y[p]-=1
    elif dash == 3 and y[p] <L:
        y[p] += 1
    if x[p] == 0 and (L-hole)/2 <= y[p] <= (L+hole)/2:
        #partl.remove(partn)#I remove points that reach the hole from the list. Not working.
        x[p]=100000000#Can't delete so I send away
        partn-=1
    partl.append(partn)
    
plt.figure(3)
plt.title('Cream in coffee mug: Step = %.2E' %(i+1))
plt.plot(x,y,'.')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0,L)
plt.ylim(0,L)
 

plt.figure(4)
plt.title('Population vs time')
plt.plot(range(int(step+1)),partl)
plt.ylabel('Pops')
plt.xlabel('Steps')
#Pop v step graph makes sense. Only lose 2 particles over 1million steps.
#Initially I tried removing the particles that reach the hole from the list partl entirely
#this failed so I just sent it very, very far away.
#########################################
#Problem 3: Escape from the Box 2: Electric Boogaloo starring Kurt Russell
# same (basic code) as above but averaged so I copy the same code as above
npart=400#number of particles
L=200#box size
#d=1 #step distance
step=1000000
hole=40
#need arrays for average particles and average lists, need experiment number as well
experiments=10

npartl=[]
partavg=[]


for i in range(int(experiments)):
   x=[L/2]*npart
   y=[L/2]*npart
   
   partl=[npart]
   partn=npart
   
   for j in range(step):#adding another loop for 
         p=random.randint(npart)#selects a particle
         dash=random.randint(4)#moves it in the following directions
    #following defined in class
         if dash==0 and x[p]>0:
            x[p]-= 1#-xdir
         elif dash == 1 and x[p]<L:
            x[p]+=1#xdir
         elif dash == 2 and y[p] > 0:
            y[p]-=1
         elif dash == 3 and y[p] <L:
            y[p] += 1
         if x[p] == 0 and (L-hole)/2 <= y[p] <= (L+hole)/2:
        #partl.remove(partn)#I remove points that reach the hole from the list. Not working.
            x[p]=100000000#Can't delete so I send away
            partn-=1#take 1 from partn
         partl.append(partn)
    
   npartl.append(partl)
#need to add loop to find the avg over the previous loop
for i in range(int(step+1)):
    list1=[]
    for j in npartl:
        list1.append(j[i])
    iav=np.mean(list1)
    partavg.append(iav)
    
plt.figure(5)
plt.title('Average Particle loss')
plt.plot(range(int(step+1)),partavg)
plt.xlabel('Steps')
plt.ylabel('Number of Particles')
#The Average Particle loss graph shows a total loss of 1 particles,
#The graph is similar to the previous problem, but shows the loss of the particle at different steps.
        