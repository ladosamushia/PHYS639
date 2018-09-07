
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Problem 1 of the Warmup
N0 = 10
tau = 703.8
tini = 0
tfin =10*tau
Nsteps = 10000


# In[3]:


t = np.linspace(tini,tfin,Nsteps+1)
N = np.zeros(Nsteps+1)
N[0] = N0
dt = (tfin - tini)/Nsteps


# In[4]:


for i in range(1,Nsteps+1):
    dN = -N[i-1]/tau
    N[i] = N[i-1] + dN*dt


# In[5]:


plt.plot(t,N, 'go')
plt.plot(t,N0*np.exp(-t/tau), 'y-')
plt.xlabel('time in millions of years')
plt.ylabel('Number of atoms in N_A')


# In[6]:


#Problem 2 of the Warmup
#we want  dN/dt = aN + bN^2
#Inital conditions
S0 = 1 #Inital Population
a=10
b=15
Ssteps = 1000
rini = 0
rfin = 2


# In[7]:


r = np.linspace(rini,rfin,Ssteps+1)
S = np.zeros(Ssteps+1)
S[0]=S0 #Inital Population plugged plt.plot(r,S, 'y'in
#We need some sort of delta change / steps
dr = (rfin - rini)/Ssteps


# In[8]:


for i in range(1,Ssteps+1):
    dS = a*S[i-1]-b*S[i-1]**2
    S[i] = S[i-1]+dS*dr


# In[9]:


plt.plot(r,S, 'oy')
plt.plot(r,(a*np.exp(a*r)*S0)/(a-b*S0+b*np.exp(a*r)*S0), 'r')
plt.xlabel('Time in Years')
plt.ylabel('Population')

