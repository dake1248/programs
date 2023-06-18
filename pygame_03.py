import pygame
from pygame.locals import *
import sys

white=255,255,255
blue=0,0,255

pygame.init()
screen=pygame.display.set_mode((500,400))
myfont=pygame.font.Font(None,50)
FPS=80#帧率
clock=pygame.time.Clock()#每秒时钟

textImage=myfont.render("hello pygame",True,white)
space=pygame.image.load('pygame_22.png').convert()
planet=pygame.image.load('pygame_21.png').convert_alpha()
arrow=pygame.image.load('pygame_21.png').convert_alpha()
width,height=planet.get_size()
snow=pygame.image.load('pygame_20.png').convert_alpha()
w_snow,h_snow=snow.get_size()
snow=pygame.transform.scale(snow,(w_snow*2,h_snow*2))
#snow=pygame.transform.smoothscale(snow,(w_snow*2,h_snow*2))#平滑放大、缩小
snow_x=50
snow_y=50
line=200
count=0
count_arrow_y=0
count_arrow_y1=0
count_arrow_x=0
count_arrow_x1=0

sound=pygame.mixer.Sound("Alarm01.wav")


while(True):

	clock.tick(FPS)#设置帧率

	for event in pygame.event.get():
		#if event.type in (QUIT,KEYDOWN):
		#	sys.exit()
		if event.type==MOUSEMOTION:
			snow_x,snow_y=event.pos
		elif event.type==MOUSEBUTTONDOWN:
			snow_x,snow_y=event.pos
	screen.fill(blue)
	screen.blit(space,(0,0))
	#screen.blit(planet,(250-width/2,200-height/2))#窗口居中放置
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
	#screen.blit(snow,(snow_x,snow_y))
	#-----------移动雪花snow

	count+=1
	if count>2000:
		count=0
	#pygame.draw.circle(screen,blue,(snow_x+10,snow_y+10),100,2)
	#pygame.draw.rect(screen,blue,(100,200,snow_x,snow_y),1)
	pygame.draw.rect(screen,blue,(10,20,100,300),1)
	#pygame.draw.circle(screen,blue,(+10,snow_y+10),100,2)
	for i in range(10,30):
		pygame.draw.line(screen,blue,(1+i*40+20,1+count),(1+i*40+20,1+count+line),2)

	pygame.draw.arc(screen,blue,(100,200,200,300),60,90,3)

	

	keys=pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		sys.exit()
	
	elif keys[K_SPACE]:# or keys[K_LEFT]:
		snow_x=250
		snow_y=200
		sound.play()
	elif keys[K_UP]:
		count_arrow_y+=1
		if count_arrow_y>400:
			count_arrow_y=0
	elif keys[K_DOWN]:
		count_arrow_y-=1
		if count_arrow_y>400:
			count_arrow_y=0
	elif keys[K_LEFT]:
		count_arrow_x+=1
		if count_arrow_x>250:
			count_arrow_x=0
	elif keys[K_RIGHT]:
		count_arrow_x-=1
		if count_arrow_x>250:
			count_arrow_x=0


	screen.blit(arrow,(250-count_arrow_x,400-count_arrow_y))
	#pygame.display.flip()#整个窗口的更新
	
	pygame.display.update()	
	
	
  
    