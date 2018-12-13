# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 17:10:37 2018

@author: mikelobe
"""

import numpy as np
import matplotlib.pyplot as plt

#Kinetic Energy of Nuclear Reactions

MeV= 1.6e-13 #joules to electron volts conversion
AMU=1.66e-27 #mass of atomic mass unit in kg
Ma= 6.015*AMU #known standard atomic weight of reactant A
Mb= 2.014*AMU #known standard atomic weight of reactant B
Mc= 4.0026*AMU #known standard atomic weight of reactant C
Md= 4.0026*AMU #known standard atomic weight of reactant D
E= 0 #initial energy before reaction
dM=0
c= 2.9979e8 #speed of light
def Energy(dM):
    Mr=Ma+Mb #Mass of Reactants
    Mp=Mc+Md #Mass of Products
    dM=Mr-Mp #Change in Mass over reaction
    return (dM*c**2)/MeV #E=mc**2 energy relation
print Energy(dM) #Kinetic Energy Released in MeV

#You need to know the masses of the reactants as well as the identities and
#masses of the products. It is easiest to do this with a data set that is imported.
#A positive energy shows that the reaction is exothermic releasing energy
#while a negative energy shows that the reaction is endothermic requiring energy
#for it to be carried out.