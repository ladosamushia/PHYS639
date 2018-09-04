# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 22:30:41 2018

@author: Joshua Williams
"""

#radio active decay
#numerically solve the diffy q dN/Ni=-dt/tao
#graph the dependence of N on time
#N is the number of U-235 in a sample tao is half-life=702.8million years
import numpy as np
import matplotlib.pyplot as plt
  
tao = 702.8  
Ni=100
n=10000
ti=0
tf=10*tao

    
t=np.linspace(ti,tf,n+1)
N=np.zeros(n+1)
N[0]=Ni
dt=(tf-ti)/n
    
for i in range(1,n+1):
        dN=-N[i-1]/tao
        N[i]=N[i-1]+dN*dt
        
plt.figure(1)
plt.title('U-235 atoms dependence on time')
plt.plot(t,N)
plt.xlabel('t(millions of years)')
plt.ylabel('U-235 atoms')
####
#population growth problem
#dN/dt=alphaN-betaN^2
#alpha is births, beta is deaths, and N is population (initial?) number
#solve for Different values of alpha, beta and N
Ni=10 #initial pop
alpha=1
beta=.01

#basically copied from warmup1
ti=0
tf=100

n=10000 
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(ti,tf,n+1)
N=np.zeros(n+1)
N[0]=Ni
dt=(tf-ti)/n

for i in range(1,n+1):
    dN=alpha*N[i-1]-beta*(N[i-1]**2)
    N[i]=N[i-1]+dN*dt
    
plt.figure(1)
plt.title('Please work')
plt.plot(t,N)
plt.xlabel('Some unit of time')
plt.ylabel('population')
    #keep getting overflow graph not working
    #fiddled with initial conditions seems to work now
    #From the graph it would seem that population changes until it reaches some
    #maximum. Concievably this is where the two terms from our population dynamics equation,
    #are equal. Assuming I am not doing something horribly wrong this is what my graph seems to corroborate.
    
    #####
    #problem3
#coupled decay boogaloo
#A,B are radioactive isotopes, B decays to A s.t. there are lots of A and very few B
#dNa/dt=-Na/taoa, dNb/dt=Na/taoa-Nb/taob
#solve numerically and graph numbers as funtions of time. do so for different values of taoa taob
# explan results
import numpy as np
import matplotlib.pyplot as plt
N_Ai=100
N_Bi=200
tao_A=200
tao_B=200
ti=0
tf=100
n=10000
t=np.linspace(ti,tf,n+1) #ctrl c ctrl v from 1

N_A=np.zeros(n+1)
N_B=np.zeros(n+1)
N_A[0]=N_Ai
N_B[0]=N_Bi

dt=(tf-ti)/n
for i in range(1,n+1):
    dN_A=-N_A[i-1]/tao_A
    dN_B=N_A[i-1]/tao_A-N_B[i-1]/tao_B
    N_A[i]=N_A[i-1]+dN_A*dt
    N_B[i]=N_B[i-1]+dN_B*dt
    
plt.figure(1)
plt.title('Decay products')
plt.plot(t,N_A)
plt.plot(t,N_B,'b-')
plt.xlabel('Some unit of time')
plt.ylabel('population')
#From my graph A looks to be simply decaying, which should be wrong as B which has a comparably fast
#decay rate should add to N_A. B rapidly decays, as it should, but it does not correspond to an increase in N_A, as we had ought to expect
#I have no idea what I am doing wrong.
#####
#Problem 4 Coupled decay boogaloo: the last half-life
# same as before but dna/dt=Nb/t-Na/t, dnb/dt-na/t-nb/t
#above t is tao
# solve numerically and graph, explan results
import numpy as np
import matplotlib.pyplot as plt
N_Ai=100
N_Bi=100
tao_A=5
tao_B=2
ti=0
tf=100
n=10000
#from 3
t=np.linspace(ti,tf,n+1)
N_A=np.zeros(n+1)
N_B=np.zeros(n+1)
N_A[0]=N_Ai
N_B[0]=N_Bi
dt=(tf-ti)/n

for i in range(1,n+1):
    dN_A= N_B[i-1]/tao_B-N_A[i-1]/tao_A
    dN_B= N_A[i-1]/tao_A-N_B[i-1]/tao_B
    N_A[i]= N_A[i-1]+dN_A*dt
    N_B[i]= N_B[i-1]+dN_B*dt

plt.figure()
plt.title('Decay products')
plt.plot(t, N_A)
plt.plot(t, N_B, 'b-')
plt.xlabel('Time')
plt.ylabel('population')
#according to my graph A does not decay, although B does, and B decays to A which properly adds to the population of A
#Both populations appear to be limited in their capacities to increase in number or decay, to to the coupled equations limiting these behaviours.

#Finished