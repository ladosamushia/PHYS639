#some people were having trouble loading the IPython Notebook or do not use IPython Notebook so I converted the code to a regular python file

import numpy as np
try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk
import time

# Decide whether or not to flip the spin based on temperature (T), external magnetic field (B), and neighbourhood.
def flip_spin(i, j, T, B):
    # Neighbours are one step in each direction.
    # Unless you are on the boundary, in which case one neihgbour is missing (two if you are in a corner)
    if i == 0:
        s1 = 0
    else:
        s1 = spins[i-1,j]
    if i == Ngrid - 1:
        s2 = 0
    else:
        s2 = spins[i+1,j]
    if j == 0:
        s3 = 0
    else:
        s3 = spins[i,j-1]
    if j == Ngrid - 1:
        s4 = 0
    else:
        s4 = spins[i,j+1]
    # Initial and final energies of interaction with neighbours (first term) and the external magnetic field (second term)
    Eini = -(s1 + s2 + s3 + s4)*spins[i,j] - spins[i,j]*B
    Efin = -Eini
    # If final energy lower always flip
    if Eini > Efin:
        return True
    # If not it's more complicated
    else:
        # Flip based on this probability
        prob_no_flip = np.exp(-(Efin - Eini)/T)
        prob = np.random.rand()
        if prob < prob_no_flip:
            return True
        else:
            return False



# grid size
Ngrid = 80
# matrix for spins
spins = np.random.choice([-1, 1], (Ngrid, Ngrid))
# Temperature. Don't set to exactly zero because the exponential in flip_spin function may misbehave
T = 0.0001
# Strength of external magnetic field
B = 0

# Creating a window to draw on
master = tk.Tk()
window = tk.Canvas(master, width = 800, height = 800)
window.pack()

# Coordinates and the radius of circles representing particles on the animation
x = np.linspace(0, 800, Ngrid)
y = np.linspace(0, 800, Ngrid)
r_oval = 10
# We need Ngrid*Ngrid circles 
ovals = [[[] for i in range(Ngrid)] for j in range(Ngrid)]

# Random initial conditions
# red means spin up (+1) blue means spin down (-1)
for i in range(Ngrid):
    for j in range(Ngrid):
        if spins[i,j] == 1:
            color = 'red'
        else:
            color = 'blue'
        # Draw 
        ovals[i][j] = window.create_oval(x[i], y[j], x[i] + r_oval, y[j] + r_oval, fill=color)

# Number of steps for simulation
Nsteps = 10000000
for i in range(Nsteps):
    # Randomly choose a particle
    i_rand = np.random.randint(Ngrid)
    j_rand = np.random.randint(Ngrid)
    # Decide whether or not to flip its spin
    if flip_spin(i_rand,j_rand,T,B) == True:
        spins[i_rand,j_rand] = -spins[i_rand,j_rand]
        # Delete old sphere
        window.delete(ovals[i_rand][j_rand])
        if spins[i_rand,j_rand] == 1:
            color = 'red'
        else:
            color = 'blue'
        # Redraw with updated color
        ovals[i_rand][j_rand] = window.create_oval(x[i_rand], y[j_rand], x[i_rand] + r_oval, y[j_rand] + r_oval, fill=color)
    master.update()
master.mainloop()
