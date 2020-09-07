import pygame
from background import screen
import random

fly_animation_frames = [pygame.image.load('frame1-resized.png').convert_alpha(),
                        pygame.image.load('frame1-resized.png').convert_alpha(),
                        pygame.image.load('frame1-resized.png').convert_alpha(),
                        pygame.image.load('frame2-resized.png').convert_alpha(),
                        pygame.image.load('frame2-resized.png').convert_alpha(),
                        pygame.image.load('frame2-resized.png').convert_alpha(),
                        pygame.image.load('frame3-resized.png').convert_alpha(),
                        pygame.image.load('frame3-resized.png').convert_alpha(),
                        pygame.image.load('frame3-resized.png').convert_alpha(),
                        pygame.image.load('frame4-resized.png').convert_alpha(),
                        pygame.image.load('frame4-resized.png').convert_alpha(),
                        pygame.image.load('frame4-resized.png').convert_alpha(),
                        ]

duck_shot = pygame.image.load('duck_shot.png').convert_alpha()
duck_shot = pygame.transform.scale(duck_shot, (125, 125))

# Ducks
duckX = []
duckY = []
duckX_change = []
duckY_change = []
num_of_ducks = 10

flyCount = 0

for i in range(num_of_ducks):
    duckX.append(random.randint(-1000, -100))  # random x coordinate
    duckY.append(random.randint(0, 500))  # random y coordinate
    duckX_change.append(random.randint(2, 9))  # random duck speed
    duckY_change.append(0)


def ducks(x, y):
    global flyCount
    screen.blit(fly_animation_frames[flyCount], (x, y))
    flyCount += 1  # cycle through the frames
    if flyCount + 1 > 12:  # 12 is num of frames
        flyCount = 0  # reset back to first frame to keep the cycle goings


def killed_duck(x, y):
    screen.blit(duck_shot, (x - 63, y - 63))  # draw shot duck in the middle of the cursor


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
