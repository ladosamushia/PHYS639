from Tkinter import *
from math import *
from sys import argv
import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

yellow = "#FFD700"
blue = "#0000CD"
black = "#000000"
crimson = "#DC143C"
green = "#006400"
grey = "#696969"
#canvas scale and center
c = [600.0,400.0]
scale = 0.25
scale = 200.0
sunrad = 25.0
erad = 7.5
#planetary constants
sm = 200.0
pm = 1.0
mev = 1/((1/pm)+(1/sm))
G = 1
sol = 3e8
rs = 2*G*sm/(sol*sol)
raf = sol*10000
def dpdt(r, J):
    return (J/(mev*r*r))
def drdt(r, je):
    temp = (je[1]*je[1]/(pm*pm*sol*sol)) -((1-(rs/r))*((sol*sol)+(je[0]*je[0]/(mev*mev*r*r))))
    return -sqrt(abs(temp))/1000

def dtaudt(u):
    return 1.0/sqrt(1.0 - (2.0*G))
def polar(xy):
    rt = [0,0]
    rt[0] = sqrt((xy[0]*xy[0])+(xy[1]*xy[1]))
    rt[1] = atan2(xy[1], xy[0])
    return rt
def polarv(vxy, xy, rt):
    vrt = [0,0]
    #find ang
    vr = sqrt(vxy[0]*vxy[0] + vxy[1]*vxy[1])
    if(vr == 0):
        print("hi")
        vrt[1] = 0
        vrt[0] = 0
    else: 

        vrt[0] = ((xy[0]*vxy[0]) + (xy[1]*vxy[1]))/rt[0]
        vrt[1] = ((xy[0]*vxy[1]) - (vxy[0]*xy[1]))/rt[0]
    return vrt
def nforce(xy):
    r = sqrt(xy[0]*xy[0] + xy[1]*xy[1])
    a = -G*sm*xy[0]/(r**3), -G*sm*xy[1]/(r**3)
    return a
def rforce(xy, le):
    a = [0,0]
    r = sqrt(xy[0]*xy[0] + xy[1]*xy[1])
    a[0] = -(G*sm*xy[0]/(r**3)) - raf*(3*G*(sm + pm)*le[0]*le[0]*xy[0]/(sol*sol*mev*pm*(r**5)))
    a[1] = -(G*sm*xy[1]/(r**3)) - raf*(3*G*(sm + pm)*le[0]*le[0]*xy[1]/(sol*sol*mev*pm*(r**5)))
    return a
def rect(rt):
    xy = [0,0]
    xy[0] = rt[0]*cos(rt[1])
    xy[1] = rt[0]*sin(rt[1])
    return xy

def drawCircle(canvas, xy, rad, fill):
    # draw a circle of given radius
    return canvas.create_oval(xy[0]-rad, xy[1]-rad, xy[0]+rad, xy[1]+rad, width=1, fill=fill)

def drawLine(canvas, xyi, xyf, col):
    # draw a circle of given radius
    canvas.create_line(xyi[0], xyi[1], xyf[0], xyf[1] ,fill = col, width=1)
def moveObject(canvas, shape, xyi, xyf):
    canvas.move(shape, xyf[0]-xyi[0], xyf[1]-xyi[1])
def canvconv(xy):
    #convert to canvas coordinates
    xyc = [0,0]
    xyc[0] = c[0] + (scale*xy[0])
    xyc[1] = c[1] - (scale*xy[1])
    return xyc
def euler(pxy, vxy, dt, je, isR):
    au = [0,0]
    if(isR == True):
        au = rforce(pxy, je)
    if(isR == False):
        au = nforce(pxy)
    vxy[0] = vxy[0] + au[0]*dt
    vxy[1] = vxy[1] + au[1]*dt
    pxy[0] = pxy[0] + vxy[0]*dt
    pxy[1] = pxy[1] + vxy[1]*dt
    return pxy, vxy
def planet(canvas):
    #planet initial conditions
    xyc = [0,-1]
    xyr = [0,-1]
    vxyc = [15.0, 7.0]
    vxyr = [15.0, 7.0]
    t=0.0
    dt=0.005
    #draw sun
    sun = drawCircle(canvas, c, sunrad, yellow)
    pxyc = canvconv(xyc)
    pxyr = canvconv(xyr)
    #draw planets
    planetc = drawCircle(canvas, pxyc, erad, green)
    planetr = drawCircle(canvas, pxyr, erad, blue)
    canvas.after(1)
    gui.update()
    #keep prior position
    pxycl = pxyc
    pxyrl = pxyr
    #convert to relativistic to polar
    rtr = polar(xyr)
    vrtr = polarv(vxyr, xyr, rtr)
    print(pxyc, pxyr)
    #conserved quantities
    #print vrtr
    cons = [rtr[0]*rtr[0]*vrtr[1]*mev, pm*sol*sol*(1 - (rs/rtr[0]))]
    while(True):
        #euler's method
        xyc, vxyc = euler(xyc, vxyc, dt, cons, False)
        xyr, vxyr = euler(xyr, vxyr, dt, cons, True)
        t += dt
        #convert to canvas coordinates
        pxyc = canvconv(xyc)
        #pxyr = canvconv(rect(rtr))
        pxyr = canvconv(xyr)

        moveObject(canvas, planetc, pxycl, pxyc)
        moveObject(canvas, planetr, pxyrl, pxyr)
        #draw lines

        drawLine(canvas, pxyc, pxycl, black)
        drawLine(canvas, pxyr, pxyrl, grey)
        canvas.after(1)
        #update prior position
        pxycl = pxyc
        pxyrl = pxyr
        gui.update()

gui = Tk()
#root.mainloop()

width, height = 1200, 800
x_center, y_center = 0.5*width, 0.5*height
x_scale, y_scale = 70, 70

# create a canvas
canvas = Canvas(gui, width=width, height=height, bg='white')
canvas.pack(expand=YES, fill=BOTH)

canvas.create_text(115, 25, font=("Purisa", 12), text="Earth's Orbit")

# begin recursive drawing
planet(canvas)
gui.mainloop()