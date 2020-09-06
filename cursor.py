import pygame
from background import screen


def get_cursor_pos():
    x, y = pygame.mouse.get_pos()
    # print(x, y)
    return x - 50, y - 49  # return half of crosshair image size to put the crosshair in the center


def set_cursor_image():
    cursor = pygame.image.load('crosshair.png')
    cursor = pygame.transform.scale(cursor, (100, 98))  # set the image size
    screen.blit(cursor, get_cursor_pos())
    # make mouse invisible
    pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
