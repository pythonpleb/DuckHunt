import pygame

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
grass = pygame.image.load('grass.png')

tree = pygame.image.load('tree.png')
tree = pygame.transform.scale(tree, (2900, 634))

bush = pygame.image.load('bush.png')
bush = pygame.transform.scale(bush, (2900, 634))

dirt = pygame.image.load('dirt.png')


def grass_builder():
    screen.blit(grass, (0, 650))
    screen.blit(grass, (1050, 650))


def dirt_builder():
    screen.blit(dirt, (0, 960))
    screen.blit(dirt, (750, 960))


def nature_builder():
    screen.blit(tree, (0, 450))
    screen.blit(bush, (-750, 420))


def build_background():
    screen.fill((79, 168, 253))
    nature_builder()
    grass_builder()
    dirt_builder()


