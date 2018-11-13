# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:04:17 2018

@author: Camden
"""

import numpy as np
import matplotlib.pyplot as plt

# Initial conditions are the only thing that should be adjusted. Other parameters
# will correct themselves to fit initial conditions, as long as each condition
# is kept even/odd

#------------------------------------------------------------------------------

# Problem 1: Square in a box

# Sets initial conditions
stepLimit = 200
gridSize = 50
squareSize = 10

# Start and end index of interior square
squareStart = int((gridSize - squareSize) / 2)
squareEnd = int((gridSize + squareSize) / 2)

# Initializes (gridSize x gridSize) grid with all 0's
grid = [np.zeros(gridSize) for i in range(gridSize)]

# Sets potential of tiles in interior square to 1
for i in range(gridSize):
    for j in range(gridSize):
        if i in range(squareStart, squareEnd) and j in range(squareStart, squareEnd):
            grid[i][j] = 1

# Loops through every tile n times
for n in range(stepLimit):
    for i in range(gridSize):
        for j in range(gridSize):
            
            # Does nothing to tile if it is in the interior square
            if i in range(squareStart, squareEnd) and j in range(squareStart, squareEnd):
                pass
            
            else:
                # x and y coordinates of surrounding tiles
                x = [i - 1, i, i + 1, i - 1, i + 1, i - 1, i, i + 1]
                y = [j + 1, j + 1, j + 1, j, j, j - 1, j - 1, j -1]
                # Tracks total potential and number of samples for each group of tiles
                adjacentSamples = 0
                diagonalSamples = 0
                adjacentTotal = 0
                diagonalTotal = 0
                
                # Loops through diagonally touching and adjacent tiles
                for k in range(8):
                    # Tries to add the tile's potential to total
                    try:
                        # Runs if tile is diagonally touching
                        if k == 0 or k == 2 or k == 5 or k == 7:
                            diagonalTotal += grid[ x[k] ][ y[k] ]
                            diagonalSamples += 1
                        # Runs if tile is adjacent
                        else:
                            adjacentTotal += grid[ x[k] ][ y[k] ]
                            adjacentSamples += 1
                    # Does nothing if tile is off the grid
                    except:
                        pass
                
                # Sets current tile to weighted total of average potentials
                grid[i][j] = (2.0/3.0) * (adjacentTotal/adjacentSamples) + (1.0/3.0) * (diagonalTotal/diagonalSamples)
    
# Graphs the grid in a heatmap
plt.imshow(grid, cmap='hot', interpolation='nearest')
plt.show()

#------------------------------------------------------------------------------

# Problem 2: Parallel Plate Capacitor

## Sets initial conditions
#stepLimit = 400
#gridSize = 50
#plateLength = 20
#plateSeparation = 6
#
## Top and bottom index of plates
#plateTop = int((gridSize - plateLength) / 2)
#plateBot = int((gridSize + plateLength) / 2)
## X coordinates of each plate
#xPlate1 = int((gridSize - plateSeparation) / 2)
#xPlate2 = int((gridSize + plateSeparation) / 2)
#
## Initializes (gridSize x gridSize) grid with all 0's
#grid = [np.zeros(gridSize) for i in range(gridSize)]
#
## Sets potential of plates to 1 and -1
#for i in range(gridSize):
#    for j in range(gridSize):
#        if j in range(plateTop, plateBot):
#            if i == xPlate1:
#                grid[i][j] = 1
#            elif i == xPlate2:
#                grid[i][j] = -1
#
## Loops through every tile n times
#for n in range(stepLimit):
#    for i in range(gridSize):
#        for j in range(gridSize):
#            
#            # Does nothing to tile if it is in one of the plates
#            if (i == xPlate1 or i == xPlate2) and j in range(plateTop, plateBot):
#                pass
#            
#            else:
#                # x and y coordinates of surrounding tiles
#                x = [i - 1, i, i + 1, i - 1, i + 1, i - 1, i, i + 1]
#                y = [j + 1, j + 1, j + 1, j, j, j - 1, j - 1, j -1]
#                # Tracks total potential and number of samples for each group of tiles
#                adjacentSamples = 0
#                diagonalSamples = 0
#                adjacentTotal = 0
#                diagonalTotal = 0
#                
#                # Loops through diagonally touching and adjacent tiles
#                for k in range(8):
#                    # Tries to add the tile's potential to total
#                    try:
#                        # Runs if tile is diagonally touching
#                        if k == 0 or k == 2 or k == 5 or k == 7:
#                            diagonalTotal += grid[ x[k] ][ y[k] ]
#                            diagonalSamples += 1
#                        # Runs if tile is adjacent
#                        else:
#                            adjacentTotal += grid[ x[k] ][ y[k] ]
#                            adjacentSamples += 1
#                    # Does nothing if tile is off the grid
#                    except:
#                        pass
#                
#                # Sets current tile to weighted total of average potentials
#                grid[i][j] = (2.0/3.0) * (adjacentTotal/adjacentSamples) + (1.0/3.0) * (diagonalTotal/diagonalSamples)
#    
## Graphs the grid in a heatmap
#plt.imshow(grid, cmap='hot', interpolation='nearest')
#plt.show()
              
#------------------------------------------------------------------------------

# Problem 3: Perpendicular Plates

## Sets initial conditions
#stepLimit = 400
#gridSize = 50
#plateLength = 20
#plateSeparation = 3
#
## Important indexes of plates
#xPlate1 = int((gridSize - plateSeparation - plateLength - 1) / 2)
#yPlate2 = int(gridSize / 2)
#plate1Top = int((gridSize - plateLength) / 2)
#plate1Bot = int((gridSize + plateLength) / 2)
#plate2Start = xPlate1 + plateSeparation
#plate2End = plate2Start + plateLength
#
## Initializes (gridSize x gridSize) grid with all 0's
#grid = [np.zeros(gridSize) for i in range(gridSize)]
#
## Sets potential of plates to 1 and -1
#for i in range(gridSize):
#    for j in range(gridSize):
#        if i == xPlate1 and j in range(plate1Top, plate1Bot):
#            grid[i][j] = 1
#        elif j == yPlate2 and i in range(plate2Start, plate2End):
#            grid[i][j] = -1
#
## Loops through every tile n times
#for n in range(stepLimit):
#    for i in range(gridSize):
#        for j in range(gridSize):
#            
#            # Does nothing to tile if it is in one of the plates
#            if (i == xPlate1 and j in range(plate1Top, plate1Bot)) or (j == yPlate2 and i in range(plate2Start, plate2End)):
#                pass
#            
#            else:
#                # x and y coordinates of surrounding tiles
#                x = [i - 1, i, i + 1, i - 1, i + 1, i - 1, i, i + 1]
#                y = [j + 1, j + 1, j + 1, j, j, j - 1, j - 1, j -1]
#                # Tracks total potential and number of samples for each group of tiles
#                adjacentSamples = 0
#                diagonalSamples = 0
#                adjacentTotal = 0
#                diagonalTotal = 0
#                
#                # Loops through diagonally touching and adjacent tiles
#                for k in range(8):
#                    # Tries to add the tile's potential to total
#                    try:
#                        # Runs if tile is diagonally touching
#                        if k == 0 or k == 2 or k == 5 or k == 7:
#                            diagonalTotal += grid[ x[k] ][ y[k] ]
#                            diagonalSamples += 1
#                        # Runs if tile is adjacent
#                        else:
#                            adjacentTotal += grid[ x[k] ][ y[k] ]
#                            adjacentSamples += 1
#                    # Does nothing if tile is off the grid
#                    except:
#                        pass
#                
#                # Sets current tile to weighted total of average potentials
#                grid[i][j] = (2.0/3.0) * (adjacentTotal/adjacentSamples) + (1.0/3.0) * (diagonalTotal/diagonalSamples)
#    
## Graphs the grid in a heatmap
#plt.imshow(grid, cmap='hot', interpolation='nearest')
#plt.show()  
                
#------------------------------------------------------------------------------

# Problem 4: Charge in a box

## Sets initial conditions
#stepLimit = 400
#gridSize = 51
#
## Indexes of charges
#xCharge = int(np.floor(gridSize / 2.0))
#yCharge = xCharge
#
## Initializes (gridSize x gridSize) grid with all 0's, except for the charge
#grid = [np.zeros(gridSize) for i in range(gridSize)]
#grid[xCharge][yCharge] = 1
#
## Loops through every tile n times
#for n in range(stepLimit):
#    for i in range(gridSize):
#        for j in range(gridSize):
#            
#            # Does nothing to tile if it is the tile of the charge
#            if i == xCharge and j == yCharge:
#                pass
#            
#            else:
#                # x and y coordinates of surrounding tiles
#                x = [i - 1, i, i + 1, i - 1, i + 1, i - 1, i, i + 1]
#                y = [j + 1, j + 1, j + 1, j, j, j - 1, j - 1, j -1]
#                # Tracks total potential and number of samples for each group of tiles
#                adjacentSamples = 0
#                diagonalSamples = 0
#                adjacentTotal = 0
#                diagonalTotal = 0
#                
#                # Loops through diagonally touching and adjacent tiles
#                for k in range(8):
#                    # Tries to add the tile's potential to total
#                    try:
#                        # Runs if tile is diagonally touching
#                        if k == 0 or k == 2 or k == 5 or k == 7:
#                            diagonalTotal += grid[ x[k] ][ y[k] ]
#                            diagonalSamples += 1
#                        # Runs if tile is adjacent
#                        else:
#                            adjacentTotal += grid[ x[k] ][ y[k] ]
#                            adjacentSamples += 1
#                    # Does nothing if tile is off the grid
#                    except:
#                        pass
#                
#                # Sets current tile to weighted total of average potentials
#                grid[i][j] = (2.0/3.0) * (adjacentTotal/adjacentSamples) + (1.0/3.0) * (diagonalTotal/diagonalSamples)
#    
## Graphs the grid in a heatmap
#plt.imshow(grid, cmap='hot', interpolation='nearest')
#plt.show()  
                
#------------------------------------------------------------------------------

# Problem 5: Charge in a box (Part 2)

## Sets initial conditions
#stepLimit = 400
#gridSize = 51
#yCharge = 2
#
## X coordinate of charge
#xCharge = int(np.floor(gridSize / 2.0))
#
## Initializes (gridSize x gridSize) grid with all 0's, except for the charge
#grid = [np.zeros(gridSize) for i in range(gridSize)]
#grid[xCharge][yCharge] = 1
#
## Loops through every tile n times
#for n in range(stepLimit):
#    for i in range(gridSize):
#        for j in range(gridSize):
#            
#            # Does nothing to tile if it is the tile of the charge
#            if i == xCharge and j == yCharge:
#                pass
#            
#            else:
#                # x and y coordinates of surrounding tiles
#                x = [i - 1, i, i + 1, i - 1, i + 1, i - 1, i, i + 1]
#                y = [j + 1, j + 1, j + 1, j, j, j - 1, j - 1, j -1]
#                # Tracks total potential and number of samples for each group of tiles
#                adjacentSamples = 0
#                diagonalSamples = 0
#                adjacentTotal = 0
#                diagonalTotal = 0
#                
#                # Loops through diagonally touching and adjacent tiles
#                for k in range(8):
#                    # Tries to add the tile's potential to total
#                    try:
#                        # Runs if tile is diagonally touching
#                        if k == 0 or k == 2 or k == 5 or k == 7:
#                            diagonalTotal += grid[ x[k] ][ y[k] ]
#                            diagonalSamples += 1
#                        # Runs if tile is adjacent
#                        else:
#                            adjacentTotal += grid[ x[k] ][ y[k] ]
#                            adjacentSamples += 1
#                    # Does nothing if tile is off the grid
#                    except:
#                        pass
#                
#                # Sets current tile to weighted total of average potentials
#                grid[i][j] = (2.0/3.0) * (adjacentTotal/adjacentSamples) + (1.0/3.0) * (diagonalTotal/diagonalSamples)
#    
## Graphs the grid in a heatmap
#plt.imshow(grid, cmap='hot', interpolation='nearest')
#plt.show() 

#------------------------------------------------------------------------------

# Problem 6: Dipole in a box

## Sets initial conditions
#stepLimit = 400
#gridSize = 50
#dipoleLength = 10
#
## Important indexes of plates
#xCharge1 = int(np.floor(gridSize / 2.0))
#xCharge2 = xCharge1
#yCharge1 = int((gridSize - dipoleLength) / 2)
#yCharge2 = yCharge1 + dipoleLength
#
## Initializes (gridSize x gridSize) grid with all 0's, except for the charges
#grid = [np.zeros(gridSize) for i in range(gridSize)]
#grid[xCharge1][yCharge1] = 1
#grid[xCharge2][yCharge2] = -1
#
## Loops through every tile n times
#for n in range(stepLimit):
#    for i in range(gridSize):
#        for j in range(gridSize):
#            
#            # Does nothing to tile if it is the tile one of the charges
#            if (i == xCharge1 and j == yCharge1) or (i == xCharge2 and j == yCharge2):
#                pass
#            
#            else:
#                # x and y coordinates of surrounding tiles
#                x = [i - 1, i, i + 1, i - 1, i + 1, i - 1, i, i + 1]
#                y = [j + 1, j + 1, j + 1, j, j, j - 1, j - 1, j -1]
#                # Tracks total potential and number of samples for each group of tiles
#                adjacentSamples = 0
#                diagonalSamples = 0
#                adjacentTotal = 0
#                diagonalTotal = 0
#                
#                # Loops through diagonally touching and adjacent tiles
#                for k in range(8):
#                    # Tries to add the tile's potential to total
#                    try:
#                        # Runs if tile is diagonally touching
#                        if k == 0 or k == 2 or k == 5 or k == 7:
#                            diagonalTotal += grid[ x[k] ][ y[k] ]
#                            diagonalSamples += 1
#                        # Runs if tile is adjacent
#                        else:
#                            adjacentTotal += grid[ x[k] ][ y[k] ]
#                            adjacentSamples += 1
#                    # Does nothing if tile is off the grid
#                    except:
#                        pass
#                
#                # Sets current tile to weighted total of average potentials
#                grid[i][j] = (2.0/3.0) * (adjacentTotal/adjacentSamples) + (1.0/3.0) * (diagonalTotal/diagonalSamples)
#    
## Graphs the grid in a heatmap
#plt.imshow(grid, cmap='hot', interpolation='nearest')
#plt.show()             
                