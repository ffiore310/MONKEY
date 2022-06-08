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
        self.rect.x = 30
        self.rect.y = 330
        self.speedx = 0
        self.speedy = 0
        self.last = 1

        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 70
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.speedx 
        self.rect.y += self.speedy 

        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        if elapsed_ticks >self.frame_ticks:
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
    def __init__(self, img, l, c, blocos):
        pygame.sprite.Sprite.__init__(self)
        self.l = l
        self.c = c
        self.blocos = blocos
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = l * BLOCO_LARGURA
        self.rect.y = c * BLOCO_ALTURA
        self.speedx = random.choice(lista_speed)
        if self.speedx == 0:
            self.speedy = -5
        else:
            self.speedy = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.orientacao = random.randint(0, 3)
        self.tempo = 50
    
    def update (self):
         colisoes = pygame.sprite.spritecollide(self, self.blocos, False)
         self.rect.y += self.speedy
         for colisao in colisoes:
            if self.speedy > 0:
                self.rect.bottom = colisao.rect.top
                self.speedy = random.choice(lista_speed)
                if self.speedy == 0:
                    self.speedx = -5
                else:
                    self.speedx = 0
            elif self.speedy < 0:
                self.rect.top = colisao.rect.bottom
                self.speedy = random.choice(lista_speed)
                if self.speedy == 0:
                    self.speedx = -5
                else:
                    self.speedx = 0

         self.rect.x += self.speedx
         colisoes = pygame.sprite.spritecollide(self, self.blocos, False)
         for colisao in colisoes:
            if self.speedx > 0:
                self.rect.right = colisao.rect.left
                self.speedx = random.choice(lista_speed)
                if self.speedx == 0:
                    self.speedy = -5
                else:
                    self.speedy = 0
            elif self.speedx < 0:
                self.rect.left = colisao.rect.right
                self.speedx = random.choice(lista_speed)
                if self.speedx == 0:
                    self.speedy = -5
                else:
                    self.speedy = 0
         
        #colisoes = pygame.sprite.spritecollide(self, self.blocos, False)
        #if len(colisoes) > 0 or self.tempo == 0:
        #    o = self.orientacao
        #    self.orientacao = random.randint(1, 3)
        #    while o == self.orientacao:
        #        self.orientacao = random.randint(1, 3)
        #    self.tempo = 50
        #if self.orientacao == 0:
        #    self.speedx = 0
        #    self.speedy = 5
        #if self.orientacao == 1:
        #    self.speedx = -5
        #    self.speedy = 0
        #if self.orientacao == 2:
        #    self.speedx = 0
        #    self.speedy = -5
        #if self.orientacao == 3:
        #    self.speedx = 5
        #    self.speedy = 0
        #self.rect.y += self.speedy
        #self.rect.x += self.speedx
        #self.tempo -= 1


class Comidinha(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x * COMIDINHA_WIDTH
        self.rect.y = y * COMIDINHA_HEIGHT
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        pass

class Comida (pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x * COMIDA_WIDTH
        self.rect.y = y * COMIDA_HEIGHT
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        pass

class Explosion(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, list_img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.explosion_anim = list_img

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 70

    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_anim):
                self.kill()
                player.rect.x = 0
                player.rect.y = 330
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    class Fantasma_inicial(pygame.sprite.Sprite):
        def __init__(self, img, l, c, porta):
            self.image = img
            self.l = l
            self.c = c
            self.rect.x = l * BLOCO_LARGURA
            self.rect.y = c * BLOCO_ALTURA
            self.speedx = 0
            self.speedy = 0
            self.porta = porta
        def update():
            pass

    
    