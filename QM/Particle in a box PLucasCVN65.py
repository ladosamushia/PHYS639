"""
Created on Wed Oct 31 2018 Created by Philip Lucas
Brute Force methode developed from inclass discussion
Particle in the Box with Linear Algebra Built from in-class demo by Jesse Laning
Made with Python 2.7
"""
# Lennard-Jones doesn't quite work right. 
import numpy as np
import matplotlib.pyplot as plt
numberofsteps = 4000 # exceeding 1000 breaks my low end laptop exceed
#at your own risk
print ""
print "Potential : Inputs "
print ""
print " 0 = Infinite Well (linear algebra)" , " 1 = Infinite Well (Brute Force) " , " 2 = Infinite Well with a Wall " , " 3 = Harmonic Potential " , " 4 = Lennard-Jones "  
B = int(input("Potential :"))
print ""
N = 5 # number of waves you want to see 
nd = 5 #number of decimal places to round solution to 
m = 1
L = 1
x = np.linspace(-0.5, 0.5, numberofsteps)
xLJ = np.linspace(0.1, 10, numberofsteps )
dx = x[1] - x[0]
E_a = []
V = np.zeros(numberofsteps)
A = np.zeros((numberofsteps, numberofsteps)) # Matrix Size and memory allotment 
dx2_inv = 1/(dx**2)
if B < 1 or B > 1:
    for i in range(numberofsteps): # matrix solution
        if B == 0 or B > 4: #infinite Well
            V[i] = 0
        if B == 2: #infinite Well with wall 
            if i > 449 and i < 550:
                V[i] = 500 # to be noticable increase V to hundereds
        if B == 3:
            V[i] = ((i - numberofsteps/2)**2)*dx*0.5 # harmonic oscilator 
        if B == 4: 
            V[i] = (10*(((1/(xLJ[i])**12)-((1/(xLJ[i]))**6)))*dx*0.5) # Lennard Jones Potential
        for j in range(numberofsteps):
            if i == j:
                A[i][j] = dx2_inv + + V[i]
            if i == j - 1 or i == j + 1:
                A[i][j] = -dx2_inv*0.5
# compute eigen values and eigen vectors
E, psi_t = np.linalg.eigh(A)
# take the transpose of psi_t to the wavefunction vectors can accessed as psi[n]
psi = np.transpose(psi_t)
if B == 0: 
    print "Infinite Well solutions" , "(No Wall):"
    for i in range(1, numberofsteps + 1):
        E_a.append(((i**2)*np.pi**2)/2)
    for i in range(1, N+1):
        print "Approximate v. Actual ", " E( n =",i,"):",  round(E[i], nd) ," v. ", round(E_a[i], nd)
    for i in range(N):
        plt.figure(1)
        plt.xlabel (" Position " " L/step " )
        plt.ylabel (" Psi ")
        plt.title (" Wavefunction: (Infinite Square Well No Wall) ")
        plt.plot(-psi[i])
        plt.figure(2)
        plt.plot((psi[i])**2)
        plt.xlabel (" Position " " (L)/step ")
        plt.ylabel (" P(x) = Psi**2 ")
        plt.title (" Probability: (Infinite Square Well No Wall )")
if B == 2: 
    for i in range(N):
        plt.figure(3)
        plt.xlabel (" Position " " L/step " )
        plt.ylabel (" Psi ")
        plt.title (" Wavefunction : (Infinite Square Well with a Finite Wall) ")
        plt.plot(-psi[i])
        plt.figure(4)
        plt.plot((psi[i])**2)
        plt.xlabel (" Position " " L/step ")
        plt.ylabel (" P(x) = Psi**2 ")
        plt.title (" Probability : (Infinite Square Well with a Finite Wall) ")
if B == 3: 
    for i in range(1, N+1):
        print "Energy Differences between En(i) - En(i+1)"
        print " E( n =",i,") - E( n =",i+1,"):", round(E[i] - E[i-1] , 2)
    for i in range(N):
        plt.figure(5)
        plt.xlabel (" Position " " L/step " )
        plt.ylabel (" Psi ")
        plt.title (" Wavefunction: Harmonic Potential ")
        plt.plot(psi[i])
        plt.figure(6)
        plt.plot((psi[i])**2)
        plt.xlabel (" Position " " L/step ")
        plt.ylabel (" P(x) = Psi**2 ")
        plt.title (" Probability : Harmonic Potential ")
if B == 4: 
    for i in range(N):
        plt.figure(7)
        plt.xlabel (" Position " " L/step " )
        plt.ylabel (" Psi ")
        plt.title (" Wavefunction: Lennard-Jones Potential ")
        plt.plot(psi[i])
        plt.figure(8)
        plt.plot((psi[i])**2)
        plt.xlabel (" Position " " L/step ")
        plt.ylabel (" P(x) = Psi**2 ")
        plt.title (" Probability : Lennard-Jones Potential ")
    for i in range(1, N+1):
        print "Approximate ", " E( n =",i,"):",  round(E[i], nd) 
if B == 1:
    steps = 1000
    E = []
    Energylist = []
    psilist = []
    N=[]
    L = 1.0
    n = 0 
    x = 0
    aboutzero = 0.00000001
    energy = 4.8
    ENERGY = 200
    step = 1000
    psi = np.zeros(step)
    dpsi = np.zeros(step)
    ddpsi = np.zeros(step)
    dx = L/step
    dE = 0.01
    while energy < ENERGY:
        dpsi = 1.0 
        ddpsi = 0.0
        for j in range(1,step):
            psi[j] = psi[j-1] + dpsi*dx
            ddpsi = -2*energy*psi[j-1] 
            dpsi += ddpsi*dx   
        if psi[998] < aboutzero and psi[999] > -aboutzero or psi[998] > aboutzero and psi[999] < -aboutzero:
            N.append(1)
            Energylist.append(energy)
            energy += (0.25)*energy
            plt.figure(7)
            plt.plot(psi)
            plt.xlabel (" Position " " L/step " )
            plt.ylabel (" Psi ")
            plt.title (" Wavefunction ")
            plt.figure(8)
            plt.plot(psi**2)
            plt.xlabel (" Position " " L/step ")
            plt.ylabel (" P(x) = Psi**2 ")
            plt.title (" Probability")
        else:
            energy += dE      
    # For comparision of  solutions to Test Code
    def E_n(n): #to validate a simple box
        return((n*np.pi)**2)/(2*(L)**2)
    Nrange = len(N)
    for k in range( 1, Nrange + 1 ): # for comparison with approximate PDE solution for a 1D infinite well
       E_n(k) 
       E.append(E_n(k))
    print "Analytical", E , ","
    print "Approximation" ,  Energylist
    plt.figure(9)
    plt.plot(E)
    plt.plot(Energylist)
    plt.xlabel (" n-Level (Unitless integer) ")
    plt.ylabel (" Energy(n) (eV) ")
    plt.title (" Energy level ")