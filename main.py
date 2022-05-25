import pygame
import random
from mapa import MAPA
from fiorao import Bloco, Fantasma

pygame.init()

#-------------------- GERAR TELA PRINCIPAL--------------

BLOCO_ALTURA = 20
BLOCO_LARGURA = 20

lista_posicoes_disponiveis = []
lista_fantasmas = ['assets/img/fantasma azul .png', 'assets/img/fantasma laranja.png', 'assets/img/fantasma rosa 11.30.35.png', 'assets/img/fantasma vermelho .png']
lista_fantasmas_melhorados = []
ALTURA = len(MAPA[0]) * 20
LARGURA = len(MAPA) * BLOCO_LARGURA

window = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption('PAC-MAN')

#----------------------INICIA ASSETS-----------------

background = pygame.image.load('assets/img/img_mapa.jpeg').convert()
background = pygame.transform.scale(background, (ALTURA,LARGURA))

for fantasmas in lista_fantasmas:
    img_fantasma = pygame.image.load(fantasmas).convert()
    img_fantasma = pygame.transform.scale(img_fantasma, (30,30))
    lista_fantasmas_melhorados.append(img_fantasma)
img_bloco = pygame.image.load('assets/img/bloco jogo pacman.jpg').convert()
img_bloco = pygame.transform.scale(img_bloco, (20,20))
all_blocos = pygame.sprite.Group()
all_fantasmas = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
for l in range(len(MAPA)):
    for c in range(len(MAPA[l])):
        if MAPA[l][c] == '0':
            bloco = Bloco(img_bloco, c * 20, l * 20)
            all_blocos.add(bloco)
            all_sprites.add(bloco)


#================ LOOP PRINCIPAL ================
game= True


while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    if len(all_fantasmas) < 4:
        posicao_x = random.randint(0, LARGURA)
        posicao_y = random.randint(0, ALTURA)
        for fantasmas in lista_fantasmas_melhorados:
            fantasma = Fantasma(fantasmas, posicao_x, posicao_y)
            all_fantasmas.add(fantasma)
            all_sprites.add(fantasma)

#-------------------- GERAR SAIDAS-----------

    all_sprites.update()

    window.fill((0,0,0))
    #window.blit(background, (0,0))

    all_sprites.draw(window)

    pygame.display.update()

#------------------FINALIZACAO-----------------------























pygame.quit()