import pygame
pygame.init()
import random
from pygame.locals import * 
import time
WIDTH=900
HEIGHT=700
screen=pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Recycle")

def changebackground(img):
    bg=pygame.image.load(""+img)
    bg1=pygame.transform.scale(bg,(WIDTH,HEIGHT))
    screen.blit(bg1,(0,0))


class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bin.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

class Recycle(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(""+img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()

class Non_Recycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("plasticbag.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
images=["C:\\Users\\Hp\\Desktop\\Pro Game Development\\bag.png","C:\\Users\\Hp\\Desktop\\Pro Game Development\\item1.png","C:\\Users\\Hp\\Desktop\\Pro Game Development\\item2.png"]
itemlist=pygame.sprite.Group()
allsprites=pygame.sprite.Group()
plasticlist=pygame.sprite.Group()
for i in range(50):
    item=Recycle(random.choice(images))
    item.rect.x=random.randrange(WIDTH)
    item.rect.y=random.randrange(HEIGHT)
    itemlist.add(item)
    allsprites.add(item)
for i in range(20):
    plastic=Non_Recycle()
    plastic.rect.x=random.randrange(WIDTH)
    plastic.rect.y=random.randrange(HEIGHT)
    plasticlist.add(plastic)
    allsprites.add(plastic)

bin=Bin()
allsprites.add(bin)

run= True
score=0
clock=pygame.time.Clock()
starttime=time.time()
font=pygame.font.SysFont("Arial",20)
text=font.render("score="+str(score),True,"blue")
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    timelapse=time.time()-starttime
    if timelapse>=60:
        if score>=50:
            text=font.render("loot successful",True,"red")
            changebackground("gameover.jpg")
        else:
            text=font.render("loot unsuccessful",True,"red")
            changebackground("youlose.jpg")
        screen.blit(text,(250,40))
    else:
        changebackground("background.png")
        countdown=font.render("timeleft: "+str(60-int(timelapse)),True,"black")
        screen.blit(countdown,(20,10))
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if bin.rect.y>0:
                bin.rect.y-=5
        if keys[pygame.K_s]:
            if bin.rect.y<630:
                bin.rect.y+=5
        if keys[pygame.K_a]:
            if bin.rect.x>0:
                bin.rect.x-=5
        if keys[pygame.K_d]:
            if bin.rect.x<850:
                bin.rect.x+=5
        itemhitlist=pygame.sprite.spritecollide(bin,itemlist,True)
        plastichitlist=pygame.sprite.spritecollide(bin,plasticlist,True)
        for i in itemhitlist:
            score+=1
            text=font.render("score="+str(score),True,"blue")
        for i in plastichitlist:
            score-=1
            text=font.render("score="+str(score),True,"blue")
        screen.blit(text,(20,50))
        allsprites.draw(screen)
    pygame.display.update()