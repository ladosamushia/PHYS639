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
N = 1000
M = 1000
tot = 0
for j in range ( M ):
    pos = 0
    for i in range ( N ):
        step = random.choice( randomnumbers1 ) #number generator
        pos += step
    tot += pos
    averagedisplacement1.append( ( tot/M ) )
    J.append( j )
    displacement1.append( tot/M )
    meandisplacement1.append( np.mean( displacement1 ) )
plt.figure( 1 )
plt.plot( J , averagedisplacement1 )
plt.plot(J , meandisplacement1 )
#%%
