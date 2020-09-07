import pygame
from background import screen
import random

duck_frame = pygame.image.load('frame1.png').convert_alpha()
duck_frame = pygame.transform.scale(duck_frame, (125, 125))

duck_shot = pygame.image.load('duck_shot.png').convert_alpha()
duck_shot = pygame.transform.scale(duck_shot, (125, 125))

# Ducks
duckX = []
duckY = []
duckX_change = []
duckY_change = []
num_of_ducks = 10

for i in range(num_of_ducks):
    duckX.append(random.randint(-1000, -100))  # random x coordinate
    duckY.append(random.randint(0, 500))  # random y coordinate
    duckX_change.append(random.randint(2, 9))  # random duck speed
    duckY_change.append(0)


def ducks(x, y):
    screen.blit(duck_frame, (x, y))


def killed_duck(x, y):
    screen.blit(duck_shot, (x-63, y-63))  # draw shot duck in the middle of the cursor


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
    x, y = pos
    for i in range(num_of_ducks):
        if duckX[i] <= x <= duckX[i] + 125 and duckY[i] <= y <= duckY[i] + 125:
            return i
    return -1
