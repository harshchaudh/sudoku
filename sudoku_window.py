import pygame
from sudoku_matrix import matrix, grid, size

pygame.font.init()
background_colour = (255,255,255)
length = 600 # square window
myfont = pygame.font.SysFont("Ariel", 65)

screen = pygame.display.set_mode((length, length))
pygame.display.set_caption(f'Sudoku - LEVEL {grid}')
screen.fill(background_colour)

# board

L_side = 48
R_side = length - L_side
square_len = int((R_side - L_side)/size)

def outline():
  pygame.draw.lines(screen, (255, 136, 17), True, 
                  [(L_side, L_side), (R_side, L_side), (R_side, R_side), (L_side, R_side)], 
                  width = 2)

def grid():
  for line in range(1, 9):
    lines = []
    lines.append((L_side, L_side + (square_len * line)))
    lines.append((R_side, L_side + (square_len * line)))

    if (line == 3 or line == 6):
      pygame.draw.lines(screen, (157, 217, 210), False, lines, width = 2)
    else:
      pygame.draw.lines(screen, (244, 208, 111), False, lines)
  
    lines = []
    lines.append((L_side + (square_len * line), L_side))
    lines.append((L_side + (square_len * line), R_side))

    if (line == 3 or line == 6):
      pygame.draw.lines(screen, (157, 217, 210), False, lines, width = 2)
    else:
      pygame.draw.lines(screen, (244, 208, 111), False, lines)

def elements():
  cornerY = 0
  for elementY in range (0, size):
    cornerX = 0
    for elementX in range (0, size):
      value = str(matrix[elementX][elementY])
      square_center = ((L_side + (square_len * cornerX )) + int(square_len/2), 
                        (L_side + (square_len * cornerY) + int(square_len/2)))
      square_value = myfont.render(value, 1, (192, 204, 135))
      if value != "0":
        screen.blit(square_value, square_value.get_rect(center = square_center))
      else:
        matrix[elementX][elementY] = 0
      cornerX += 1
    cornerY += 1

def square_blink():
  pygame.draw.rect(selection_surface, (0, 0, 0), [0, 0, 56, 56], width = 2)

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

def square_error(positionX, positionY):
  pygame.draw.rect(error_surface, (255, 130, 130),[0, 0, 56, 56])

error_surface = pygame.Surface((504, 504))
error_surface.set_alpha(255)

selection_surface = pygame.Surface((504, 504))
selection_surface.set_alpha(255)


grid()
outline()
elements()

pygame.display.flip()
positionX, positionY = 0, 0
check_reminder = False

executing = True
while executing:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      executing = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT and (positionX < size - 1):
          positionX += 1
      if event.key == pygame.K_LEFT and (positionX > 0):
          positionX -= 1
      if event.key ==  pygame.K_UP and (positionY > 0):
          positionY -= 1
      if event.key == pygame.K_DOWN and (positionY < size - 1):
          positionY += 1
      
      print(positionX, positionY)

      if (isinstance(matrix[positionX][positionY], int) == True):
        if event.unicode.isdigit():
          if matrix[positionX][positionY] != 0:
            matrix[positionX][positionY] = 0
            screen.fill(background_colour)
            grid()
            outline()

          if event.key == pygame.K_1:
            if check_position(positionX, positionY, 1) == False:
              check_reminder = True
            matrix[positionX][positionY] = 1
          if event.key == pygame.K_2:
            if check_position(positionX, positionY, 2) == False:
              check_reminder = True
            matrix[positionX][positionY] = 2
          if event.key == pygame.K_3:
            if check_position(positionX, positionY, 3) == False:
              check_reminder = True
            matrix[positionX][positionY] = 3
          if event.key == pygame.K_4:
            if check_position(positionX, positionY, 4) == False:
              check_reminder = True
            matrix[positionX][positionY] = 4
          if event.key == pygame.K_5:
            if check_position(positionX, positionY, 5) == False:
              check_reminder = True
            matrix[positionX][positionY] = 5
          if event.key == pygame.K_6:
            if check_position(positionX, positionY, 6) == False:
              check_reminder = True
            matrix[positionX][positionY] = 6
          if event.key == pygame.K_7:
            if check_position(positionX, positionY, 7) == False:
              check_reminder = True
            matrix[positionX][positionY] = 7
          if event.key == pygame.K_8:
            if check_position(positionX, positionY, 8) == False:
              check_reminder = True
            matrix[positionX][positionY] = 8
          if event.key == pygame.K_9:
            if check_position(positionX, positionY, 9) == False:
              check_reminder = True
            matrix[positionX][positionY] = 9
      
      if check_reminder:
        square_error(positionX, positionY)
        check_reminder = False
        
      square_blink()

      screen.blit(selection_surface, ((positionX * square_len) + 48, (positionY * square_len) + 48))
      screen.blit(error_surface, ((positionX * square_len) + 48, (positionY * square_len) + 48))
      elements()

      pygame.display.update()