from Tkinter import *
from math import *
from sys import argv
from matplotlib import pyplot as plt
import time
pi = 3.14159265359
global gui
# initiliaze tk object


def f(a, w, t):
	#constants
	g = 9.8
	l = 0.1
	b = 0.2
	F=1
	b = 0.2
	#acceleration from gravity, damping, and forcing
	return -(g/l)*sin(a) - b*w +F*sin(sqrt(g/l)*t)
def drawLine(canvas, x1, y1, x2, y2):
	# globalize variables
	global q
	# color according to compression
	fill = "#ffffff"
	canvas.create_line(x1, y1, x2, y2, width=0.5)
def drawCircle(canvas, x, y, rad, phase=0):
	# color circle
	fill = "#ee1100"

	# draw a circle of given radius
	canvas.create_oval(x-rad, y-rad, x+rad, y+rad, width=3, fill=fill)
def drawcanvas(canvas, a):
	# clear canvas
	canvas.delete("all")
	canvas.create_text(115, 25, font=("Purisa", 12), text="Cool Pendelum")
	#find components of string length given angle
	x1 = 450
	y1 = 300
	l = 300
	lx = l*sin(a)
	ly = l*cos(a)
	x2 = x1 + lx
	y2 = y1 + ly
	#draw pendelum
	drawLine(canvas, x1, y1, x2, y2)
	drawCircle(canvas, x2, y2, l/25)
  	canvas.after(1)
	gui.update()
	#q = raw_input()
	
def pendelumGO(canvas):
	#initial conditions
	w0 = -1
	a0 = pi/4
	ts = 0.001
	t = ts
	a = a0
	w = w0
	d = 0
	tf = 20
	#lists for plot
	alist = [a0]
	tlist = [t]
	drawcanvas(canvas, a)
	while (t < tf):
		#eulers method
		d = f(a, w, t)
		w += (d*ts)
		a += (w*ts)
		#keep values for plot
		alist.append(a)
		#print a
		t += ts
		tlist.append(t)
		drawcanvas(canvas, a)
	#plot
	plt.plot(tlist,alist)
	plt.xlabel('Time (s)')
	plt.ylabel('Angle (s)')
	plt.show()
gui = Tk()
#root.mainloop()

width, height = 900, 900
x_center, y_center = 0.5*width, 0.5*height
x_scale, y_scale = 70, 70

# create a canvas
canvas = Canvas(gui, width=width, height=height, bg='white')
canvas.pack(expand=YES, fill=BOTH)

# begin recursive drawing
pendelumGO(canvas)




q = raw_input()

gui.mainloop()
#print q
# not sure