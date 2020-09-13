# The purpose of this file is to manage the duc objects.
# Things like movement, drawing images, etc

import pygame

from background import screen
from duck_object import DuckObject

# all of our ducks are here
ducks = []  # 10
num_of_ducks = 10

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

fall_animation_frames = [pygame.image.load('falling_duck_resized.png').convert_alpha(),
                         pygame.image.load('falling_duck_resized.png').convert_alpha(),
                         pygame.image.load('falling_duck_resized.png').convert_alpha(),
                         pygame.image.load('falling_duck_resized.png').convert_alpha(),
                         pygame.image.load('falling_duck_resized_flipped.png').convert_alpha(),
                         pygame.image.load('falling_duck_resized_flipped.png').convert_alpha(),
                         pygame.image.load('falling_duck_resized_flipped.png').convert_alpha(),
                         pygame.image.load('falling_duck_resized_flipped.png').convert_alpha()
                         ]
# duck_down = pygame.image.load('falling_duck_resized.png').convert_alpha()


def show_pts_on_screen(mouse_x, mouse_y):
    score_font = pygame.font.Font('duckHuntFont.TTF', 32)
    score_num = score_font.render('1500', True, (255, 255, 255))  # cant display + sign
    text_x = mouse_x + 25
    text_y = mouse_y - 25
    screen.blit(score_num, (text_x, text_y))


# This will create a new duck and store it in the ducks array
def create_duck():
    duck = DuckObject()  # this creates a new instance (object) of the class
    duck.reset()
    ducks.append(duck)


# This will create a bunch of ducks
def populate_ducks():
    for i in range(num_of_ducks):
        create_duck()


# This function will check if a duck was clicked based on the mouse click location.
# Return True id a duck was hit
def check_click(mouse_x, mouse_y):
    for duck in ducks:
        if duck.x <= mouse_x <= duck.x + 125 and duck.y <= mouse_y <= duck.y + 125:
            # if we are here, this means duck was clicked
            duck.store_x = duck.x  # store coordinates x, y where the duck was clicked
            duck.store_y = duck.y
            duck.dead = True
            duck.dead_time = 20 * 1.5  # 20 ticks = 1 second
            return True
    return False


# Draw a duck on the screen
def draw_duck(duck):
    if duck.is_falling:
        # blit falling duck at pos where duck was clicked
        screen.blit(fall_animation_frames[duck.fall_frame_count],
                    (duck.store_x - 20, duck.store_y))  # -20 to center img. because im a retard who cant crop images properly
        duck.fall_frame_count += 1  # cycle through the frames
        if duck.fall_frame_count + 1 > 8:  # 8 is num of frames
            duck.fall_frame_count = 0  # reset back to first frame to keep the cycle goings
    if duck.dead:
        screen.blit(duck_shot, (duck.x, duck.y))
        show_pts_on_screen(duck.x, duck.y)

    else:
        screen.blit(fly_animation_frames[duck.animation_frame_count], (duck.x, duck.y))
        duck.animation_frame_count += 1  # cycle through the frames
        if duck.animation_frame_count + 1 > 12:  # 12 is num of frames
            duck.animation_frame_count = 0  # reset back to first frame to keep the cycle goings


# Move and draw all of the ducks
def move_and_draw_ducks():
    for duck in ducks:
        draw_duck(duck)

        if duck.is_falling:
            duck.store_y += duck.fall_speed
            if duck.store_y > 1080:
                duck.is_falling = False

        if not duck.dead:
            # make the duck move
            duck.x += duck.v_x
            if duck.x > 2000:
                # respawn with new random x,y coordinates and speed
                duck.reset()
        if duck.dead:
            duck.dead_time -= 1
            if duck.dead_time <= 0:
                duck.is_falling = True  # set fall animation after dead animation
                duck.reset()
