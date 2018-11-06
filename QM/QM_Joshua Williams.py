#Schrodingers equation infinite well, find eigenvalues, energy states.

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as random
#simpler method
hbar=1#plancks constant
n=1#starting energy state
N=5#final energy state
m=1#mass
n_steps=2000
x=np.linspace(0,1,int(n_steps)+1)
#x0=0
dx=1/n_steps
dE=.1
E=dE
psi=0#initial wave value
#dpsi=1
ddpsi=0
Fpsi=[1,2,3]#final wave value

while n <= N:
    psi=np.zeros(int(n_steps)+1)
    dpsi=1
    
    for i in range(int(n_steps)+1):
        psi[i] = psi[i] + dpsi*dx
        dpsi -= 2 * E*psi[i]*dx
        
    Fpsi.append(np.abs(psi[-1]))
    
    if Fpsi[-3] >=  Fpsi[-2]<= Fpsi[-1]:
        print('Energy state: %d: %.1f'%(n, E-dE))#print values of E
        plt.plot(x,psi)
        plt.ylabel('psi')
        plt.xlabel('x')
        plt.title('probability distrobution functions')
        n+=1
    E+=dE
    
#Energy states always 0.
#plot always some linear function which is sort of expected for an energy vs energy state graph
#we would expect a sinusoidal wave for the probability function however.
#I think I fixed it, but I can't run it on my computer

##################VESTIGAL CODE 
##def psi(x)?
## #def psi(n):
##     return -.5 * psy / E
##     x=0
##     x = [x]
##     x=np.array[x]
##     n=np.array[n]
    
    
# def Schro(Psi,E,m,V): #Schrödinger equation
#     ddPsi=-((E-V)*Psi)*((2*m)/hbar**2)
#     return ddPsi
# E_list=[] #list of energy levels
# N=[] #list of energy level values
# Psi_list=[] #list of psi values
# Psi_array=np.zeros(n_steps) 
# dPsi_array=np.zeros(n_steps)
# Emax=200#maximum energy value
# while E<Emax
#     psi=0
#     dpsi=dPsi + ddPsi*dx
#     ddPsi= Schro(Psi,E,m,V)
#     Psi_array[i]=Psi
#     dPsi_array[i]=dPsi
    
    
    
    
    
    
    
    
      
