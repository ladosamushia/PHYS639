
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
print(Amin)
print(E0min)
print(ki2min)
print(imin)
print(jmin)
#############################################################
#Part 2     L=(np.exp(-1*(ki2)**2))/2
def Hmat(ki2,A,E0,jmin,imin):
    dada=(ki2[imin,jmin+1]+ki2[imin,jmin-1]-2*ki2[imin,jmin])/(A[jmin+1]-A[jmin])
    dede=(ki2[imin+1,jmin]+ki2[imin-1,jmin]-2*ki2[imin,jmin])/(E0[imin+1]-E0[imin])
    dade=(ki2[imin-1,jmin-1]+ki2[imin+1,jmin+1]-ki2[imin-1,jmin+1]-ki2[imin+1,jmin-1])/(4*(A[jmin+1]-A[jmin])*(E0[imin+1]-E0[imin]))
    Hess=np.zeros((2,2))
    Hess[0][0]=.5*dada
    Hess[0][1]=.5*dade
    Hess[1][0]=.5*dade
    Hess[1][1]=.5*dede
    return Hess

#def Hess(Z,Y,X,j,i):
#    dxx=Z[i-1][j]+Z[i+1][j]-2*Z[i][j]/(X[i+1]-X[i])
#    dyy=Z[i][j-1]+Z[i][j+1]-2*Z[i][j]/(Y[j+1]-Y[j])
#    dxy=(Z[i+1][j+1]+Z[i-1][j-1]-Z[i+1][j-1]-Z[i-1][j-1])/4*(X[i]-X[i+1])*(Y[j]-Y[j+1]) 
#    H=np.zeros((2,2))
#    H[0][0]=-.5*dxx
#    H[1][1]=-.5*dyy
#    H[0][1]=-.5*dxy
#    H[1][0]=-.5*dxy
#    return H


Hess= Hmat(ki2,A,E0,jmin,imin)
np.linalg.inv(Hess)
print(Hess)
