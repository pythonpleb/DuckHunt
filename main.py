import pygame

from background import build_background
from cursor import set_cursor_image
from duck import draw_duck, check_click, reset_duck

pygame.init()

clock = pygame.time.Clock()
running = True


def events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONUP:
            duck_id = check_click(event.pos)
            if duck_id >= 0:
                reset_duck(duck_id)
                print("hit: ", duck_id)


if __name__ == '__main__':
    while running:
        build_background()
        draw_duck()
        set_cursor_image()
        events()
        pygame.display.update()
        clock.tick(300)
    pygame.quit()
