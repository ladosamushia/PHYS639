# -*- coding: utf-8 -*-
"""


@author: Mikelobe
"""

import numpy as np
import matplotlib.pyplot as plt

#1 Quantum Well

hbar=1 #Plancks constant
m=1 #mass
steps=1000 #step size
L=1 #length of well
V=0 #Potential of well
Psi=0 #initial wave function value
dPsi=1 #initial derivative wave function value
ddPsi=0 #initial second derivative wave function value
n0=0 #initial energy level
x0=0 #initial position
margin=0.00000001 #about 0 that helps determine energy levels
E=4.8 #initial energy
Emax=200 #final energy
dx=L/steps #small change in position
dE=0.01 #small change in energy

def Schrödinger(Psi,E,m,V): #Schrödinger equation
    ddPsi=-((E-V)*Psi)*((2*m)/hbar**2)
    return ddPsi
Actual_E=[] #list for Actual energy values from energy solution
E_list=[] #list for energy values from Schrödinger equation
N=[] #list for energy level values
Psi_list=[] #list for psi values
Psi_array=np.zeros(steps) #array for psi
dPsi_array=np.zeros(steps) #array for the derivative of psi

while E < Emax: #determines boundaries for the energy levels
    Psi=0
    dPsi=1
    for i in range(steps): #loop for second order differential Schrödinger equation
        Psi=Psi + dPsi*dx
        dPsi=dPsi + ddPsi*dx
        ddPsi= Schrödinger(Psi,E,m,V)
        Psi_array[i]=Psi
        dPsi_array[i]=dPsi
    previous=steps-2 #these determine the two boundaries to try to find a 0 point
    final=steps-1
    if (Psi_array[previous]<margin and Psi_array[final]>-margin or Psi_array[previous]>margin and Psi_array[final]<-margin):
#determine 0 points
        Psi_list.append(Psi)
        E_list.append(E)
        N.append(1)
        E=E+(0.25*E) #I got this from Zane which helps speed up the processing which works because we know
        #after we find a energy level there shouldn't be another one for a little bit
        plt.figure(1)
        plt.plot(Psi_array)
        plt.xlabel("Position from Nucleus")
        plt.ylabel("Psi/Wave Function")
        plt.title("Wave Function")
        plt.figure(2)
        plt.plot((Psi_array)**2)
        plt.xlabel("Position from Nucleus")
        plt.ylabel("ddPsi/Probability")
        plt.title("Probability")
    else:
        E=E+dE
def E_Solution(n,m,l): #actual energy solution to the Schrödinger equation
    E= ((n*np.pi*hbar)**2)/(2*m*(l**2))
    return E
length=len(N)
for i in range(length): #loop for actual energy solution to the Schrödinger equation
    E_N=E_Solution((i+1),m,L)
    Actual_E.append(E_N)
plt.figure(3) #graph displaying actual energy versus energy we approximated
plt.plot(Actual_E,'b-')
plt.plot(E_list,'y-')
plt.xlabel("Energy Level")
plt.ylabel("Energy")
