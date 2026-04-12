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
    bg=pygame.image.load("/"+img)
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
        self.image=pygame.image.load("/"+img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()

class Non_Recycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("plasticbag.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
images=["bag.png","item1.png","item2.pmg"]