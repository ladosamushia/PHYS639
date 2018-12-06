
import numpy as np
import matplotlib.pyplot as plt

Data= np.loadtxt("data_2.txt")

Ein=Data[:,0]
Nin=Data[:,1]
Ndel=Data[:,2]



step=100
ki2=np.zeros((step,step))
E0=np.linspace(0,20,step)


for i in range(step):

    A=np.linspace(0,1,step)
    for j in range(step):
        N_th= 1 + A[j]*np.exp(-(Ein-E0[i])**2)
        ki2[i][j]=np.sum((N_th-Nin)**2/Ndel**2)
imin, jmin=np.where(ki2==np.min(ki2))

E0min=E0[imin[0]]
Amin=A[jmin[0]]
ki2min=np.min(ki2)
Nmin= 1 + Amin*np.exp(-(Ein-E0min)**2)

plt.errorbar(Ein, Nin, Ndel, fmt='o')
plt.xlabel('Energy')
plt.ylabel('Number of Photons')
plt.plot(Ein, Nmin)
plt.show()
print('Amin is', Amin)
print('E0min is', E0min)
print('ki2min is', ki2min)
print('imin is', imin)
print('jmin is', jmin)
#############################################################
#Part 2     L=(np.exp(-1*(ki2)**2))/2
def Hmat(ki2,A,E0,jmin,imin):
    dada=(ki2[imin,jmin+1]+ki2[imin,jmin-1]-2*ki2[imin,jmin])/((A[jmin+1]-A[jmin])**2)
    dede=(ki2[imin+1,jmin]+ki2[imin-1,jmin]-2*ki2[imin,jmin])/((E0[imin+1]-E0[imin])**2)
    dade=(ki2[imin-1,jmin-1]+ki2[imin+1,jmin+1]-ki2[imin-1,jmin+1]-ki2[imin+1,jmin-1])/(4*(A[jmin+1]-A[jmin])*(E0[imin+1]-E0[imin]))
    Hess=np.zeros((2,2))
    Hess[0][0]=.5*dada
    Hess[0][1]=.5*dade
    Hess[1][0]=.5*dade
    Hess[1][1]=.5*dede
    return Hess




Hess= Hmat(ki2,A,E0,jmin,imin)
C=np.linalg.inv(Hess)
sigma=np.sqrt(np.diagonal(C))
print('sigmaE0 is', sigma[0],'sigmaA is',sigma[1])
