import numpy as np
import matplotlib.pyplot as plt

# Problem 1
Data = np.loadtxt("DataAnalysis.txt")
E = Data[:,0]
N = Data[:,1]
SN = Data[:,2]
step = 100
E0 =  np.linspace(0,20,step)
jhat = np.zeros((step,step))
for i in range (step):
    A = np.linspace(0, 1, 100)
    for j in range (step): 
        Nth = 1 + A[j]*np.exp(-(E-E0[i])**2)
        jhat[i][j] = np.sum((Nth-N)**2/SN**2)       
imin, jmin = np.where(jhat == np.min(jhat))
Emin = E0[imin[0]]
Amin = A[jmin[0]]

g = amin
m = Emin
bestfit = np.min(jhat)




#Problem 2 (assistance provided from Cheyne Weis and Parker Stoops
def Hmat(jhat,A,E0,jmin,imin):
    #Partial 2nd derivatives
    dada=(jhat[imin,jmin+1]+jhat[imin,jmin-1]-2*jhat[imin,jmin])/((A[jmin+1]-A[jmin])**2)
    dede=(jhat[imin+1,jmin]+jhat[imin-1,jmin]-2*jhat[imin,jmin])/((E0[imin+1]-E0[imin])**2)
    dade=(jhat[imin-1,jmin-1]+jhat[imin+1,jmin+1]-jhat[imin-1,jmin+1]-jhat[imin+1,jmin-1])/(4*(A[jmin+1]-A[jmin])*(E0[imin+1]-E0[imin]))
    # Matrices
    Hess=np.zeros((2,2))
    Hess[0][0]=.5*dada
    Hess[0][1]=.5*dade
    Hess[1][0]=.5*dade
    Hess[1][1]=.5*dede
    return Hess
# Hessian Matrix
Hess= Hmat(jhat,A,E0,jmin,imin)
C=np.linalg.inv(Hess)
sigma=np.sqrt(np.diagonal(C))
print "Rounded Values"
print( 'E0 = ', np.round(Emin, 2), "+/-", np.round(sigma[0], 2))
print( 'A =', np.round(Amin, 1), "+/-" , np.round(sigma[0], 1))
print "Raw Values"
print('A is', Amin,'E0 is',Emin)
print('sigmaE0 is', sigma[0],'sigmaA is',sigma[1])
Esmooth = np.linspace(0,20,10000)
plt.figure(1)
#Scatter plot
plt.plot(Esmooth,1 + Amin*np.exp(-(Esmooth-Emin)**2), "black")
plt.title("Data and Best fit Model")
plt.xlabel("Energy")
plt.ylabel("N value")
plt.figure(2)
# Error Bars 
plt.errorbar(Esmooth,1 + Amin*np.exp(-(Esmooth-Emin)**2), sigma[0], sigma[1], "yellow")
plt.plot(Esmooth,1 + Amin*np.exp(-(Esmooth-Emin)**2), "black")
plt.title("Data and Best fit Model with Uncertantity Band")
plt.xlabel("Energy")
plt.ylabel("N value")