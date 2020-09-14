import pygame
from duck_object import DuckObject
from background import screen, width, height

strike = pygame.image.load('strike.png').convert_alpha()
strike = pygame.transform.scale(strike, (60, 92))

d = DuckObject  # access the duck obj


def draw_strike():
    if d.strike == 1:
        screen.blit(strike, (50, 980))
    if d.strike == 2:
        screen.blit(strike, (50, 980))
        screen.blit(strike, (125, 980))
    if d.strike == 3:
        screen.blit(strike, (50, 980))
        screen.blit(strike, (125, 980))
        screen.blit(strike, (200, 980))


def game_over_text():
    if d.strike == 3:
        gg = pygame.font.Font('duckHuntFont.TTF', 72).render("GAME OVER", True, (0, 0, 0))
        gg_rect = gg.get_rect(center=(width / 2, height / 2))  # center the text in the middle of screen
        screen.blit(gg, gg_rect)
