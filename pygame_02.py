import pygame
from pygame.locals import *
import sys

white=255,255,255
blue=0,0,255
pygame.init()
screen=pygame.display.set_mode((500,400))
myfont=pygame.font.Font(None,50)
textImage=myfont.render("hello pygame",True,white)
space=pygame.image.load('pygame_02.png').convert()
planet=pygame.image.load('pygame_12.png').convert_alpha()
width,height=planet.get_size()
snow=pygame.image.load('pygame_05.png').convert_alpha()
w_snow,h_snow=snow.get_size()
snow=pygame.transform.scale(snow,(w_snow*2,h_snow*2))
#snow=pygame.transform.smoothscale(snow,(w_snow*2,h_snow*2))#平滑放大、缩小
snow_x=50
snow_y=50

sound=pygame.mixer.Sound("Alarm01.wav")


while(True):
	for event in pygame.event.get():
		#if event.type in (QUIT,KEYDOWN):
		#	sys.exit()
		if event.type==MOUSEMOTION:
			snow_x,snow_y=event.pos
		elif event.type==MOUSEBUTTONDOWN:
			snow_x,snow_y=event.pos
	screen.fill(blue)
	screen.blit(space,(0,0))
	screen.blit(planet,(250-width/2,200-height/2))#窗口居中放置
	#screen.blit(planet,(250,200))
	screen.blit(textImage,(100,100))
	
	#-----------移动雪花snow
	#for event in pygame.event.get():
		#if event.type==pygame.MOUSEBUTTONUP:
	#if pygame.event.get()=='MOUSEMOTION':
	#if event.type in (K_RIGHT,KEYDOWN):
	if snow_x>400:
		snow_x=50
	else:
		snow_x=snow_x+0.01
	if snow_y>400:
		snow_y=50
	else:
		snow_y=snow_y+0.01
	screen.blit(snow,(snow_x,snow_y))
	

	#-----------移动雪花snow
	pygame.draw.circle(screen,blue,(300,250),100,10)
	pygame.draw.rect(screen,blue,(100,200,230,300),1)
	pygame.draw.rect(screen,blue,(10,20,100,300),1)
	pygame.draw.line(screen,blue,(100,100),(500,400),2)
	pygame.draw.arc(screen,blue,(100,200,200,300),60,90,3)

	pygame.display.update()	

	keys=pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		sys.exit()
	
	elif keys[K_UP] or keys[K_DOWN] or keys[K_LEFT]:
		snow_x=250
		snow_y=200
		sound.play()

	#pygame.display.flip()#整个窗口的更新
	
	
	
  
    