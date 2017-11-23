from pico2d import *

import game_framework
import fight1_state

from boy import FreeBoy as Boy # import Boy class from boy.py
from background import FixedBackground as Background


name = "scroll_state"

boy = None
background = None

def create_world():
    global boy, background,penguin,cat,wolf,tajo
    boy = Boy()
    background = Background()
    background.set_center_object(boy)
    boy.set_background(background)

    # fill here
    penguin=load_image('펭귄1단계.png')
    cat=load_image('길고양이2단계.png')
    wolf=load_image('늑대3단계.png')
    tajo=load_image('타조4단계.png')
def destroy_world():
    global boy, background
    del(boy)
    del(background)
def enter():
    open_canvas(800, 600)
    hide_cursor()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    global x
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
                boy.handle_event(event)
                background.handle_event(event)
               
def update(frame_time):
    boy.update(frame_time)
    background.update(frame_time)


def draw(frame_time):
    clear_canvas()
    background.draw()
    boy.draw()
    penguin.draw(250,50)
    cat.draw(400,50)
    wolf.draw(550,50)
    tajo.draw(700,50)
    update_canvas()






