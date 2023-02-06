import pygame
import time

pygame.init()
width  = 400
height = 400
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))
surf1 = pygame.Surface((width,height))
surf1.set_alpha(255)

exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.draw.lines(surf1,(0, 255, 0), 1, [(0, 0), (56, 0), (56, 56), (0, 56)], width = 2)
    screen.blit(surf1, (48, 48))
    pygame.display.update()
    pygame.draw.lines(surf1,(255, 0, 0), 1, [(0, 0), (56, 0), (56, 56), (0, 56)], width = 2)
    screen.blit(surf1, (48, 48))
    pygame.display.update()
pygame.quit()