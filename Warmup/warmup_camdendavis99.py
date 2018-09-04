# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:21:27 2018

@author: Camden
"""

import numpy as np
import matplotlib.pyplot as plt

#     To run each problem, uncomment the lines which actually run the function
# beneath each problem. The explanation/analysis of each graph is below
# each line that runs the function.

# Problem 1: Radioactive Decay

def Problem1(N0, tau):
    # Initializes all constants and variables
    partitions = 10000
    t_i = 0
    t_f = 4 * tau
    dt = (t_f - t_i) / partitions
    t = np.linspace(t_i, t_f, partitions + 1)
    
    # Creates N as an array filled with zeroes as placeholders
    N = np.zeros(partitions + 1)
    N[0] = N0
    
    # Generates all values of N
    for i in range(1, partitions + 1):
        dN = -N[i - 1] / tau
        N[i] = N[i - 1] + (dN * dt)
        
    # Plots graph of N with labeled axes
    plt.plot(t, N, 'go')
    plt.plot(t, N0 * np.exp(-t / tau), 'y-')
    plt.xlabel("Time in millions of years")
    plt.ylabel("Number of atoms in N")
    plt.title("Atoms in N vs. Time")
    
#Problem1(8, 703.8)
# This graph appears like you would expect it to, as the number of atoms is
# halved when t ~= 700, which is equivalent to the particle's half-life.

#Problem1(16, 1000)
# Setting N0 equal to 16 (a power of 2) and tau to 1000 makes it more apparent
# that the graph is halved at each half-life.

#     I trust this graph, because I have graphed the analytic solution to the
# equation with it, and it lines of perfectly with my solution.

#------------------------------------------------------------------------------

# Problem 2: Population Growth

def Problem2(N0, a, b):
    # Initializes all constants and variables
    partitions = 100000
    t_i = 0
    t_f = 30
    dt = (t_f - t_i) / partitions
    t = np.linspace(t_i, t_f, partitions + 1)
    
    # Creates N as an array filled with zeroes as placeholders
    N = np.zeros(partitions + 1)
    N[0] = N0
    
    # Finds and records each value of N in an array
    for i in range(1, partitions + 1):
        dN = (a * N[i - 1]) - (b * (N[i - 1] * N[i - 1]))
        N[i] = N[i - 1] + (dN * dt)
        
    # Plots graph of N with labeled axes
    plt.plot(t, N, 'r')
    plt.xlabel("Time in years")
    plt.ylabel("Population")
    plt.title("Population vs. Time")

#Problem2(5, 0.47, 0.0005)
# With these cherry-picked values for alpha (a) and beta (b), the behavior of
# the function is shown pretty clearly. With a small beta and large alpha, the
# function increases slowly initially, then speeds up before slowing down and
# reaching a plateau at a value of ~a/b.
    
#Problem2(5, 10, 1)
# By graphing the funciton with alpha = 10 and beta = 1, it clearly shows that
# my guess was correct, and the graph plateaus at a/b.

#Problem2(100, 10, 10)
# The graph grows rapidly with a high value of alpha, and will decrease
# if the value of beta is too large, as shown by this graph.

#     I trust my solution of this equation, even though no analytic solution is
# available to compare it to, because the behavior of the graph is predictable
# by the function, since high values of beta cause it to decrease rapidly,
# while high values of alpha cause it to increase.

#------------------------------------------------------------------------------

# Problem 3: Coupled Radioactive Decay

def Problem3(NA0, NB0, tauA, tauB):
    # Initializes all constants and variables
    partitions = 10000
    t_i = 0
    t_f = 10 * tauA
    dt = (t_f - t_i) / partitions
    t = np.linspace(t_i, t_f, partitions + 1)
    
    # Creates NA and NB as an array filled with zeroes as placeholders
    NA = np.zeros(partitions + 1)
    NB = np.zeros(partitions + 1)
    NA[0] = NA0
    NB[0] = NB0
    
    # Generates all values of NA and NB
    for i in range(1, partitions + 1):
        dNA = -NA[i - 1] / tauA
        NA[i] = NA[i - 1] + (dNA * dt)
        dNB = -dNA - (NB[i - 1] / tauB)
        NB[i] = NB[i - 1] + (dNB * dt)
        
    # Plots graph of N with labeled axes
    plt.plot(t, NA, 'r', label = "Sample A")
    plt.plot(t, NB, 'b', label = "Sample B")
    plt.xlabel("Time in millions of years")
    plt.ylabel("Number of atoms in NA and NB")
    plt.title("Atoms vs. Time")
    plt.legend()
    
#Problem3(100, 10, 0.1, 0.1)
# The graph behaves as expected, as sample B increases rapidly as there is
# an abundance of sample A.

#Problem3(10, 100, 0.5, 1)
# The opposite effect takes place as expected too. Even with a higher value of
# tauA and tauB, sample B is unable to increase due to the low amount of
# sample A.
    
#Problem3(50, 50, 0.000001, 1)
# When the value of tauA is decreased to an extremely small value, sample A
# completely decays into sample B almost instantly. Sample A increases by
# exactly the amount sample B decreases.

#     I trust my solution, as I have already previously proved my work for
# sample A back in problem 1. The only difference in this problem is sample B,
# which behaved as I expected it to.

#------------------------------------------------------------------------------

# Problem 4: Coupled Radioactive Decay - Part 2

def Problem4(NA0, NB0, tauA, tauB):
    # Initializes all constants and variables
    partitions = 10000
    t_i = 0
    t_f = 10 * tauA
    dt = (t_f - t_i) / partitions
    t = np.linspace(t_i, t_f, partitions + 1)
    
    # Creates NA and NB as an array filled with zeroes as placeholders
    NA = np.zeros(partitions + 1)
    NB = np.zeros(partitions + 1)
    NA[0] = NA0
    NB[0] = NB0
    
    # Generates all values of NA and NB
    for i in range(1, partitions + 1):
        dNA = (NB[i - 1] / tauB) - (NA[i - 1] / tauA)
        NA[i] = NA[i - 1] + (dNA * dt)
        dNB = -dNA
        NB[i] = NB[i - 1] + (dNB * dt)
        
    # Plots graph of N with labeled axes
    plt.plot(t, NA, 'r', label = "Sample A")
    plt.plot(t, NB, 'b', label = "Sample B")
    plt.xlabel("Time in millions of years")
    plt.ylabel("Number of atoms in NA and NB")
    plt.title("Atoms vs. Time")
    plt.legend()
    
#Problem4(10, 10, 3, 2)
# Sample A increases by the exact amount sample B decreases. This makes sense,
# since, dNA = -dNB.

#Problem4(10, 10, 2, 3)
# When tauB > tauA, sample B increases while sample A decreases.

#Problem4(10, 10, 1, 1)
# When tauA = tauB and N0A = N0B, neither function changes from its initial
# value. If you look at the initial differential equation for either dNA/dt or
# dNB/dt, it can be seen that when tauA = tauB, each term shares a common
# denominator, and they combine into one fraction. Then they subtract the other
# to equal 0. 
    
#Problem4(15, 10, 1, 1)
# When inital values are different but tauA = tauB, the functions either
# increase or decrease to the average value of the two, then stop moving.

#     The graph behaves exactly as expected, so I trust the results, even
# though there is no analytic solution to compare it to (as far as I know).










