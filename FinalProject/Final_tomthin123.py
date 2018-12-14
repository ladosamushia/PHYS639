import numpy as np
import numpy.random as random  
import matplotlib.pyplot as plt
dice=np.array([1,2,3,4,5,6])
ddice=np.add.outer(dice,dice).flatten()
coin=np.array(['h','t'])
Na=np.unique(ddice)
Np=np.zeros(Na.size)
Nexp=10000
M=0

for i in range(Nexp):
    N=random.choice(ddice)
    #print('dice',p1)
    M=0
    for j in range(N):
        c=random.choice(coin)
        if c=='h':
            M=M+1
    #print("M that is the number of Heads count in each experiment as described:",M)        
    if M==7 :
        Np[N-2]=Np[N-2]+1
for i in range(Np.size):
    print("Probabilty such that M=7 and N ",Na[i],"after doing",Nexp,"experiments is:",Np[i]/Nexp)
print("Since N=1 and N>12 doesn't even include in the sample(check ddice array), hence probabilty is always 0 for them")
