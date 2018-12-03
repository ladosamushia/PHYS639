import numpy as np 
import matplotlib.pyplot as plt
data=np.loadtxt('J:/Users/Tomthin/DataAnalysis.txt')
E_in=data[:,0]
N_in=data[:,1]
er_in=data[:,2]

A_m=np.linspace(0,1,100)
E_m=np.linspace(0,10,100)
def model(Am,Em):
    Nth=1+Am*np.exp(-(E_in-Em)**2)
    return(Nth)
i=0
j=0
chi2=np.zeros((100,100))
chi2min=100000
np.meshgrid(A_m,E_m)
for Ai in A_m:
    j=0
    for Ej in E_m:
        chi2[j][i]=np.sum((model(Ai,Ej)-N_in)**2/er_in**2)
        
        if chi2[j][i]<=chi2min:
            posx=j
            posy=i
            chi2min=chi2[j][i]
            #print(E_m[posx],Ej)
            #print(chi2min)
        j=j+1
    i=i+1 
Amin=A_m[posy] 
Emin=E_m[posx]
print(r'$\chi^2$:',chi2min)
plt.figure(0)
plt.errorbar(E_in,N_in,er_in,fmt=".")
plt.plot(E_in,model(Amin,Emin))
plt.show()
plt.figure(1)
plt.imshow(chi2,cmap="jet")
plt.xlabel("A*")
plt.ylabel("E0*")
plt.title(r'$\chi^2$')
plt.colorbar()
plt.show()
################################################################################
def Hess(X,Y,Z,i,j):
    dxx=Z[i-1][j]+Z[i+1][j]-2*Z[i][j]/(X[i+1]-X[i])
    dyy=Z[i][j-1]+Z[i][j-1]-2*Z[i][j]/(Y[j+1]-Y[j])
    dxy=(Z[i+1][j+1]+Z[i-1][j-1]-Z[i+1][j-1]-Z[i-1][j-1])/4*(X[i]-X[i+1])*(Y[j]-Y[j+1]) 
    H=np.zeros((2,2))
    H[0][0]=-.5*dxx
    H[1][1]=-.5*dyy
    H[0][1]=-.5*dxy
    H[1][0]=-.5*dxy
    return H
H=Hess(E_m,A_m,chi2,posx,posy)
C=np.linalg.inv(H)
sigmas=np.sqrt(C.diagonal())
print('error:',sigmas)
#################################################################################
import pandas as pd
Af=np.array([])
g1=0
g2=0
for l in range(100):
    signal=np.ones(E_in.size)
    noise=np.random.normal(np.zeros(E_in.size),er_in)
    makeup=signal+noise
    #print(makeup)
    i=0
    j=0
    chi2fake=np.zeros((100,100))
    chi2minfake=100000
    for Ai in A_m:
        j=0
        for Ej in E_m:
            chi2fake[j][i]=np.sum((model(Ai,Ej)-makeup)**2/noise**2)
            if chi2fake[j][i]<=chi2minfake:
                posxf=j
                posyf=i
                chi2minfake=chi2fake[j][i]
                #print(E_m[posx],Ej)
                #print(chi2min)
            j=j+1
        i=i+1
    Af=np.append(Af,A_m[posyf]) 
    if A_m[posyf]>=Amin:
        g1=g1+1
    else:
        g2=g2+1
print('this is how often A* in the artificial data gets to be more or equal to Amin for the best fit model:',g1/(g2+g1))        
df=pd.DataFrame(data=Af)  
fig, ax = plt.subplots()
df.plot.kde(ax=ax, legend=False)
df.plot.hist(density=False, ax=ax,legend=False)
ax.set_ylabel('Distribution')
ax.set_xlabel('A*')
plt.axvline(x=Amin)
#plt.legend(loc="upper right")
plt.show()
################################################################################
chi2fake1f=np.array([])
g1=0
g2=0
for l in range(1000):
    signal1=model(Amin,Emin)
    noise1=np.random.normal(np.zeros(E_in.size),er_in)
    makeup1=signal1+noise1
    #print(makeup)
    i=0
    j=0
    chi2fake1=np.zeros((100,100))
    chi2minfake1=100000
    for Ai in A_m:
        j=0
        for Ej in E_m:

            makeup1=signal1+noise1
            chi2fake1[j][i]=np.sum((model(Ai,Ej)-makeup1)**2/noise1**2)
            if chi2fake1[j][i]<=chi2minfake:
                posxf1=j
                posyf1=i
                chi2minfake1=chi2fake1[j][i]
                #print(E_m[posx],Ej)
                #print(chi2min)
            j=j+1
        i=i+1
    chi2fake1f=np.append(chi2fake1f,chi2minfake1)    
    if chi2minfake1<=chi2min:
        g1=g1+1
    else:
        g2=g2+1
goodness=g1/(g2+g1)
print('goodness:',goodness) 
df=pd.DataFrame(data=chi2fake1f)  
fig, ax = plt.subplots()
df.plot.kde(ax=ax, legend=False)
df.plot.hist(density=True, ax=ax,legend=False)
ax.set_ylabel('Distribution')
ax.set_xlabel(r'$\chi^2$')
plt.axvline(x=chi2min)
#plt.legend(loc="upper right")
plt.show()