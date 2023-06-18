import pygame
from pygame.locals import *
import sys

white=255,255,255
blue=0,0,255
pygame.init()
screen=pygame.display.set_mode((500,400))
myfont=pygame.font.Font(None,50)
textImage=myfont.render("hello pygame",True,white)
while(True):
    for event in pygame.event.get():
            if event.type in (QUIT,KEYDOWN):
                    sys.exit()
    screen.fill(blue)
    screen.blit(textImage,(100,100))
    pygame.draw.circle(screen,white,(300,250),100,10)
    pygame.draw.rect(screen,white,(100,200,230,300),1)
    pygame.draw.rect(screen,white,(10,20,100,300),1)
    pygame.draw.line(screen,white,(100,100),(500,400),2)
    pygame.draw.arc(screen,white,(100,200,200,300),60,90,3)
    pygame.display.update()
  
    