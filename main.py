
import pygame
import random

pygame.init()

#-------------------- GERAR TELA PRINCIL--------------

ALTURA = 825
LARGURA = 750

window = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption('PAC-MAN')

#----------------------INICIA ASSETS-----------------

background = pygame.image.load('img_mapa.jpeg').convert()
background = pygame.transform.scale(background, (ALTURA,LARGURA))
#================ LOOP PRINCIPAL ================
game= True

while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

#-------------------- GERAR SAIDAS-----------

    window.fill((0,0,0))
    window.blit(background, (0,0))

    pygame.display.update()

#------------------FINALIZACAO-----------------------























pygame.quit()