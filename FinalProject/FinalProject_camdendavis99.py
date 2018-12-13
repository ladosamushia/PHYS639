# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:11:46 2018

@author: Camden
"""

# Camden Davis
# Final Project: Galton Board


import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


# This class represents the Galton Board
class Board:

    # Constructor - initializes slot and ball count for Board class
    def __init__(self, slots, balls):
        self.slots = slots
        self.balls = balls

        # Initializes array to store ball counts in each position
        self.slotCounts = [np.zeros(i + 1) for i in range(slots)]
        self.slotCounts[0][0] = balls


    # Prints number of balls in each spot. Used only for testing, but I figured
    # it's worth keeping.
    def printSlotCounts(self):
        for row in self.slotCounts:
            for slot in row:
                print(str(slot) + " ", end="")
            print()


    # Determines how many balls will bounce to the left off a peg
    def randomHalf(self, n):
        leftCount = 0
        # Loops through each ball in the current position
        for i in range(int(n)):
            if rand.ranf() < 0.5:  # 50% chance of running
                leftCount += 1     # Adds 1 ball to the total balls bouncing left
        return leftCount


    # Calculates the next row of ball locations on the board
    def calcNextRow(self, curRow):
        # Loops through each position in the current row
        for curSlot in range(curRow + 1):
            curSlotCount = self.slotCounts[curRow][curSlot]  # Stores count in current position
            nextLeftCount = self.randomHalf(curSlotCount)    # Calculates balls that bounce left
            nextRightCount = curSlotCount - nextLeftCount    # Calculates balls that bounce right

            # Updates the slots to which the balls bounce
            self.slotCounts[curRow + 1][curSlot] += nextLeftCount
            self.slotCounts[curRow + 1][curSlot + 1] += nextRightCount



# This class handles all statistical operations on the board
class Data:

    def __init__(self, data):
        # Stores the original data
        self.bins = len(data)
        self.origData = data
        self.origTotal = self.calcTotal(data)

        # Stores probablity data, then converts format of data for histograms and normal curves
        self.probData = self.numToProb(data, self.origTotal, self.bins)
        self.data = self.histConvert(data)

        # Final calculations on data
        self.N = len(self.data)
        self.total = self.calcTotal(self.data)
        self.mean = (self.bins-1) / 2.0
        self.sd = self.calcSD(self.data, self.mean, self.N)


    # Converts an array of ball counts to a more usable format
    # e.g. {4, 1, 3} -> {0, 0, 0, 0, 1, 2, 2, 2}
    def histConvert(self, data):
        hist = []
        for i, val in enumerate(data):
            for j in range(int(val)):
                hist.append(i)
        return hist


    # Calculates the sum of all values in an array
    def calcTotal(self, data):
        total = 0.0
        for val in data:
            total += val
        return total


    # Calculates standard deviation of an array
    def calcSD(self, data, mean, N):
        sdTotal = 0.0
        for x in data:
            sdTotal += (x - mean)**2
        sd = np.sqrt(sdTotal / N)
        return sd


    # Converts an array of numbers to an array of probabilities
    def numToProb(self, data, total, N):
        newData = np.zeros(N)
        for index, val in enumerate(data):
            newData[index] = val / total
        return newData


    # Returns value of normal curve at a given x value
    def normalCurve(self, x, mean, sd):
        variance = sd*sd
        k = 1 / np.sqrt(2 * np.pi * variance)
        n = -(x - mean)**2 / (2 * variance)
        return k * np.exp(n)


    # Tests how likeness to the normal curve increases as slot number increases
    def slotTest(self):
        # Sets initial conditions
        balls = 50
        slotIncrement = 1
        maxSlotCount = 100
        # Initializes arrays to store data
        initialSlotCounts = [slotIncrement*(n+1) for n in range(int(maxSlotCount / slotIncrement))]
        deviations = np.zeros(len(initialSlotCounts))

        # Loops through numbers of balls
        for index, slotCount in enumerate(initialSlotCounts):
            # Creates new Board object
            board = Board(slotCount, balls)
            # Simulates the ball falling down the board
            for curRow in range(0, slotCount - 1):
                board.calcNextRow(curRow)

            # Gets final slot counts and re-initializes the Data class
            finalSlotCounts = board.slotCounts[len(board.slotCounts) - 1]
            self.__init__(finalSlotCounts)

            # Calculates variance
            totalVariance = 0
            for i, slotCount in enumerate(finalSlotCounts):
                totalVariance += (self.normalCurve(slotCount, self.mean, self.sd) - self.probData[i])**2
            # Stores the current value of deviation
            deviations[index] = (1.0 / self.N) * np.sqrt(totalVariance)

        # Plots the deviation of ball distribution from the normal curve
        self.plotDeviation(initialSlotCounts, deviations, "Number of Slots")


    # Tests how likeness to the normal curve increases as number of balls increases
    def ballTest(self):
        # Sets initial conditions
        slots = 12
        ballIncrement = 1
        maxBallCount = 50
        # Initializes arrays to store data
        initialBallCounts = [ballIncrement*(n+1) for n in range(int(maxBallCount / ballIncrement))]
        deviations = np.zeros(len(initialBallCounts))

        # Loops through numbers of balls
        for index, ballCount in enumerate(initialBallCounts):
            # Creates new Board object
            board = Board(slots, ballCount)
            # Simulates the ball falling down the board
            for curRow in range(0, slots - 1):
                board.calcNextRow(curRow)

            # Gets final slot counts and re-initializes the Data class
            finalSlotCounts = board.slotCounts[len(board.slotCounts) - 1]
            self.__init__(finalSlotCounts)

            # Calculates variance
            totalVariance = 0
            for i, slotCount in enumerate(finalSlotCounts):
                totalVariance += (self.normalCurve(slotCount, self.mean, self.sd) - self.probData[i])**2
            # Stores the current value of deviation
            deviations[index] = (1.0 / self.N) * np.sqrt(totalVariance)

        # Plots the deviation of ball distribution from the normal curve
        self.plotDeviation(initialBallCounts, deviations, "Number of Balls")


    # Plots current data
    def plotData(self):
        # Plots histogram of ball counts in each slot
        n, bins, patches = plt.hist(self.data, np.arange(0, self.bins+1), facecolor='blue', alpha=0.75, rwidth=0.85)
        plt.xlabel("Slot Number")
        plt.ylabel("Number of Balls")
        plt.title("Number of balls in each slot")
        plt.show()

        # Plots probability of a ball falling in each slot, compared to normal curve
        resolution = 100  # Resolution of x values
        x = np.linspace(0, self.bins-1, resolution) # x values
        plt.plot(self.probData, 'ro')               # Plots ball distribution
        plt.plot(x, mlab.normpdf(x, self.mean, self.sd))  # Plots normal curve
        plt.xlabel("Slot Number")
        plt.ylabel("Fraction of balls in slot")
        plt.title("Probability Density Compared to Gaussian Distribution")
        plt.show()

    # Plots the deviation of ball distribution from the normal curve
    def plotDeviation(self, x, data, title):
        plt.plot(x, data)
        plt.xlabel(title)
        plt.ylabel("Deviation of Ball Distribution from Normal Curve")
        plt.title("Deviation from Normal Curve Compared to {}".format(title))
        plt.show()


# This is the main class of the program, and controls the general flow of the program
class FinalProject_camdendavis99:

    # Prints an example of the Galton board
    def displayExample(self):
        pegCount = 8
        print(" "*(pegCount - 1) + "\\ /")

        for i in range(pegCount):
            print(" "*(pegCount - (i + 1)) + "/" + " " + "o "*i + "\\")
        print("|", end="")

        for i in range(pegCount):
            print(str(i + 1) + "|", end="")
        print("\n")


    # Prints introductory message
    def intro(self):
        print("\tThis program simulates the random behavior of a Galton Board.")
        print("Below is an example of a Galton Board, where a ball falls and bounces off pegs")
        print("along the way. This causes the balls to fall into the final slots according to")
        print("a normal distribution.")
        print()
        self.displayExample()


    # Gets input from the user as a positive integer
    def errorCheckedInput(self, message):
        returnValue = input(message)

        while True:
            try:
                returnValue = int(returnValue)
                if (returnValue < 1):
                    raise Exception()
                break

            except:
                print("\nError: must be a positive integer", end="")
                returnValue = input("Please enter a valid number: ")

        return returnValue


    # Main method, runs at start
    def main(self):
        # Prints introductory message
        self.intro()

        # Gets number of slots and balls from user input, and creates new Board object
        slots = self.errorCheckedInput("Enter number of slots: ")
        balls = self.errorCheckedInput("Enter number of balls: ")
        galtonBoard = Board(slots, balls)

        # Simulates the balls falling down the Galton Board
        for curRow in range(0, slots - 1):
            galtonBoard.calcNextRow(curRow)
        print()

        # Retrieves final slot counts
        counts = galtonBoard.slotCounts
        finalSlotCounts = counts[len(counts) - 1]

        # Creates new Data object for the ball distribution, and plots it
        data = Data(finalSlotCounts)
        data.plotData()
        # Tests and plots the relationship between devation from the normal
        # curve and number of slots/balls
        data.ballTest()
        data.slotTest()


# Runs main method
Run = FinalProject_camdendavis99()
Run.main()

