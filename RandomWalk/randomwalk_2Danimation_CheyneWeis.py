from Tkinter import *
from math import *
from sys import argv
from matplotlib import pyplot as plt
import time
import numpy.random as random
pi = 3.14159265359
global gui
# initiliaze tk object

def f():
	#constants
	m = 20
	s = 5
	#acceleration from gravity, damping, and forcing
	q = random.normal(m,s)
	while (q < 0):
		q = random.normal(m,s)
	print q
	return q
def g():
	#constants
	q = random.rayleigh(12.5)
	return q
def drawLine(canvas, x1, y1, x2, y2):
	# globalize variables
	global q
	# color according to compression
	fill = "#ffffff"
	canvas.create_line(x1, y1, x2, y2, width=1)
def drawcanvas(canvas, x1, y1, r, a, t):
	#find components of string length given angle
	w = 800
	OS = False
	x2 = x1 + r*cos(a)
	y2 = y1 + r*sin(a)

	drawLine(canvas, x1, y1, x2, y2)
 	canvas.after(25)
	gui.update()
	if(x2 > w):
		x2 -= w
		x1 -= w
		OS = True
	if(x2 < 0):
		x2 += w
		x1 += w
		OS = True
	if(y2 > w):
		y2 -= w
		y1 -= w
		OS = True
	if(y2 < 0):
		y2 += w
		y1 += w
		OS = True
	if(OS == True):
		drawLine(canvas, x1, y1, x2, y2)
	  	canvas.after(1)
		gui.update()
	return x2, y2
	#q = raw_input()
	
def brownian(canvas):
	#initial conditions
	t = 0
	dt = 0.01
	tf = 100
	x1 = 400
	y1 = 400
	while (t < tf):
		#eulers method
		r = g()
		a = 2*pi*random.random()
		#print a

		x1, y1 = drawcanvas(canvas, x1, y1, r, a, t)
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

canvas.create_text(115, 25, font=("Purisa", 12), text="Cool Brownian Motion on Torus")

# begin recursive drawing
brownian(canvas)

q = raw_input()

gui.mainloop()
#print q
# not sure
