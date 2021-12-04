'''
Task #1 – Sudoku Puzzle Solver                                                                         (35 Points)

Problem Description:
Sudoku is a number-placement problem in which a partially filled 9x9 grid is filled with digits
from 1 to 9. The 9x9 grid itself consists of 9 sub-girds of size 3x3. The objective of this
puzzle is to assign single digits from 1 to 9 in empty cells of this grid such that every row,
every column and every sub-gird contains exactly one instance of the numbers between1 to 9.

Use backtracking technique to solve a given Sudoku Puzzle.

INPUT:

    Your program must read from an input.txt file which contains a partially filled 9x9 gird
    of numbers. (To represent empty cells use 0 or -1).

OUTPUT: 

    Print the solved puzzle in format of a 9x9 grid.
'''

def printGrid(gridPrint):
    for i in range(9):
        #print("i = " + str(i))
        if (i % 3 == 0) and (i != 0): # blank line after 3 rows
            print()
        printStr = ""
        for j in range(9):
            #print("j = " + str(j))
            if (j % 3 == 0) and (j != 0): # doublt space after 3 columns
                printStr += " "
            printStr += str(gridPrint[i][j])
        print(printStr)

# Check if a prospective value is promising
def isPromising(row,col,digit):
    switch = True
    if switch:
        for i in range(9): # checks row for same number
            if grid[row][i] == digit:
                switch = False
    if switch:
        for i in range(9): # checks column for same number
            if grid[i][col] == digit:
                switch = False
    if switch:
        # checks "big square" (3x3) for same number
        bigSquareRow = (row // 3) * 3 # row of "big square"
        bigSquareCol = (col // 3) * 3 # col of "big square"
        for i in range(3):
            for j in range(3):
                if grid[bigSquareRow + i][bigSquareCol + j] == digit:
                    switch = False    
    return switch


def solve():
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0: # If space is blank
                for digit in range(1,10): # Assigns a number 1-9 to a square
                    if isPromising(row,col,digit): # Checks if the number is promising
                        grid[row][col] = digit # A promising solution is reached
                        solve() # backtracking
                        grid[row][col] = 0
                return
    print("\nSolution grid:")
    printGrid(grid)


grid = []


with open('sudoku-input.txt') as f:
    for i in range(9):
        line = []
        for x in next(f).split():
            line.append(int(x))
        grid.append(line)

print("Initial grid:")
printGrid(grid)

solve()