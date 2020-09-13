import pygame

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
grass = pygame.image.load('grass.png').convert_alpha()

tree = pygame.image.load('tree.png').convert_alpha()
tree = pygame.transform.scale(tree, (2900, 634))

bush = pygame.image.load('bush.png').convert_alpha()
bush = pygame.transform.scale(bush, (2900, 634))

dirt = pygame.image.load('dirt.png').convert_alpha()

sky = pygame.image.load('sky.png').convert_alpha()


def grass_builder():
    screen.blit(grass, (0, 650))
    screen.blit(grass, (1050, 650))


def dirt_builder():
    screen.blit(dirt, (0, 960))
    screen.blit(dirt, (750, 960))


def nature_builder():
    screen.blit(tree, (0, 450))
    screen.blit(bush, (-750, 420))


def sky_builder():
    screen.blit(sky, (0, 0))


def build_background():
    screen.fill((79, 168, 253))
    sky_builder()
    nature_builder()
