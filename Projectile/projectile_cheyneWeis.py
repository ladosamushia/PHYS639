from math import *
from matplotlib import pyplot as plt
#pi, gravity, mass
pi, g, m = 3.14159265359, 9.8, 1
def f(t, vx, vy, x, y):
	##calculate x and y acceleration including air reistance, 1-4
	h = (1- (2.2e-5*y))**(5/2)
	thet = atan2(vy,vx)
	a = -m*sin(thet)*0.00004*((vx*vx)+(vy*vy))*h
	b = -6.674e-11*5.97219e24*m/(6.3781e6 + y)**2 - m*cos(thet)*0.00004*((vx*vx)+(vy*vy))*h
	#return tuple
	return a,b 
#initial velocity and angle
v0, thet = 10, pi/4
#initialize position and velocities
vx, vy, ts, t, x, y = v0*cos(thet), v0*sin(thet), 0.00001, 0, 0, 0
xlist = [vx]
ylist = [vy]
#lists for graph
while (y >= 0):
	#euler method
	ax, ay = f(t, vx, vy, x, y)
	vx += (ax*ts)
	vy += (ay*ts)
	x += (vx*ts)
	y += (vy*ts)
	xlist.append(x)
	print x
	ylist.append(y)
#plot it
plt.plot(xlist,ylist)
plt.show()