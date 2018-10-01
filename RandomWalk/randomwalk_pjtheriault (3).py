#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Written by Paul Theriault
#The purpose of this program is to simulate random motion
import math 
import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#Problem I
#Particle can either move to the left or to the right
#We'll let -1 be to the left and +1 to the right

Nsteps = int(input('Please enter the amount of steps you want: '))
Exp = int(input('Please enter the amount of trials to run: '))
z_array =[]
a_array=[]
for steps in range(1, Nsteps):
        for exp in range(1, Exp):
            i = 0
            x = 0 #inital condition at origin 
            while(i <= steps):
                x += random.choice([-1,1]) #Picks a value -1 or 1
                i+=1
            z_array.append(np.abs(x)) #Adds absolute value of x to an array
        a_array.append((np.mean(z_array))) #Finds the mean of the array
plt.title('1D Random Walk')
plt.xlabel('Number of Steps')
plt.ylabel('Average Distance')
plt.plot(a_array,'r');
plt.show()
#The code is not very optimal give it some time to plot if you run many trials 
#Would not recommend more than 1000 unless you like waiting
#################################################################################################################################

#Problem II
#We now have a particle that is 3 times as likely to move left than to move right
#The only thing we really change here is the random.choice selections
P_array=[]
S_array=[]
for steps in range(1, Nsteps):
        for exp in range(1, Exp):
            i = 0
            x = 0 #inital condition at origin 
            while(i <= steps):
                x += random.choice([-1,1,-1,-1]) #Picks a value -1 or 1 but 3/4 of the time it's -1
                i+=1
            P_array.append(np.abs(x)) #Adds absolute value of x to an array
        S_array.append((np.mean(P_array))) #Finds the mean of the array
plt.title('1D Biased Walk')
plt.xlabel('Number of Steps')
plt.ylabel('Average Distance')
plt.plot(S_array,'r');
plt.show()
#Again give the code some time to run
#Expect this to take about a minute for 1000 trials
#################################################################################################################################

#Final comments
#The graphs make sense for the problems they are simulating 
#I noticed compared to other peoples graphs that mine smooths out a lot faster and I'm not certain why


# In[ ]:




