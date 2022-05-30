from mapa import MAPA
import pygame
from classes import Bloco

pygame.init()

BLOCO_ALTURA = 20
BLOCO_LARGURA = 20

ALTURA = len(MAPA[0]) * 20
LARGURA = len(MAPA) * BLOCO_LARGURA

window = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption('PAC-MAN')

img_bloco = pygame.image.load('assets/img/bloco_jogo_pacman.jpg').convert()
img_bloco = pygame.transform.scale(img_bloco, (20,20))
mapa_com_blocos = pygame.sprite.Group()


for l in range(len(MAPA)):
    for c in range(len(MAPA[l])):
        if MAPA[l][c] == 0:
            bloco = Bloco(img_bloco, c * 20, l * 20)
            mapa_com_blocos.add(bloco)
game= True


while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    mapa_com_blocos.update()
    window.fill((0,0,0))

    mapa_com_blocos.draw(window)
    pygame.display.update()

