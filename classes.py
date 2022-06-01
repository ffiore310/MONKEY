import pygame
import random
from mapa import MAPA
from config import *

class Bloco(pygame.sprite.Sprite):
    def __init__(self,img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x * BLOCO_LARGURA
        self.rect.y = y * BLOCO_ALTURA

    def update(self):
        pass
    
class Pacman02 (pygame.sprite.Sprite):

    def __init__(self, lista_img):
        pygame.sprite.Sprite.__init__(self)
        self.e = 0
        self.lista_img = lista_img
        self.image = lista_img[self.e]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 330
        self.speedx = 0
        self.speedy = 0
        self.last = 1
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 50

    def update(self):
        self.rect.x += self.speedx 
        self.rect.y += self.speedy

        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
        
        if self.speedx > 0:
            self.last = 1
            self.e = (self.e -1 )* (-1)
            if self.e == 0:
                self.image = self.lista_img[0]
            else:
                self.image = self.lista_img[1]

        if self.speedx < 0:
            self.last = 2
            self.e = (self.e -1 )* (-1)
            if self.e == 0:
                self.image = self.lista_img[0]
            else:
                self.image = self.lista_img[2]

        if self.speedy > 0:
            self.last = 4
            self.e = (self.e -1 )* (-1)
            if self.e == 0:
                self.image = self.lista_img[0]
            else:
                self.image = self.lista_img[4]

        if self.speedy < 0:
            self.last = 3
            self.e = (self.e -1 )* (-1)
            if self.e == 0:
                self.image = self.lista_img[0]
            else:
                self.image = self.lista_img[3]

        if self.speedy == 0 and self.speedx == 0:
            self.e = (self.e -1 )* (-1)
            if self.e == 0:
                self.image = self.lista_img[0]
            else:
                self.image = self.lista_img[self.last]


class Fantasma(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        pygame.sprite.Sprite.__init__(self)
        self.l = l
        self.c = c
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = l * BLOCO_LARGURA
        self.rect.y = c * BLOCO_ALTURA
        self.speedx = 0
        self.speedy = 0
    
    def update (self):
        lugar = MAPA[self.l][self.c]
        if MAPA[self.l-1][self.c] != 0:
            self.speedy = 3
        elif MAPA[self.l][self.c-1] != 0:
            self.speedx = -3
        elif MAPA[self.l+1][self.c] != 0:
            self.speedx = -3
        elif MAPA[self.l][self.c+1] != 0:
            self.speedy = 3
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Comidinha(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x * COMIDINHA_WIDTH
        self.rect.y = y * COMIDINHA_HEIGHT
    def update(self):
        pass

class Comida (pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x * COMIDA_WIDTH
        self.rect.y = y * COMIDA_HEIGHT
    def update(self):
        pass


    
    