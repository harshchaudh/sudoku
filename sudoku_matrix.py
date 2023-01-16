# 2-D array
size = 9 # treat as constant
matrix = [[0 for i in range(size)] for j in range(size)]

# grid assignment
grid = 1 # no. corresponds to grid in sudoku_puzzles.txt
GridRange_START = (10 * grid) - 9
GridRange_END = (10 * grid)

puzzle = open("sudoku_puzzles.txt", "r")
lines = puzzle.readlines()
lines = lines[GridRange_START:GridRange_END]

i = 0
j = 0
while (i != 9 and j != 9):
    for line in lines:
        line = line.replace("\n", "")
        for character in list(line):
            matrix[i][j] = character

            j += 1
        j = 0
        i +=  1

#for row in board:
#    print(row)
