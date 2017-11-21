import fight1_state
from pico2d import*

def create_world():
	global boy,penguin
	boy=Boy()
	penguin=Penguin()

	
def collide(a,b):
	left_a,bottom_a,right_a,top_a=a.get_bb()
	left_b,bottom_b,right_b,top_b=b.get_bb()
	if left_a>right_b:return False
	if right_a<left_b:return False
	if top_a<bottom_b:return False
	if bottom_a>top_b:return False
	return True

def update(frame_time):
	boy.update(frame_time)
	penguin.update(frame_time)
	if collide(boy, penguin):game_framework.change_state(fight1_state)
		
def draw(frame_time):
        clear_canvas()
        boy.draw()
        penguin.draw()
        boy.draw_bb()
        penguin.draw_bb()
        update_canvas()
