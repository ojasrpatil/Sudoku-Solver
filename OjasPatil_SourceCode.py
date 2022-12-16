'''
Description: This code creates a program that takes in 5 sudoku puzzles and solves them by using recursion.
Programmer Name: Ojas Patil
Date Created: 11/8/2022
Preconditons: There are no preconditions since the user does not need to input anything.
Postconditions: The program prints the name of the file, the unsolved puzzle, and the solved puzzle.
                If there is no solution to the puzzle, it prints "No solution found".
'''


board1 = [ #creates the first board to be solved
    [5,0,0,0,0,0,1,7,0], 
    [1,0,6,5,0,9,0,4,0], 
    [4,7,2,1,0,6,0,0,0], 
    [9,0,0,0,0,0,5,0,0], 
    [0,1,8,0,9,5,4,0,0], 
    [6,0,0,4,0,2,3,8,9], 
    [0,4,0,0,0,0,9,3,0], 
    [0,9,0,7,0,3,0,5,0], 
    [2,6,3,9,5,8,7,1,4] 
]

board2 = [ #creates the second board to be solved
    [5,3,0,8,0,4,0,7,6], 
    [1,0,6,0,7,9,0,4,3], 
    [0,7,0,0,3,6,0,0,5], 
    [9,2,4,0,8,0,5,6,0], 
    [3,0,8,6,9,0,4,2,7],
    [0,5,0,4,1,2,3,0,0],
    [7,4,5,0,6,0,9,0,8], 
    [8,0,1,7,0,3,6,5,2], 
    [0,6,3,9,5,0,7,0,4] 
]

board3 = [ #creates the third board to be solved
    [7,0,0,3,0,6,0,4,0], 
    [3,4,0,5,0,9,6,0,8], 
    [6,1,9,8,0,7,5,2,3], 
    [4,9,0,0,8,5,0,0,7], 
    [1,2,0,0,0,0,3,6,5],
    [0,7,6,0,3,0,8,0,0],
    [2,0,1,4,9,0,0,0,6], 
    [0,3,0,2,0,8,4,0,1], 
    [8,6,4,7,0,0,9,3,2] 
]

board4 = [ #creates the fourth board to be solved
    [7,3,2,0,8,4,6,9,1], 
    [9,1,0,3,0,0,5,2,0], 
    [8,0,0,9,0,2,7,3,4], 
    [5,4,9,0,0,0,8,6,3], 
    [1,0,0,0,3,0,2,0,7], 
    [0,2,3,0,4,8,9,1,0], 
    [3,9,0,8,5,0,4,7,2], 
    [0,7,0,4,0,3,0,0,6], 
    [4,6,8,0,7,0,0,5,9] 
]

board5 = [ #creates the fifth board to be solved
    [0,0,0,0,0,4,2,0,1], 
    [0,0,0,0,7,0,0,0,5],
    [0,0,8,1,0,5,7,0,0], 
    [0,4,1,0,3,2,8,0,0],
    [3,8,9,0,5,6,1,2,7], 
    [2,0,0,0,0,8,3,0,0], 
    [0,2,4,0,0,7,0,1,0],
    [8,3,6,0,9,0,4,0,0],
    [0,0,7,0,0,3,5,0,0] 
]

def solve(board): #creates a function solve that takes in board
    find = find_empty_space(board) #var find is set to the function find_empty_space
    if not find: #creates an if statement that checks if find is not true the following happens
        return True #returns true
    else: #if the above statement is not true, the following happens
        row, col = find #the row and col is set to find
    for i in range(1,10): #creates a for loop for i in the range of 1 through 10
        if check(board, i, (row, col)): #creates an if statement that checks for the check function
            board[row][col] = i #the boards row and coloum is set to i
            if solve(board): #creates an if statement that checks if the solve function is true
                return True #returns true
            board[row][col] = 0 #the boards row and column is set to 0
    return False #returns false


def check(board, num, pos): #creates a function check that takes in board, num, and pos
    for i in range(len(board[0])): #creates a for loop for i in the range of the length of the row of the board
        if board[pos[0]][i] == num and pos[1] != i: #creates an if statement that checks if board[pos[0]][i] is num and the pos[1] does not equal i
            return False #returns false
    for i in range(len(board)): #creates a for loop for i in the range of the length of the board
        if board[i][pos[1]] == num and pos[0] != i: #creates an if statement that checks if board[i][pos[1]] is num and the pos[0] does not equal i
            return False #returns false
    box_x = pos[1] // 3 #box_x is set to pos of 1 // 3
    box_y = pos[0] // 3 #box_y is set to pos of 0 // 3
    for i in range(box_y*3, box_y*3 + 3): #creates a for loop for i in the range of the box_y*3, box_y*3 + 3
        for j in range(box_x * 3, box_x*3 + 3): #creates a for loop for j in the range of the box_x*3, box_x*3 + 3
            if board[i][j] == num and (i,j) != pos: #creates an if statement that checks if the boards i and j is num and (i,j) doesn't equal pos
                return False #returns false
    return True #returns true


def print_board(board): #creates a function print_board that takes in board
    for i in range(len(board)): #creates a for loop for i in the range of the length of the board
        if i % 3 == 0 and i != 0: #creates an if statement that checks if i % 3 is 0 and that i doesn't equal 0
            print("- - - - - - - - - - - - ") #prints for formatting the board
        for j in range(len(board[0])): #creates a for loop for j in the range of the length of the colomn of the board
            if j % 3 == 0 and j != 0: #creates an if statement that checks if j % 3 is 0 and that j doesn't equal 0
                print(" | ", end="") #prints for formatting the board

            if j == 8: #creates an if statement that checks if j is 8
                print(board[i][j]) #prints the board
            else: #if the above statement is not true, the following happens
                print(str(board[i][j]) + " ", end="") #the following is printed


def find_empty_space(board): #creates a function find_empty_space that takes in board
    for i in range(len(board)): #creates a for loop for i in the range of the length of the board
        for j in range(len(board[0])): #creates a for loop for j in the range of the length of the colomn of the board
            if board[i][j] == 0: #creates an if statement that checks if board[i][j] is 0
                return (i, j)  #returns the row and column
    return None #returns none


print("File Name: puzzle1.txt") #prints the file name
print("Puzzle 1:") #prints the following
print_board(board1) #prints the unsolved board
print("Puzzle 1 Solved: ") #prints the following
solve(board1) #runs board1 through the solve function
if solve(board1) == False: #creates an if statement that checks if the solved board is false
    print("No solution found") #prints that there is no solution
else: #if there is a solution to the puzzle the following happens
    print_board(board1) #prints the solved board
print() #prints an empty line

print("File Name: puzzle2.txt") #prints the file name
print("Puzzle 2:") #prints the following
print_board(board2) #prints the unsolved board
print("Puzzle 2 Solved: ") #prints the following
solve(board2) #runs board2 through the solve function
if solve(board2) == False: #creates an if statement that checks if the solved board is false
    print("No solution found") #prints that there is no solution
else: #if there is a solution to the puzzle the following happens
    print_board(board2) #prints the solved board
print() #prints an empty line

print("File Name: puzzle3.txt") #prints the file name
print("Puzzle 3:") #prints the following
print_board(board3) #prints the unsolved board
print("Puzzle 3 Solved: ") #prints the following
solve(board3) #runs board3 through the solve function
if solve(board3) == False: #creates an if statement that checks if the solved board is false
    print("No solution found") #prints that there is no solution
else: #if there is a solution to the puzzle the following happens
    print_board(board3) #prints the solved board
print() #prints an empty line

print("File Name: puzzle4.txt") #prints the file name
print("Puzzle 4:") #prints the following
print_board(board4) #prints the unsolved board
print("Puzzle 4 Solved: ") #prints the following
solve(board4) #runs board4 through the solve function
if solve(board4) == False: #creates an if statement that checks if the solved board is false
    print("No solution found") #prints that there is no solution
else: #if there is a solution to the puzzle the following happens
    print_board(board4) #prints the solved board
print() #prints an empty line

print("File Name: puzzle5.txt") #prints the file name
print("Puzzle 5:") #prints the following
print_board(board5) #prints the unsolved board
print("Puzzle 5 Solved: ") #prints the following
solve(board5) #runs board5 through the solve function
if solve(board5) == False: #creates an if statement that checks if the solved board is false
    print("No solution found") #prints that there is no solution
else: #if there is a solution to the puzzle the following happens
    print_board(board5) #prints the solved board
print() #prints an empty line


