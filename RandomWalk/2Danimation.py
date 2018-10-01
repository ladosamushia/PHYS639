from tkinter import *
import time
import numpy as np
import numpy.random as random

stop_moving = False
r = 10
restart = False

def rup():
    global r 
    r += 1
    return

def rdown():
    global r 
    r -= 1
    return

def stop():
    global stop_moving
    stop_moving = True
    return

def restart():
    global restart
    restart = True
    return
    
    
gui = Tk()
gui.geometry("800x800")
c = Canvas(gui ,width=800 ,height=800)
c.pack()
oval = c.create_oval(390,390,410,410,fill='pink')
center = c.create_oval(399,399,401,401,fill='black')
def reset():
    c.coords(oval,390,390,410,410)
    
brup = Button(c,text='increase step size',command = rup,anchor=W)
brup_window = c.create_window(20, 10, anchor=NW, window=brup)

brdown = Button(c,text='decrease step size',command = rdown)
brdown_window = c.create_window(20, 10, anchor=NW, window=brdown)

bpause = Button(c,text='pause',command = stop)
bpause_window = c.create_window(20, 10, anchor=NW, window=bpause)

brestart = Button(c,text='restart',command = restart)
brestart_window = c.create_window(20, 10, anchor=NW, window=brestart)

breset = Button(c,text='reset',command = reset)
breset_window = c.create_window(20, 10, anchor=NW, window=breset)

bquit = Button(c,text='quit',command = gui.destroy)
bquit_window = c.create_window(20, 10, anchor=NW, window=bquit)

brup.place(x=0,y=0)
brdown.place(x=0,y=30)
bpause.place(x=0,y=60)
brestart.place(x=0,y=90)
breset.place(x=0,y=120)
bquit.place(x=0,y=150)

rlevel = Label(gui,text="{}".format(r))
rlevel.place(x=150,y=0)

while True:
  phi = random.rand()*2*np.pi
  dx = r*np.cos(phi)
  dy = r*np.sin(phi)
  c.move(oval,dx,dy)
  rlevel.configure(text="{}".format(r))
  gui.update()
  while stop_moving:        
        time.sleep(.5)
        gui.update()
        if restart == True:
            restart = False
            stop_moving = False
            break

  time.sleep(.1)

gui.title("Random Walk")

gui.mainloop()
