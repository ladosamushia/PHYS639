from Tkinter import *
from math import *
from sys import argv
from matplotlib import pyplot as plt
import time
import numpy.random as random
pi = 3.14159265359
global gui
# initiliaze tk object


r=1
nlist = []
rlist = []
for j in range(0,4000):
	x = 0
	y = 0
	z = 0
#	print j
	for i in range(0,j):
		thet = 2*pi*random.random()
		phi = acos(2*random.random() - 1)
		xv = r*sin(phi)*cos(thet)
		yv = r*sin(phi)*sin(thet)
		zv = r*cos(phi)
		x += xv
		y += yv
		z += zv
	nlist.append(j)
	rlist.append(sqrt((x*x) + (y*y) + (z*z)))

plt.plot(nlist,rlist)
plt.xlabel('Steps')
plt.ylabel('Distance from Origin (units)')
plt.show()
