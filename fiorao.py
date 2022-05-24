import pygame
import random 


lista_fantasmas = []
listas_cores = ['amarelo', 'azul', 'rosa', 'vermelho']
imagem_fantasma = random.choice(lista_fantasmas)
class Fantasma(pygame.sprite.Sprite):
    def __init__(self, img, cor):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 30
        self.cor = cor
        