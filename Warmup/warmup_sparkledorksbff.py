import numpy as np
import matplotlib.pyplot as plt

#For this problem we are attempting to determine how the radioactive isotope Uranium-235 changes with time.  We will numerically solve the equation and graph the dependence of the number of isotopes on time

N0 = 10 #number of Uranium-235 in a sample
tau = 703.8 #half-life of Uranium-235 in millions of years
t0 = 0 #initial time in years
tfin = 10*tau #final time in years
Nsteps = 10000 #the number of steps for our graph for accuracy

t = np.linspace(t0,tfin,Nsteps+1) #the time that we will plot the change in N against
N = np.zeros(Nsteps+1) #the change in N that we will plot
N[0] = N0 #initial number of Uranium-235
dt = (tfin-t0)/Nsteps #time derivative

for i in range(1,Nsteps): #defining the function
    dN = - N[i-1]/tau #our equation:  how N changes with respect to time
    N[i] = N[i-1] + dN*dt #N in the range of i

plt.plot(t,N,'go') #This is where we plot N vs. t
plt.plot(t,N0*np.exp(-t/tau),'y-') #This creates a plot of the expected solution


#For this code we are trying to graph how the population of certain rodents changes with births and deaths over time.

a = 1 #birth coefficient
b = 1 #death coefficient
N0 = 10 #initial population
t0 = 0.0 #initial time in years
tfin = 10.0 #final time in years
Nsteps = 1000 #the number of steps on our graph

t = np.linspace(t0,tfin,Nsteps+1) #this is the time that we will plot N against
N = np.zeros(Nsteps+1) #this is the N that we will plot
N[0] = N0 #definition of the initial population
dt = (tfin-t0)/Nsteps #change in time

for i in range(1,Nsteps+1): #defining the equation we want to solve
    dN = ((a*N[i-1]) - (b*((N[i-1])**2))) #this is the differential equation that defines how population changes over time
    N[i] = N[i-1] + dN*dt #defining N in the range of i

plt.plot(t,N,'go') #here we will plot N vs. t to prove our results

#Here we have two isotopes:  A and B, where B decays into A and A decays into something else.  If there is a lot of A and little of B, the decay rate is faster, and vice versa.
#We want to solve our differential equations for the decay rates of A and B numerically and graph how each decays with respect to time

tA0 = 0.0 #initial time for A in years
tB0 = 0.0 #initial time for B in years
NA0 = 5 #initial number of A isotopes
NB0 = 500 #initial number of B isotopes
tAF = 2000000.0 #final time for A in years
tBF = 2000000.0 #final time for B in years
tauA = 1000 #half-life for A in millions of years
tauB = 90000 #half-life for B in millions of years
Nsteps = 100 #number of steps for our graph

tA = np.linspace(tA0,tAF,Nsteps+1) #time for A that we will plot
tB = np.linspace(tB0,tBF,Nsteps+1) #time for B that we will plot
NA = NB = np.zeros(Nsteps+1) #how many steps to plot NA and NB with
NA[0] = NA0 #initial value for A
NB[0] = NB0 #initial value for B
dtA = (tAF-tA0)/Nsteps #time derivative for A
dtB = (tBF-tB0)/Nsteps #time derivative for B

for i in range(1,Nsteps+1): #defining our differential equations
    dNA = - (NA[i-1]/tauA) #how A decays
    NA[i] = NA[i-1] + (dNA*dtA) #defining A in range of i
    dNB = (NA[i-1]/tauA) - (NB[i-1]/tauB) #how B decays into NA
    NB[i] = ((NA[i]) - NB[i-1]) + dNB*dtB #defining B in range of i

plt.plot(tA,NA,'go') #plotting A vs. time
plt.plot(tB,NB,'y-') #plotting B vs. time

#We will plot A and B on the same graph to see how each decays with respect to time

#This is the same code as the previous problem, except that the differential equations are coupled.
#Isotopes A and B decay into each other in this problem
#We want to solve this numerically and see how the isotopes decay with respect to time


tA0 = 0.0 #initial time for A in years
tB0 = 0.0 #initial time for B in years
NA0 = 5 #initial number of A isotopes
NB0 = 500 #initial number of B isotopes
tAF = 100.0 #final time for A in years
tBF = 100.0 #final time for B in years
tauA = 1000 #half-life of A in millions of years
tauB = 90000 #half-life of B in millions of years
Nsteps = 100 #the number of steps we want on our graphs

tA = np.linspace(tA0,tAF,Nsteps+1) #defining the time for A that we will plot
tB = np.linspace(tB0,tBF,Nsteps+1) #defining the time for B that we will plot
NA = NB = np.zeros(Nsteps+1) #defining the amount of steps to graph NA and NB according to
NA[0] = NA0 #the initial value of NA
NB[0] = NB0 #the initial value of NB
dtA = (tAF-tA0)/Nsteps #time derivative for NA
dtB = (tBF-tB0)/Nsteps #time derivative for NB

for i in range(1,Nsteps+1): #defining our differential equations that we want to solve
    dNA = (NB[i-1]/tauB) - (NA[i-1]/tauA) #derivative of NA:  how NA decays into NB
    NA[i] = NB[i] - NA[i-1] + (dNA*dtA) #NA in the range of i
    dNB = (NA[i-1]/tauA) - (NB[i-1]/tauB) #derivative of NB:  how NB decays into NA
    NB[i] = ((NA[i]) - NB[i-1]) + dNB*dtB #NB in the range of i

plt.plot(tA,NA,'go') #plot of NA vs. time
plt.plot(tB,NB,'y-') #plot of NB vs. time

#We will plot NA and NB on the same graph to see how they decay into each other with respect to time
