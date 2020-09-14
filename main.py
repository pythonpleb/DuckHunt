import pygame

from background import grass_builder, dirt_builder, build_background, screen
from cursor import set_cursor_image
from manager import check_click, move_and_draw_ducks, populate_ducks
from gg import draw_strike, game_over_text
from duck_object import DuckObject

pygame.init()

clock = pygame.time.Clock()
running = True

# show player score on screen
score_val = 0
score_font = pygame.font.Font('duckHuntFont.TTF', 32)
textX = 1300
textY = 1000

d = DuckObject


def show_score(x, y):
    score_num = score_font.render("SCORE: " + str(score_val), True, (255, 255, 255))
    screen.blit(score_num, (x, y))


def events():
    global running
    global score_val
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(event.pos[0], event.pos[1]):
                score_val += 1500


if __name__ == '__main__':
    populate_ducks()

    while running:
        events()
        if d.strike == 3:
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)  # if player has 3 strikes they can't click anymore
        build_background()
        move_and_draw_ducks()
        grass_builder()
        dirt_builder()
        draw_strike()
        show_score(textX, textY)
        set_cursor_image()
        game_over_text()
        pygame.display.flip()
        clock.tick(50)  # this means 20 ticks per second
    pygame.quit()
