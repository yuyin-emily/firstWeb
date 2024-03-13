import pygame
import datetime

import bricks
import charas

pygame.init()
pygame.display.set_caption("Mario")
screen = pygame.display.set_mode((640,360))
clock = pygame.time.Clock()
clock.tick(55)
background = pygame.image.load("./image/background.png")

running = True

brick = []
for i in range(24): #24塊地板
        brick.append(bricks.bricks(i))
        
chara = charas.charas()

while running:
    time = datetime.datetime.now().microsecond
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #print(time)
    
    chara.run(keys)    
    for i in range(5):
        screen.blit(background,[i * 160,0])
        
    for i in range(24):
        screen.blit(brick[i].img,brick[i].position)
        
    if chara.dirX == "right":
        screen.blit(chara.img[(time % 800000) // 400000],chara.position)
    else:
        screen.blit(chara.img[(time % 800000) // 400000 + 2],chara.position)
    

    pygame.display.update()

