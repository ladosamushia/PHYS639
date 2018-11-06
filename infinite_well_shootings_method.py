import matplotlib.pyplot as plt 
import numpy as np
#Shooting method idea and runge kutta implemented
#this method solves an IVP and make sure that the Boundary values are satified, check wiki
tini=0
tfin=1
Nsteps=1000
psi0=0
psip0=1
e={"e1":1,"e2":10,"e3":30,"e4":65,"e5":100}# guess work

psid={}
h=abs(tini-tfin)/Nsteps
t=np.linspace(tini,tfin,Nsteps+1)
d=.1
sig=1
def sign(j):
    si=sig*j
    if si>0:
        si=1
    elif si<0:
        si=-1 
    return si  
def f(x1,x2,a):
    y1=-(2*a)*x1
    y2=x2
    return y1,y2
for key in e.keys():
    a1=e[key]
    print("e:",a1)
    psip=np.zeros(Nsteps+1)
    psi=np.zeros(Nsteps+1)
    psi[0]=psi0
    psip[0]=psip0
    while abs(psi[Nsteps-1])>=0.005 or psi[Nsteps-1]==0 :
        for i in range(1,Nsteps):
        #calculating psip(t)    
        #calculating psi(t)   
            k1=h*f(psi[i-1],0,a1)[0]
            l1=h*f(0,psip[i-1],a1)[1]
            k2=h*f(psi[i-1]+l1/2,0,a1)[0]
            l2=h*f(0,psip[i-1]+k1/2,a1)[1]
            k3=h*f(psi[i-1]+l2/2,0,a1)[0]
            l3=h*f(0,psip[i-1]+k2/2,a1)[1]
            k4=h*f(psi[i-1]+l3,0,a1)[0]
            l4=h*f(0,psip[i-1]+k3,a1)[1]
            psi[i]=psi[i-1]+1/6*(l1+2*l2+2*l3+l4)
            psip[i]=psip[i-1]+1/6*(k1+2*k2+2*k3+k4)
        a1=a1+d
        #trying to minimize the steps
        if sign(psi[Nsteps-1])*psi[Nsteps-1]>=2 or sign(psi[Nsteps-1])*psi[Nsteps-1]>=1:
            d=1
        elif  sign(psi[Nsteps-1])*psi[Nsteps-1]>=.5 or sign(psi[Nsteps-1])*psi[Nsteps-1]>=.2:
            d=.5 
        elif  sign(psi[Nsteps-1])*psi[Nsteps-1]>=.05 or sign(psi[Nsteps-1])*psi[Nsteps-1]>=.02:     
            d=.1 
        elif  sign(psi[Nsteps-1])*psi[Nsteps-1]>=.01 or sign(psi[Nsteps-1])*psi[Nsteps-1]>=.0055: 
            d=.01
    psid[key]=psi 
    print(a1)   
psik=list(psid.keys())
#print(len(psid[psik[3]]))
print(len(psid[psik[0]]))
print(len(psid[psik[1]]))
plt.figure(1)
plt.plot(t,psid[psik[0]])
plt.plot(t,psid[psik[1]])
plt.plot(t,psid[psik[2]])
plt.plot(t,psid[psik[3]])
plt.plot(t,psid[psik[4]])
plt.axvline(x=0)
plt.axhline(y=0)
#plt.legend(loc="upper right")
plt.xlabel('t')
plt.ylabel(r'$\psi$(t)') 
plt.show()
