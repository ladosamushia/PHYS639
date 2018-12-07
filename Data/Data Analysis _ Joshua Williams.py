#data analysis
#Best-fit values
import numpy as np
import matplotlib.pyplot as plt


n=100
data = np.loadtxt('DataAnalysis.txt')

E= data[:,0]
N = data[:,1]
delta=data[:,2]

plt.figure(1)
plt.errorbar(E,N,delta,fmt='o')
plt.xlabel('Energy')
plt.ylabel('Number of Photons')
chi2 = np.zeros((n,n))

E0 = np.linspace(0,20,n)
A = np.linspace(0,1,n)
for i in range(n):
    for j in range(n):
        Nth = 1 + A[j]*np.exp(-(E-E0[i])**2)
chi2[i][j] = np.sum(((N-Nth)**2)/(delta**2))

print('Minimum chi2 = ', np.min(chi2))

chi2min = np.min(chi2)
chi2max = np.exp(-chi2min/2)
imin, jmin = np.where(chi2 == np.min(chi2))
E0min = E0[imin[0]]
Amin = A[jmin[0]]

print('Minimum E= ', E0min, 'A = ', Amin)
plt.figure(2)
plt.imshow(chi2)

plt.figure(1)
plt.plot(E,1+Amin*np.exp(-(E-E0min)**2))

dada=(chi2[imin, jmin + 1] + chi2[imin, jmin - 1] - 2 * chi2[imin, jmin]) / (A[jmin + 1] - A[jmin])
dede=(chi2[imin + 1, jmin] + chi2[imin - 1, jmin] - 2 * chi2[imin, jmin]) / (E0[imin + 1] - E0[imin])
dade=(chi2[imin - 1, jmin - 1] + chi2[imin + 1, jmin + 1] - chi2[imin - 1, jmin + 1] - chi2[imin + 1, jmin - 1]) \
/ (4 * (A[jmin + 1] - A[jmin]) * (E0[imin + 1] - E0[imin]))

Hess=np.zeros((2,2))
Hess[0][0], Hess[0][1], Hess[1][0], Hess[1][1] = dada / 2, dade / 2, dade / 2, dede / 2

C = np.linalg.inv(Hess)
sigmas = np.sqrt(C.diagonal())

print('\nError:', sigmas)

#seems to print the distribution/error well, took a little fiddling.