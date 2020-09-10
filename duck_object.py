import random


class DuckObject:
    x = 0  # position x
    y = 0  # position y
    v_x = 0  # velocity x or the change in x position
    v_y = 0  # velocity y or the change in y position
    dead = False
    dead_time = 0   # count how long the duck was dead for
    animation_frame_count = 0

    def reset(self):
        self.x = random.randint(-1000, -100)
        self.y = random.randint(0, 500)
        self.v_x = random.randint(2, 9)
        self.animation_frame_count = 0
        self.dead = False
