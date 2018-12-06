#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Problem1: Best Fit Values
import numpy as np
import matplotlib.pyplot as plt
# Borrow the given data set for N,Eand SN
Data= np.loadtxt('/Users/bhand/downloads/DataAnalysis.txt')
E=Data[:,0]   
N=Data[:,1]
SN=Data[:,2]

# Plot error bar for given set
plt.figure(1)
plt.errorbar(E,N,SN,fmt='o')
plt.xlabel('Energy')
plt.ylabel('Number of photons')
plt.title('Given data')

# Calculate best fit values A, E0, chi2
E0=np.linspace(0,20,100)
A=np.linspace(0,1,100)
chi2= np.zeros((100,100))         # 100*100 array for given set of E0 and A
for i in range(100):
    for j in range(100):
        Nth= 1+ A[j]*np.exp(-(E-E0[i])**2)  
        chi2[i][j]=np.sum((N-Nth)**2/SN**2)
    
print('Minimum chi2 is: ',np.min(chi2))
chi2min=np.min(chi2)              # minimum chi2 value
Likmax=np.exp(-chi2min/2)         # define likelihood
imin, jmin = np.where(chi2==np.min(chi2))
E0min=E0[imin[0]]
Amin=A[jmin[0]]
print('The minimum is at A= ',Amin)
print('The minimum is at E0= ',E0min)

# Plot best fit from best fit values of A,E0
plt.figure(2)
plt.plot(E,1+Amin*np.exp(-(E-E0min)**2))
plt.title('Best Fit')
plt.xlabel('Energy')
plt.ylabel('Number of Photons');


# In[4]:


#Problem2: Error-Bars
import numpy as np
import matplotlib.pyplot as plt
# Borrow the given data set for N,Eand SN
Data= np.loadtxt('/Users/bhand/downloads/DataAnalysis.txt')
E=Data[:,0]   
N=Data[:,1]
SN=Data[:,2]
E0=np.linspace(0,20,100)
A=np.linspace(0,1,100)
chi2= np.zeros((100,100))         # 100*100 array for given set of E0 and A
for i in range(100):
    for j in range(100):
        Nth= 1+ A[j]*np.exp(-(E-E0[i])**2)  
        chi2[i][j]=np.sum((N-Nth)**2/SN**2)
    
chi2min=np.min(chi2)              # minimum chi2 value
Likmax= -chi2min/2                # define likelihood
imin, jmin = np.where(chi2==np.min(chi2))
E0min=E0[imin[0]]                 # minimum E0
Amin=A[jmin[0]]                   # minimum A

# Calculate Hessian matrix
# First diagonal element= second order derivative of Log-likelihood wrt Amin
dA=0.01
A=Amin+dA
E0=E0min
Nth=1+A*np.exp(-(E-E0)**2)
chi2dAplus=np.sum((Nth-N)**2/SN**2)
LikdAplus= -chi2dAplus/2
A=Amin-dA
E0=E0min
Nth=1+A*np.exp(-(E-E0)**2)
chi2dAminus=np.sum((Nth-N)**2/SN**2)
LikdAminus=  -chi2dAminus/2
LikddA=-(LikdAplus+LikdAminus-2*Likmax)/dA**2
# Second diagonal element= second order derivative of Log-likelihood wrt E0min
dE0=0.2
A=Amin
E0=E0min+dE0
Nth=1+A*np.exp(-(E-E0)**2)
chi2dE0plus=np.sum((Nth-N)**2/SN**2)
LikdE0plus= -chi2dE0plus/2
A=Amin
E0=E0min-dE0
Nth=1+A*np.exp(-(E-E0)**2)
chi2dE0minus=np.sum((Nth-N)**2/SN**2)
LikdE0minus= -chi2dE0minus/2
LikddE0=-(LikdE0plus+LikdE0minus-2*Likmax)/dE0**2
# Off diagonal element= second order derivative of Log-likelihood wrt E0min and Amin
A=Amin+dA
E0=E0min+dE0
Nth=1+A*np.exp(-(E-E0)**2)
chi2dAE0plus=np.sum((Nth-N)**2/SN**2)
LikdAE0plus= -chi2dAE0plus/2
A=Amin-dA
E0=E0min-dE0
Nth=1+A*np.exp(-(E-E0)**2)
chi2dAE0minus=np.sum((Nth-N)**2/SN**2)
LikdAE0minus= -chi2dAE0minus/2
A=Amin+dA
E0=E0min-dE0
Nth=1+A*np.exp(-(E-E0)**2)
chi2dAE0plusminus=np.sum((Nth-N)**2/SN**2)
LikdAE0plusminus= -chi2dAE0plusminus/2
A=Amin-dA
E0=E0min+dE0
Nth=1+A*np.exp(-(E-E0)**2)
chi2dAE0minusplus=np.sum((Nth-N)**2/SN**2)
LikdAE0minusplus=-chi2dAE0minusplus/2
LikddAE0=-(LikdAE0plus+LikdAE0minus-LikdAE0plusminus-LikdAE0minusplus)/4*dE0*dA
# introduce Hessian Matrix
Hessian= [[LikddA,LikddAE0],[LikddAE0,LikddE0]]    
# inverse matrix of Hessian
Cov=np.linalg.inv(Hessian)                         
ErrbarA= np.sqrt(Cov[0,0])
ErrbarE0= np.sqrt(Cov[1,1])
print('Error-bar on A is:',ErrbarA)
print('Error-bar on E0 is:',ErrbarE0)


# In[5]:


#Problem3: Goodness of Fit
import numpy as np
import matplotlib.pyplot as plt
# Borrow the given data set for N,Eand SN
Data= np.loadtxt('/Users/bhand/downloads/DataAnalysis.txt')
E=Data[:,0]
N=Data[:,1]
SN=Data[:,2]

E0=np.linspace(0,20,100)
A=np.linspace(0,1,100)
chi2= np.zeros((100,100))    # 100*100 array for given set of E0 and A
bestchi2=np.zeros(1000)      # stores best fit chi2 for all different sets
for k in range(1000):
    for i in range(100):
        for j in range(100):
            Nth= 1 + A[j]* np.exp(-(E-E0[i])**2)+ np.random.normal(0,SN)
            chi2[i][j]=np.sum((Nth-N)**2/SN**2)

    chi2min=np.min(chi2)
    imin, jmin = np.where(chi2==np.min(chi2))  # best fit A and E0 for minimum chi2
    E0min=E0[imin[0]]
    Amin=A[jmin[0]]
    
    bestchi2[k]=chi2min
# Separate all chi2 value greater than that for actual data set
chi2abovechimin=[i for i in bestchi2 if i >= 20.0965]
# Determine goodness of fit
goodness=len(chi2abovechimin)/len(bestchi2)
print('goodness of fit is:',goodness)

#Plot
plt.plot(bestchi2);
plt.xlabel('Number of trials')
plt.ylabel('chi2')
plt.title('best fit chi2 for different artificial data set')
plt.figure(2)
plt.hist(bestchi2)
plt.plot([20.0965, 20.0965], [0, 300], 'r-', lw=2)
plt.xlabel(' Chi2')
plt.ylabel('Frequency')
plt.title('Histogram');

print('Even goodness of fit is low, we consider this theory as good description of data.')


# In[6]:


#Problem4: Model Selection
import numpy as np
import matplotlib.pyplot as plt
# Borrow the given data set for N,Eand SN
Data= np.loadtxt('/Users/bhand/downloads/DataAnalysis.txt')
E=Data[:,0]
N=Data[:,1]
SN=Data[:,2]

E0=np.linspace(0,20,100)
A=np.linspace(0,1,100)
chi2= np.zeros((100,100))    # 100*100 array for given set of E0 and A

Afakedata=np.zeros(1000)     # store possible best fit value for A
Ntrue=np.ones(np.size(N))    # consider Ntrue is 1 
for k in range(1000):
    noise=np.random.normal(0,SN)   #  introduce noise 
    Nmeasured= Ntrue + noise       #  add noise to Ntrue
    #Repeat the measurement on fake data
    for i in range(100):
        for j in range(100):
            Nth= 1 + A[j]* np.exp(-(E-E0[i])**2)
            chi2[i][j]=np.sum((Nth-Nmeasured)**2/SN**2)
            
    chi2min=np.min(chi2)
    imin, jmin = np.where(chi2==np.min(chi2))  # best fit A and E0 for minimum chi2
    E0min=E0[imin[0]]
    Amin=A[jmin[0]]
    Afakedata[k]=Amin
    
#plot    
plt.figure(3)
plt.plot(Afakedata,'.')
plt.xlabel('number of trials')
plt.ylabel('A')
plt.title('Best fit A for different artificial data set')
plt.figure(4) 
# Histogram of the data
plt.hist(Afakedata)
plt.plot([0.3132, 0.3132], [0, 300], 'r-', lw=2)
plt.xlabel(' A')
plt.ylabel('Frequency')
plt.title('Histogram');        

print('Since Amin due to accidental allignment Noise are almost smaller than that calculated for real data set(red line),')     
print('we can reject the theory which claims that there should be no peaks in photon distribution.')


# In[ ]:




