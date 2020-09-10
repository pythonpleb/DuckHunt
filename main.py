import pygame

from background import build_background, screen
from cursor import set_cursor_image
from manager import check_click, move_and_draw_ducks, populate_ducks

pygame.init()

clock = pygame.time.Clock()
running = True

# show player score on screen
score_val = 0
score_font = pygame.font.Font('duckHuntFont.TTF', 32)
textX = 1300
textY = 1000


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
                # print("hit: ", duck_id)


if __name__ == '__main__':
    populate_ducks()

    while running:
        build_background()
        move_and_draw_ducks()
        set_cursor_image()
        events()
        # killed_duck()
        show_score(textX, textY)
        pygame.display.flip()
        clock.tick(50)  # this means 20 ticks per second
    pygame.quit()
