# 2-D array

def grid_reference(grid, size = 9):

    matrix = [[0 for i in range(size)] for j in range(size)]

    GridRange_START = (10 * grid) - 9
    GridRange_END = (10 * grid)

    puzzle = open("sudoku_puzzles.txt", "r")
    lines = puzzle.readlines()
    lines = lines[GridRange_START:GridRange_END]

    i, j = 0, 0
    while (i != size and j != size):
        for line in lines:
            line = line.replace("\n", "")
            for character in list(line):
                matrix[i][j] = character
                i += 1
            i = 0
            j +=  1
    return matrix, grid, size

values = grid_reference(1, 9)

matrix = values[0]
grid = values[1]
size = values[2]
