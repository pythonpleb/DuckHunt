import random

import pygame

from background import screen

duck_frame = pygame.image.load('frame1.png').convert()
duck_frame = pygame.transform.scale(duck_frame, (125, 125))

# Ducks
duckImg = []
duckX = []
duckY = []
duckX_change = []
duckY_change = []
num_of_ducks = 10

for i in range(num_of_ducks):
    duckX.append(random.randint(-1000, -100))  # random x coordinate
    duckY.append(random.randint(0, 500))  # random y coordinate
    duckX_change.append(random.randint(2, 9))  # random duck speed
    duckY_change.append(40)


def ducks(x, y):
    screen.blit(duck_frame, (x, y))


def reset_duck(i):
    duckX[i] = random.randint(-1000, -100)
    duckY[i] = random.randint(0, 500)
    duckX_change[i] = random.randint(2, 9)


def draw_duck():
    for i in range(num_of_ducks):
        # make the ducks move
        duckX[i] += duckX_change[i]
        ducks(duckX[i], duckY[i])
        if duckX[i] > 2000:
            # respawn with new random x,y coordinates and speed
            reset_duck(i)


def check_click(pos):
    """
    Check if the click event was on one of the ducks.
    Loop for all the ducks and find the one which has the click event coordinates
    inside its hitbox.
    Returns the duck id or -1 if no duck was clicked
    """
    x, y = pos
    for i in range(num_of_ducks):
        if duckX[i] <= x <= duckX[i] + 125 and duckY[i] <= y <= duckY[i] + 125:
            return i

    return -1
