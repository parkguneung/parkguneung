Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> 
>>> from pico2d import*
Pico2d is prepared.
>>> class Grass:
	pass

>>> grass=Grass()
>>> class Grass:
	def __init__(self):
		self.image=load_image('C:\\Users\\박건웅\\Desktop\\2d겜프\\2d이미지\\grass.png')
	def draw(self):
		self.image.draw(400,30)


>>> class Boy:
	def __init__(self):
		self.x,self.y=random.randint(100,700),90
		self.frame=random.randint(0,7)
		self.image=load_image('C:\\Users\\박건웅\\Desktop\\2d겜프\\2d이미지\\run_animation.png')
	def update(self):
		self.frame=(self.frame+1)%8
		self.x+=5
	def draw(self):
		self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


>>> def handle_events():
	global running
	events=get_events()
	for event in events:
		if event.type==SDL_QUIT:
			running=False
		elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
			running=False
		elif event.type==SDL_MOUSEMOTION:
			x,y=event.x,600-event.y


>>>  open_canvas()
 
SyntaxError: unexpected indent
>>> open_canvas()
>>> boy=Boy()
>>> grass=Grass()
>>> team=[Boy() for i in range(1000)]
running=True;
>>> running=True;
>>> while running:
	handle_events()
	for boy in team:
		boy.update()
	clear_canvas()
	grass.draw()
	for boy in team:
		boy.draw()
	update_canvas()
	delay(0.05)

	
Traceback (most recent call last):
  File "<pyshell#15>", line 8, in <module>
    boy.draw()
  File "<pyshell#6>", line 10, in draw
    self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
  File "C:\Users\박건웅\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pico2d.py", line 233, in clip_draw
    SDL_RenderCopy(renderer, self.texture, src_rect, dest_rect)
KeyboardInterrupt
>>> close_canvas()
>>> 
