import pygame
import random
from mapa import MAPA

class Bloco(pygame.sprite.Sprite):
    def __init__(self,img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass
class Pacman(pygame.sprite.Sprite):

    def __init__(self,lista_img): #lista_img -> lista de imagens do pacman (abrindo e fechando a boca)

        pygame.sprite.Sprite.__init__(self)

        self.index_image = 0 #seria a lista 
        self.lista_img = lista_img
        self.image = self.lista_img[self.index_image]
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 250
        self.speedx = 0
        self.speedy = 0

    def update(self):

        self.rect.x += self.speedx 
        self.rect.y += self.speedy
        self.index_image = (self.index_image + 1) % len(self.lista_img)
        self.image = self.lista_img[self.index_image]

class Pacman02 (pygame.sprite.Sprite):

    def __init__(self, lista_img):
        self.e = 0
        self.image = lista_img[self.e]
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 250
        self.speedx = 0
        self.speedy = 0
        self.last = 1
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 50

    def update(self, lista_img):
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
                self.image = lista_img[0]
            else:
                self.image = lista_img[1]

        if self.speedx < 0:
            self.last = 2
            self.e = (self.e -1 )* (-1)
            if self.e == 0:
                self.image = lista_img[0]
            else:
                self.image = lista_img[2]

        if self.speedy > 0:
            self.last = 4
            self.e = (self.e -1 )* (-1)
            if self.e == 0:
                self.image = lista_img[0]
            else:
                self.image = lista_img[4]

        if self.speedy < 0:
            self.last = 3
            self.e = (self.e -1 )* (-1)
            if self.e == 0:
                self.image = lista_img[0]
            else:
                self.image = lista_img[3]

        if self.speedy == 0 and self.speedx == 0:
            self.e = (self.e -1 )* (-1)
            if self.e == 0:
                self.image = lista_img[0]
            else:
                self.image = lista_img[self.last]


class Fantasma(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0
    
    def posicao (self, x, y):
        lugar = MAPA[x][y]
        if MAPA[x-1][y] != 0:
            self.speedy = 3
        elif MAPA[x][y-1] != 0:
            self.speedx = -3
        elif MAPA[x+1][y] != 0:
            self.speedx = -3
        elif MAPA[x][y+1] != 0:
            self.speedy = 3

    def update(self):
       if self.rect.x + 1 == 0 or self.rect.x - 1:
           self.speedy = random.randint(-3, 3)
    