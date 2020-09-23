import random,time,copy

WIDTH = 60
HEIGHT = 20

# Creat a list of list for the cells:
nextCells = []

for x in range(WIDTH):
    column = []  #Create a new column.
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') #add a living cell.
        else:
            column.append(' ') #add a dead cell.
    nextCells.append(column) #nextCells is a list of column lists.

while True:
    print('\n\n\n\n\n') #Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    #prints currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end ='') #print the # or space.
        print() #Prints a newline at the end of the row.

     #Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighbooring coordinates:
            # '% WIDTH' ensures leftCOord is always between 0 and WIDTH -1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCOord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighborrs:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCOord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCOord] == '#':
                numNeighbors += 1 #Top-right neighbor is alive.
            if currentCells[rightCoord][aboveCOord] == '#':
                numNeighbors += 1 # top-right nighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 #left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 #Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 #bottom0left neighboer is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom nieghbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 #bottom-right neighbor is alive.

            # Set cell based on Comway's Game of livfe rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
                # Dead cells with 3 neighbors becom alive:
            else:
                nextCells[x][y] = ' '
                # Everything else dies or stays dead:
time.sleep(2) # this Add a 1-second pause to reuce flickering.


