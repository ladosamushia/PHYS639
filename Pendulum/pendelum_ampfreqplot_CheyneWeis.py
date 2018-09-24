from Tkinter import *
from math import *
from sys import argv
from matplotlib import pyplot as plt
import time
pi = 3.14159265359
global gui
# initiliaze tk object


def f(a, w, t, i):
	#constrants
	g = 9.8
	l = 0.08
	b = 0.2
	F=1
	#acceleration from gravity, damping, and forcing
	return -(g/l)*sin(a) - b*w +F*sin(i*t)
# def drawLine(canvas, x1, y1, x2, y2):
# 	# globalize variables
# 	global q
# 	# color according to compression
# 	fill = "#ffffff"
# 	canvas.create_line(x1, y1, x2, y2, width=0.5)
# def drawCircle(canvas, x, y, rad, phase=0):
# 	# color circle according to phase
# 	fill = "#ee1100"

# 	# draw a circle of given radius
# 	canvas.create_oval(x-rad, y-rad, x+rad, y+rad, width=3, fill=fill)
# def drawcanvas(canvas, a):
# 	# clear canvas
# 	canvas.delete("all")
# 	canvas.create_text(115, 25, font=("Purisa", 12), text="Cool Pendelum")
# 	x1 = 450
# 	y1 = 300
# 	l = 300
# 	lx = l*sin(a)
# 	ly = l*cos(a)
# 	x2 = x1 + lx
# 	y2 = y1 + ly

# 	drawLine(canvas, x1, y1, x2, y2)
# 	drawCircle(canvas, x2, y2, l/25)
#   	canvas.after(1)
# 	gui.update()
# 	#q = raw_input()
	
def pendelumGO():
	#initial conditions
	w0 = 0
	a0 = 0
	ts = 0.01
	amp = []
	freq = []
	#drawcanvas(canvas, a)
	#loop through frequencies
	i = 0
	while(i <= 20):
		t = ts
		#reset all variables each time
		maxa = 0
		tot = 0
		n = 0
		a = a0
		w = w0
		d = 0
		tf = 20
		alist = [a0]
		tlist = [t]
		while (t < tf):
			#eulers method
			d = f(a, w, t, i)
			w += (d*ts)
			a += (w*ts)
			alist.append(a)
			#print a
			t += ts
			tlist.append(t)
			#keep maximum angle
			if(abs(a) > maxa):
				maxa = abs(a)
		#keep values for plot
		amp.append(maxa)
		freq.append(i)
		i += 0.01
	#plot
	plt.plot(freq,amp)
	plt.xlabel('Driving Frequency (rad/sec)')
	plt.ylabel('Amplitude')
	plt.show()

			#drawcanvas(canvas, a)
		#plt.plot(tlist,alist)
		#plt.xlabel('Time (s)')
		#plt.ylabel('Angle (s)')
		#plt.show()
# gui = Tk()
# #root.mainloop()

# width, height = 900, 900
# x_center, y_center = 0.5*width, 0.5*height
# x_scale, y_scale = 70, 70

# create a canvas
#canvas = Canvas(gui, width=width, height=height, bg='white')
#canvas.pack(expand=YES, fill=BOTH)

# begin recursive drawing
pendelumGO()




# q = raw_input()

# gui.mainloop()
#print q
# not sure