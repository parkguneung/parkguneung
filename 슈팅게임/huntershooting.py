import pygame
import random
from time import sleep

WHITE = (255,255,255)
pad_width=1024
pad_height=512
background_width=1024
rion_width=110
hunter_width=90
hunter_height=55

def drawObject(obj,x,y):
        global gamepad
        gamepad.blit(obj,(x,y))

        



def runGame():
	global gamepad,hunter,clock,background1,background2
	global rion,fires,bullet

	bullet_xy=[]

	
	x=pad_width*0.05
	y=pad_width*0.8
	y_change=0

	background1_x=0
	background2_x=background_width

	rion_x=pad_width
	rion_y=random.randrange(0,pad_height)

	fire_x=pad_width
	fire_y=random.randrange(0,pad_height)
	random.shuffle(fires)
	fire=fires[0]


	crashed=False
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed=True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					y_change = -5
				elif event.key == pygame.K_DOWN:
					y_change = 5
				elif event.key == pygame.K_LCTRL:
                                        bullet_x = x+hunter_width
                                        bullet_y = y+hunter_height/2
                                        bullet_xy.append([bullet_x,bullet_y])
                                elif event.key == pygame.K_SPACE:
                                        sleep(5)
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0
		y += y_change

		#Clear gamepad
		gamepad.fill(WHITE)

		#Draw Background

		background1_x-=2
		background2_x-=2
		#rion
		rion_x-=7
		if rion_x<=0:
			rion_x=pad_width
			rion_y=random.randrange(0,pad_height)
		#fire
		if fire == None:
			fire_x -=30
		else:
			fire_x -=15
		if fire_x <=0:
			fire_x=pad_width
			fire_y=random.randrange(0,pad_height)
			random.shuffle(fires)
			fire=fires[0]
		#bullet
		if len(bullet_xy)!=0:
                        for i,bxy in enumerate(bullet_xy):
                                bxy[0]+=15
                                bullet_xy[i][0]=bxy[0]
                                if bxy[0]>=pad_width:
                                        bullet_xy.remove(bxy)
		if background1_x == -background_width:
			background1_x=background_width
		if background2_x == -background_width:
			background2_x=background_width
		drawObject(background1,background1_x,0)
		drawObject(background2,background2_x,0)
		drawObject(rion,rion_x,rion_y)
		if fire != None:
			drawObject(fire,fire_x,fire_y)
		if len(bullet_xy)!=0:
                        for bx,by in bullet_xy:
                                drawObject(bullet,bx,by)
		drawObject(hunter,x,y)
		pygame.display.update()
		clock.tick(60)
	pygame.quit()
	quit()

	
def initGame():
	global gamepad,hunter,clock,background1,background2
	global rion,fires

	fires=[]
	
	pygame.init()
	gamepad=pygame.display.set_mode((pad_width,pad_height))
	pygame.display.set_caption('huntershooting')
	hunter=pygame.image.load('사냥꾼.png')
	background1=pygame.image.load('밀림.png')
	background2=background1.copy()
	rion=pygame.image.load('사자.png')
	fires.append(pygame.image.load('fireball.png'))
	fires.append(pygame.image.load('fireball2.png'))

	bullet=pygame.image.load('bullet.png')


	
                     
	clock=pygame.time.Clock()
	runGame()

	
 	
if __name__ == '__main__':
	initGame()

	

