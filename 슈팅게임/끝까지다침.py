
import pygame
import random
from time import sleep
WHITE = (255,255,255)
pad_width=1024
RED=(255,0,0)
pad_height=512
background_width=1024
hunter_width=90
hunter_height=55
rion_width=110
rion_height=67

fireball1_width=140
fireball1_height=60
fireball2_height=60
fireball2_width=86
#---------------------

def drawScore(count):
	global gamepad
	font = pygame.font.SysFont(None,25)
	text = font.render('놓친 사자수: ' +str(count),True,WHITE)
	gamepad.blit(text,(0,0))

	
def gameOver():
	global gamepad
	dispMessage('GAME OVER')

	
#-------------------------
def textObj(text,font):
	textSurface=font.render(text,True,RED)
	return textSurface,textSurface.get_rect()

def dispMessage(text):
	global gamepad
	largeText=pygame.font.Font('freesansbold.ttf',115)
	TextSurf,TextRect=textObj(text,largeText)
	TextRect.center=((pad_width/2),(pad_height/2))
	gamepad.blit(TextSurf,TextRect)
	pygame.display.update()
	sleep(2)
	runGame()

	
def crash():
	global gamepad
	dispMessage('Crashed!')

	
def drawObject(obj,x,y):
	global gamepad
	gamepad.blit(obj,(x,y))

	


def runGame():
	global gamepad,hunter,clock,background1,background2
	global rion,fires,bullet,boom
	isShotRion=False
	boom_count=0
	rion_passed=0
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
					bullet_x=x+hunter_width
					bullet_y=y+huter_height/2
					bullet_xy.append([bullet_x,bullet_y])
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:y_change =0
		gamepad.fill(WHITE)
		#draw background
		background1_x -=2
		background2_x -=2
		if background1_x == -background_width:
			background1_x = background_width
		if background2_x == -background_width:
			background2_x = background_width
		drawObject(background1,background1_x,0)
		drawObject(background2,background2_x,0)
		#score
		drawScore(rion_passed)
		#check rion pass
		if rion_passed>2:
			gameOver()
		#hunter
		y += y_change
		if y<0:
			y=0
		elif y>pad_height-hunter_height:
			y=pad_height-hunter_height
		#rion
		rion_x -=7
		if rion_x<=0:
			rion_passed += 1
			rion_x=pad_width
			rion_y=random.randrange(0,pad_height)
		#fireball
		if fire[1] == None:
			fire_x -=30
		else:
			fire_x -=15
		if fire_x <= 0:
			fire_x = pad_width
			fire_y = random.randrange(0,pad_height)
			random.shuffle(fires)
			fire=fires[0]
		#bullet
		if len(bullet_xy)!=0:
			for i,bxy in enumerate(bullte_xy):
				bxy[0] +=15
				bullet_xy[i][0]=bxy[0]
				#bullet strike rion
				if bxy[0]>rion_x:
					if bxy[1]>rion_y and bxy[1]<rion_y+rion_height:
						bullet_xy.remove(bxy)
						isShotRion=True
					if bxy[0]>=pad_width:
						try:
							bullet_xy.remove(bxy)
						except:
							pass
		#hunter crash rion
		if x+hunter_width>rion_x:
			if(y>rion_y and y<rion_y+rion_height)or(y+hunter_height>rion_y and y+hunter_height<rion_y+rion_height):
				crash()
		#hunter crash fireball
		if fire[1] != None:
			if fire[0] == 0:
				fireball_width = fireball1_width
				fireball_height = fireball1_height
			elif fire[0] == 1:
				fireball_width = fireball2_width
				fireball_height = fireball2_height
			if x+hunter_width>fire_x:
				if(y>fire_y and y<fire_y+fireball_height)or(y+hunter_height>fire_y and y+hunter_height<fire_y+fireball_height):
					crash()
		drawObject(hunter,x,y)
		if len(bullet_xy)!=0:
			for bx,by in bullet_xy:
				drawObject(bullet,bx,by)
		if not isShotRion:
			drawObject(rion,rion_x,rion,y)
		else:
			drawObject(boom,rion_x,rion_y)
			boom_count +=1
			if boom_count>5:
				boom_count=0
				rion_x=pad_width
				rion_y=random.randrange(0,pad_height-rion_height)
				isShotRion=False
		if fire[1] != None:
			drawObject(fire[1],fire_x,fire_y)
		pygame.display.update()
		clock.tick(60)
	pygame.quit()
	quit()

	
def initGame():
	global gamepad,hunter,clock,background1,background2
	global rion,fires,bullet,boom

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
	boom=pygame.image.load('boom.png')
	for i in range(3):
		fires.append((i+2,None))

	bullet=pygame.image.load('bullet.png')
	clock=pygame.time.Clock()
	runGame()

	
if __name__ == '__main__':
	initGame()

