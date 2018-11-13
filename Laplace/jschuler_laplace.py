# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:22:35 2018

@author: Jared
"""

import numpy as np
import matplotlib.pyplot as plt

Ngrid = 100                         # Boundary conditions. 100x100 box
Niterations = 1000

# The entire worksheet is meant to look similar, since the code is easily modified for all of the situations required.
# Almost all code (the first set of for loops in part 1 comes from Jesse) builds off of the code provided by Lado.  

def part1():                # Square box in the center
    phi = np.zeros((Ngrid, Ngrid))
    phi_new = np.zeros((Ngrid,Ngrid))
    
    for i in range(Ngrid):
        for j in range(Ngrid):
            if i >= 40 and i <= 60 and j >= 40 and j <= 60:
                phi[i][j] = 100
            elif i == 0 and j == 0:
                phi[i][j] = 0
            else:
                phi[i][j] = ((i-50)**2 + (j-50)**2)**-1 * 10000
            
    for k in range(Niterations):
        for i in range(Ngrid):
            for j in range(Ngrid):
                if i >= 40 and i <= 60 and j >= 40 and j <= 60:
                    phi_new[i][j] = 100
                # These two lines of code (35-36) are meant to be repeated throughout the entire submission. Very effective.
                elif 0 < i < Ngrid - 1 and 0 < j < Ngrid - 1:                           
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4
                else:
                    phi_new[i][j] = 0
        phi = np.copy(phi_new)
    plt.title('Part 1: Square Box')
    plt.imshow(phi)
    plt.show()
    

def part2():                # Parallel Plate Capacitor
    phi = np.zeros((Ngrid, Ngrid))
    phi_new = np.zeros((Ngrid, Ngrid))
    
    for i in range(25,75):              # Rods will extend from y = 25 to y = 75, regardless of x placement
        phi[i][45] = 1                  # Placement of Rod 1
        phi[i][55] = -1                 # Placement of Rod 2
        
    for a in range(Niterations):
        for i in range(Ngrid):
            for j in range(Ngrid):
                if i >= 25 and i <= 75 and j == 45:
                    phi_new[i][j] = 1
                elif i >= 25 and i <= 75 and j == 55:
                    phi_new[i][j] = -1
                elif 0 <= i < Ngrid - 1 and 0 <= j < Ngrid-1:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4
        phi = np.copy(phi_new)
    plt.title('Part 2: Parallel Plate Capacitors')
    plt.imshow(phi)
    plt.show()
    
def part3():                # Perpendicular Plates
    phi = np.zeros((Ngrid, Ngrid))
    phi_new = np.zeros((Ngrid, Ngrid))
    
    for i in range(25,75):              # Vertical rod placed at x = 25, extends from y = 25 to y = 75
        phi[i][25] = 1
    
    for i in range(30,70):              # Horizontal rod placed at y = 50, extends from x = 30 to x = 70
        phi[50][i] = -1
    
    for a in range(Niterations):
        for i in range(Ngrid):
            for j in range(Ngrid):
                if i >= 25 and i <= 75 and j == 25:
                    phi_new[i][j] = 1
                elif i == 50 and j >= 40 and j <= 90:
                    phi_new[i][j] = -1
                elif 0 <= i < Ngrid - 1 and 0 <= j < Ngrid-1:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4
        phi = np.copy(phi_new)
    plt.title('Part 3: Perpendicular Plates')
    plt.imshow(phi)
    plt.show()

def part4():                # Charge in a box
    phi = np.zeros((Ngrid, Ngrid))
    phi_new = np.zeros((Ngrid, Ngrid))
    
    phi[50][50] = 1             # Charge is in the center of the box
    
    for a in range(Niterations):
        for i in range(Ngrid):
            for j in range(Ngrid):
                if i == 50 and j == 50:
                    phi_new[i][j] = 1
                elif 0 <= i < Ngrid - 1 and 0 <= j < Ngrid-1:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4
        phi = np.copy(phi_new)
    plt.title('Part 4: Particle in the center')
    plt.imshow(phi)
    plt.show()

def part5():                # Charge near the edge of the box
    phi = np.zeros((Ngrid, Ngrid))
    phi_new = np.zeros((Ngrid, Ngrid))
    
    phi[5][50] = 1          # Charge is placed near the center-top of the box
    
    for a in range(Niterations):
        for i in range(Ngrid):
           for j in range(Ngrid):
               if i == 5 and j == 50:
                   phi_new[i][j] = 1
               elif 0 <= i < Ngrid - 1 and 0 <= j < Ngrid-1:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4
        phi = np.copy(phi_new)
    plt.title('Part 5: Particle near the edge')
    plt.imshow(phi)
    plt.show()


# This part doesn't feel right, but I am submitting anyways.
def part6():                # Dipole in a grounded box
    phi = np.zeros((Ngrid, Ngrid))
    phi_new = np.zeros((Ngrid, Ngrid))
    
    phi[50][45] = 1             # Placement of Particle 1
    phi[50][55] = -1            # Placement of Particle 2
    
    for a in range(Niterations):
        for i in range(Ngrid):
            for j in range(Ngrid):
                if i == 50 and j == 45:
                    phi_new[i][j] = 1
                if i == 50 and j == 55:
                    phi_new[i][j] = -1
                elif 0 <= i < Ngrid - 1 and 0 <= j < Ngrid-1:
                    phi_new[i][j] = (phi[i-1][j] + phi[i+1][j] + phi[i][j-1] + phi[i][j+1])/4
        phi = np.copy(phi_new)
    plt.title('Part 6: Dipole in a grounded box')
    plt.imshow(phi)
    plt.show()

part1()
part2()
part3()
part4()
part5()   
part6() 