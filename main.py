import pygame
from background import build_background, screen
from cursor import set_cursor_image
from duck import draw_duck, check_click, reset_duck, killed_duck, is_shot

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
            duck_id = check_click(event.pos)
            if duck_id >= 0:
                is_shot()

                reset_duck(duck_id)  # send the duck back if it was clicked
                score_val += 1500
                # print("hit: ", duck_id)


if __name__ == '__main__':

    while running:
        build_background()
        draw_duck()
        set_cursor_image()
        events()
        #killed_duck()
        show_score(textX, textY)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
