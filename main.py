from sudoku_matrix import matrix
size = 9

def check_position(positionX, positionY, value):
    column_list, row_list, square_list = [], [], [] 
    for elementX in range(positionX,positionX + 1):
        for elementY in range(size):
            column_list.append(matrix[elementX][elementY])
    
    for elementY in range(positionY, positionY + 1):
        for elementX in range(size):
            row_list.append(matrix[elementX][elementY])
        column, row = 0, 0

    if 3 <= positionX < 6:
        column = 1
    elif 6 <=  positionX < 9:
        column = 2

    if 3 <= positionY < 6:
        row = 1
    elif 6 <= positionY < 9:
        row = 2
    
    for elementX in range(3):
        for elementY in range(3):
            square_list.append(matrix[elementX + (3 * column)][elementY + (3 * row)])
            
    if str(value) not in row_list and str(value) not in column_list and str(value) not in square_list:
        return True
    else:
        return False

print(check_position(3, 3, 9))

