# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:39:58 2018

This project is a rough gravity well simulation that simulates early planet formation in the
Solar System. These already formed planetoids are randomly placed in orbit around a star with random mass
and velocity. These planets then begin to orbit around the host star.

However, they have a chance to collide and form a larger planet, which will 
combine their momentum vectors and mass. To make sure that the simulation actually works
correctly, there will be two predetermined planets with set orbits and mass. 

TL:DR,
- Rough, 2D simulation of early solar system and planet formation
- Planets have a possibility of collision which will combine their mass and momentum vectors
- Two predetermined planets to ensure that at least some planets remain in orbit

@author: Jared
"""

# The source codes that I drew from all had pygame as an added library, so pygame will need to be installed.
import numpy as np
import matplotlib.pyplot as plt
import math
import pygame
import random as ran

# Simulation limitation. This is to ensure we don't have any off-screen planets.
w_window = 1000             # Width of the window
h_window = 800              # Height of the window

# Later in the program, it becomes a cluster having to write w_window/2 and vice versa. So just set new constants
w2 = w_window/2
h2 = h_window/2

# Constants and initial conditions
planets = 10                # Number of generated planets
density = .05               # To keep the system constant, all planets will have the same density. This isn't realistic but oh well.
G = 6.67e-11                # Universal Gravitational Constant

planetlist = []             # Array of planets.

" THe planets will all depend on the same laws of physics, so we can separate them and their properties into classes"


" This class represents the kinematics of the object, notably the position and velocity vectors"
class kinematics:
    def __init__(self, x, y, vx, vy):
        self.x              # Position in x-direction
        self.y              # Position in y-direction
        self.vx             # Velocity in x-direction
        self.vy             # Velocity in y-direction
    
    def __repr_(self):
        return 'x:{x}'.format(x=self.x)
        return 'y:{y}'.format(y=self.y)
        return 'vx:{vx}'.format(vx=self.vx)
        return 'vy:{vy}'.format(vy=self.vy)
    

" THis class will reperesnt the small changes in the kinematics of the object"
class derivatives:
    def __init__(self, dx, dy, dvx, dvy):
        self.dx             # derivative of x-vector
        self.dy             # derivative of y-vector
        self.dvx            # derivative of vx-vector
        self.dvy            # derivative of vy-vector
    
    def __repr__(self):
        return 'dx:{dx}'.format(x=self.dx)
        return 'dy:{dy}'.format(y=self.dy)
        return 'dvx:{dvx}'.format(vx=self.dvx)
        return 'dvy:{dvy}'.format(vy=self.dvy)
    

" This class represents attribute everything about the individual planets "
class Planets:
    def __init__(self):
        " self.k will pull attributes from the kinematics class and assign it to the planet"
        " self.r is the radius of the planet"
        
        # Predetermined planets
        if Planets == 0:
            self.k = kinematics(200,500, 2, 1)
            self.r = 1.0
        if Planets == 1:
            self.k = kinematics(500, 750, 1, 0)
            self.r = 1.0
        
        # Now, let's have the program assign the other planets random positions and velocities
        else:
            # Kinematics(random x, random y, random vx, random vy)
            self.k = kinematics(float(ran.randint(0,w_window)), float(ran.randint(0,h_window)), float(ran.randint(0, 300)/100)-1.5, float(ran.randint((0,300)/100)-1.5))
            self.r = ran.randint(0,3)
            self.massRadius()
            self.merged = False                     # Merged comes later in the program
    
    def __repr__(self):
        return repr(self.k)
    
    def massRadius(self):
        " Will be used to determine the mass of the planet from the randomly generated radius of the planet"
        self.m = density*4*math.pi*(self.r**3)/3
    
    def radiusMass(self):
        " Will be used after the planets have merged"
        self.r = (3*self.m/(density*4*math.pi))**(0.333333)
    
    def accelerate(self, kinematics, unused_t):
        ax = 0.0
        ay = 0.0
        for i in planetlist:
            if i is self or i.merged:
                # This is to make sure it ignores any merged planet
                continue
            dx = i.k.x - kinematics.x
            dy = i.k.y - kinematics.y
            dist = dx*dx + dy*dy        # distance squared
            dr = math.sqrt(dist)        # distance
            gravityforce = G*self.m*i.m/dr if dsq > 1e-10 else 0
            ax += force*dx/dr
            ay += force*dy/dr
        return (ax, ay)
    
    def intialDerivative(self, kinematics, t):
        " Runge Kutta was the method that would be needed to solve this"
        ax, ay = self.accelerate(kinematics, t)
        return derivatives(kinematics.vx, kinematics.vy, ax, ay)
    
    def nextDerivative(self, initialkinematic, derivative, t, dt):
        state = kinematics(0, 0, 0, 0)
        state.x = initialkinematic.x + derivative.dx*dt
        state.y = initialkinematic.y + derivative.dy*dt
        state.vx = initialkinematic.vx + derivative.dvx*dt
        state.vy = initialkinematic.vy + derivative.dvx*dt
        ax, ay = self.accelerate(state, t+dt)
        return derivatives(state.vx, state.vy, ax, ay)
    
    def updateplanets(self, t, dt):
        "Even more Runge-Kutta to update planet's position and velocity"
        A = self.initialDerivative(self.k, t)
        B = self.nextDerivative(self.k, A, t, dt*0.5)
        C = self.nextDerivative(self.k, B, t, dt*0.5)
        D = self.nextDerivative(self.k, C, t, dt)
        dxdt = 1.0/6.0*(A.dx + 2.0*(B.dx + C.dx) + D.dx)
        dydt = 1.0/6.0*(A.dy + 2.0*(B.dy + C.dy) + D.dy)
        dvxdt = 1.0/6.0*(A.dvx + 2.0*(B.dvx + C.dvx) + D.dvx)
        dvydt = 1.0/6.0*(A.dvy + 2.0*(B.dvy + C.dvy) + D.dvx)
        self.k.x += dxdt*dt
        self.k.y += dydt*dt
        self.k.vx += dvxdt*dt
        self.k.vy += dvydt*dt
        

""" THe following code is, for the most part, copy-pasted from one of the source codes, as i have zero experience programming
animations and especially in pygame. Whoops """

def main():
    pygame.init()
    win = pygame.display.set_mode((w_window, h_window))
    
    keysPressed = defaultdict(bool)
    
    def ScanKeyboard():
        while True:
            # Update the keyPressed state
            evt = pygame.event.poll()
            if evt.type == pygame.NOEVENT:
                break
            elif evt.type in [pygame.KEYDOWN, pygame.KEYUP]:
                keysPressed[evt.key] = evt.type == pygame.KEYDOWN
        
    global planetlist, PLANETS
    if lens(sys.argv) == 2:
        PLANETS = int(sys.argv[1])
    
    planetlist = []
    for p in xrange(0,PLANETS):
        planetlist.append(Planets())
        
    def planetTouch(i1, i2):
        dx = i1.k.x - i2.k.x
        dy = i2.k.y - i2.k.y
        dist = dx*dx + dy*dy
        dr = math.sqrt(dist)
        return dr <= (i1.r + i2.r)
    
    Star = Planet()
    Star.k.x, Star.k.y = (w_window/2), (h_window/2)         # Centered in the middle of the page
    Star.k.vy = Star.k.vx = 0                               # No velocities
    Star.m = 1000                                           # Mass is incredibly massive
    Star.radiusMass()
    planetlist.append(Star)
    for i in planetlist:
        if i is Star:
            continue
        if planetTouch(i, Star):
            i.merged = True                 # Ignores planets inside the sun
            
    # Zoom factor, changed at runtime via '+' and '-' numeric keypad keys
    zoom = 1.0
    t = 0
    dt = 1
    
    bClearScreen = True
    pygame.display.set_caption('Gravity simulation (SPACE: show orbits, ''keypad +/- : zoom in/out)')
    
    while True:
        t += dt
        pygame.display.flip()
        if bClearScreen:        # Show orbits or not?
            win.fill((0,0,0))
        win.lock()
        for i in planetlist:
            if not i.merged:
                pygame.draw.circle(win, (255,255,255),
                (int(w2 + zoom*w2*(i.k.x - w2)/w2),
                 int(h2 + zoom*h2*(i.k.y - h2)/h2),
                 int(i.r*zoom), 0))
        win.unlock()
        ScanKeyboard()
        
        " Update all planet positions and speeds"
        for i in planetlist:
            if i.merged or i is Star:
                continue
            i.updateplanets(t, dt)
        
        for i1 in planetlist:
            if i1.merged:
                continue
            for i2 in planetlist:
                if i1 is i2 or i2.merged:
                    continue
                if planetTouch(i1, i2):
                    if i1.m < i2.m:
                        i1, i2 = i2, i1             # In here, i1 is the heaviest one
                    i2.merged = True
                    if i1 is Star:
                        continue                    # Moving a star?? HAHAHAHAHAHAHAHAHA nice one
                    newvx = (i1.k.vx*i1.m + i2.k.vx*i2.m)/(i1.m + i2.m)             # Elastic collision equation
                    newvy = (i1.k.vy*i1.m + i2.k.vy*i2.m)/(i1.m + i2.m)
                    i1.m += i2.m        # maintain new mass
                    i1.radiusMass       # New mass means new radius
                    i1.k.vx, i1.k.vy = newvx, newvy
                    
                    
        # Update our zoom factors
        if keysPressed[pygame.K_KP_PLUS]:
            zoom /= 0.99
        if keysPressed[pygame.K_KP_MINUS]:
            zoom /= 1.01
        if keysPressed[pygame.K_ESCAPE]:
            break
        if keysPressed[pygame.K_SPACE]:
            while keysPressed[pygame.K_SPACE]:
                ScanKeyboard()
            bClearScreen = not bClearScreen
            verb = "show" if bClearScreen else "hide"
            pygame.display.set_caption(
                    'Gravity simulation (SPACE: "%s orbits, keypad +/- : zoom in/out)' % verb)
            
        


    