from Tkinter import *
from math import *
from sys import argv
from matplotlib import pyplot as plt
import time
import numpy.random as random
import numpy
pi = 3.14159265359
global gui
# initiliaze tk object

def g():
	#constants
	q = random.rayleigh(10)
	return q
def brownian(canvas):
	#initial conditions
	#time
	t = 0
	dt = 0.01
	tf = 100
	#array of xy coordinates
	xa = numpy.full(100, 400)
	ya = numpy.full(100, 400)
	#circle characteristics
	rad = 3
	fill = "#f80c12"
	i = 0
	#list of circle objects
	clist = []
	#boundary
	h= 700
	l = 50
	canvas.create_rectangle(l,l,h,h, width=1)
	xlist = []
	#create all circle at initial position
	while(i <= 99):
		circle = canvas.create_oval(xa[i]-rad, ya[i]-rad, xa[i]+rad, ya[i]+rad, width=1, fill=fill)
	  	canvas.after(1)
		gui.update()
		clist.append(circle)
		i+=1
	while(t < tf):

		i = 0
		#move each particle
		while(i<=99):
			#generate random radius and angle to displace
			r = g()
			a = 2*pi*random.random()
			xlist.append(a)
			#print a
			#update xy coordinates
			xa[i] += r*cos(a)
			ya[i] += r*sin(a)
			#keep particle inside box
			if(xa[i] > h):
				xa[i] = h - 5
			if(xa[i] < l):
				xa[i] = l + 5
			if(ya[i] > h):
				ya[i] = h - 5
			if(ya[i] < l):
				ya[i] = l + 5 

			#update circle position
			canvas.delete(clist[i])
			clist[i] = canvas.create_oval(xa[i]-rad, ya[i]-rad, xa[i]+rad, ya[i]+rad, width=1, fill=fill)
	  		canvas.after(1)
			gui.update()
			i+=1
		if(t > 10):
		  	plt.hist(xlist,bins = 100)
		  	plt.show()
		t += dt
	#plot
gui = Tk()
#root.mainloop()

width, height = 800, 800
x_center, y_center = 0.5*width, 0.5*height
x_scale, y_scale = 70, 70

# create a canvas
canvas = Canvas(gui, width=width, height=height, bg='white')
canvas.pack(expand=YES, fill=BOTH)

canvas.create_text(115, 25, font=("Purisa", 12), text="Diffusion")

# begin recursive drawing
brownian(canvas)

q = raw_input()

gui.mainloop()
#print q
# not sure