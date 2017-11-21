import random

from pico2d import *

class Ball:

    image = None;

    def __init__(self):
        self.x, self.y = random.randint(250, 700),25
        if Ball.image == None:
            Ball.image = load_image('펭귄1단계.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10


