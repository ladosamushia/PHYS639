# -*- coding: utf-8 -*-
"""

Created on Tue Sep 25 2018 by Philip Lucas

"""
"""Part 1"""

import numpy.random as random
import numpy as np
import matplotlib.pyplot as plt

J = []
displacement1 = []
meandisplacement1  = []
averagedisplacement1 = []
randomnumbers1 = [ -1.0 , 1.0 ]
Nsteps = 1000
Ntrials = 1000
tot = 0
for j in range ( Ntrials ):
    pos = 0
    step = random.choice( randomnumbers1, 100) #number generator
    pos += step
    tot += pos
    averagedisplacement1.append( np.abs( tot/Ntrials) )
    J.append( j )
    displacement1.append( tot/Ntrials )
    meandisplacement1.append( np.mean( displacement1 ) )
plt.figure( 1 )
plt.plot( J , averagedisplacement1 )
plt.title(" 1-D  Non-Biased |Random Walk|")
plt.xlabel(" Trial Number ")
plt.ylabel(" Displacement ")
#%%
displacement2 = []
meandisplacement2  = []
averagedisplacement2 = []
randomnumbers2 = [ -1.0 , 1.0 , 1.0 , 1.0 ]
tot2 = 0
for h in range ( Ntrials ):
    pos2 = 0
    step = random.choice( randomnumbers2, 100) #number generator
    pos2 += step
    tot2 += pos2
    averagedisplacement2.append( np.abs( tot2/Ntrials) )
    displacement2.append( tot2/Ntrials )
    meandisplacement2.append( np.mean( displacement2 ) )
plt.figure( 2 )
plt.plot( J , averagedisplacement2 )
plt.title(" 1-D  Biased |Random Walk|")
plt.xlabel(" Trial Number ")
plt.ylabel(" Displacement ")
plt.figure( 3 )
plt.title( " 1-D  Biased and Non-Biased |Random Walk| Combined " )
plt.xlabel(" Trial Number ")
plt.ylabel(" Displacement ")
plt.plot( J , averagedisplacement1 )
plt.plot( J , averagedisplacement2 )
plt.figure(4)
plt.title(" 1-D Combined |Random Walk| Average Displacement Trend")
plt.xlabel(" Trial Number ")
plt.ylabel(" Displacement ")
plt.plot( J , meandisplacement1 )
plt.plot( J , meandisplacement2 )
#%%
""" Part 2 """
from mpl_toolkits.mplot3d import Axes3D
X = []
Y = []
Z = []
randomnumbers3D = [ 1 , 2 , 3 , 4 , 5 , 6 ]
pos3dX = 0
pos3dY = 0
pos3dZ = 0
for h in range ( Ntrials ):
    step3D = random.choice( randomnumbers3D) #number generator
    if step3D == 1:
        pos3dX = 1
        X.append(pos3dX)
    if step3D == 2: 
        step = -1
        pos3dX = step3D
        X.append(pos3dX)
    if step3D != 1 or step3D !=2: 
        pos3dX = 0
        X.append(pos3dX)
    if step3D == 3: 
        step3D = 1
        pos3dY = step3D
        Y.append(pos3dY)
    if step3D == 4: 
        step3D = -1
        pos3dY = step3D
        Y.append(pos3dY)
    if step3D != 3 or step3D !=4: 
        pos3dY = 0
        Y.append(pos3dY)
    if step3D == 5: 
        step3D = 1
        pos3dZ = step3D
        Z.append(pos3dZ)
    if step3D == 6: 
        step = -1
        pos3dZ = step3D
        Z.append(pos3dZ)
    if step3D != 5 or step3D !=6: 
        pos3dZ = 0
        Z.append(pos3dZ)
print X
plt.figure( 5 )
fig = plt.figure(5)
ax = fig.add_subplot(111, projection = '3d')
ax.plot(X, Y, Z)

""" This last part doesn't work, the list makes sense I think I'm just messing up 
the 3-D plotting"""
