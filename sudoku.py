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
        if (i%3 == 0) and (i != 0):
            print()
        printStr = ""
        for j in range(9):
            #print("j = " + str(j))
            if (j%3 == 0) and (j != 0):
                printStr += " "
            printStr += str(gridPrint[i][j])
        print(printStr)

# Check if a prospective value is promising
def isPromising(row,col,digit):
    switch = True
    if switch:
        for i in range(9):
            if grid[row][i] == digit:
                switch = False
    if switch:
        for i in range(9):
            if grid[i][col] == digit:
                switch = False
    if switch:
        square_row = (row//3)*3
        square_col = (col//3)*3
        for i in range(3):
            for j in range(3):
                if grid[square_row+i][square_col+j] == digit:
                    switch = False    
    return switch


def solve():
    #global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for digit in range(1,10): # here
                    if isPromising(row,col,digit):
                        grid[row][col] = digit
                        solve()
                        grid[row][col] = 0  #Backtrack step
                return
    printGrid(grid)

grid = []
with open('sudoku-input.txt') as f:
    for i in range(9):
        line = []
        for x in next(f).split():
            line.append(int(x))
        grid.append(line)

printGrid(grid)

solve()