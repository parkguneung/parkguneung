import game_framework
import scroll_state


from pico2d import*

name = "Fight1State"

image=None

def enter():
    global image
    global penguin
    image = load_image('전투씬1.png')
    penguin = load_image('펭귄1단계.png')
def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
               game_framework.change_state(scroll_state)
def draw():
    clear_canvas()
    image.draw(400,300)
    penguin.draw(100,100)
    update_canvas()
    
def update(): pass
