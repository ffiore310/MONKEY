import random
from mapa import MAPA
import pygame
from classes import Bloco, Fantasma
from config import *
from acalabres_playground import Pacman02

pygame.init()

# DEFINICAO MAPA

window = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption('PAC-MAN')

img_bloco = pygame.image.load('assets/img/bloco_jogo_pacman.jpg').convert()
img_bloco = pygame.transform.scale(img_bloco, (30,30))
mapa_com_blocos = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_fantasmas = pygame.sprite.Group()


for l in range(len(MAPA)):
    for c in range(len(MAPA[l])):
        if MAPA[l][c] == 0:
            bloco = Bloco(img_bloco, c, l)
            mapa_com_blocos.add(bloco)
            all_sprites.add(bloco)

# IMAGENS PACMAN

pac_img_fechado = pygame.image.load('assets/img/pacman_fechado.png')
pac_img_fechado = pygame.transform.scale(pac_img_fechado, (30,30))
pac_img_aberto = pygame.image.load('assets/img/pacman_direita.png')
pac_img_aberto = pygame.transform.scale(pac_img_aberto, (30,30))
pac_img_aberto_esquerda = pygame.image.load('assets/img/pacman_esquerdo .png')
pac_img_aberto_esquerda = pygame.transform.scale(pac_img_aberto_esquerda, (30,30))

pac_img_aberto_cima = pygame.image.load('assets/img/pacman_cima.png')
pac_img_aberto_cima = pygame.transform.scale(pac_img_aberto_cima, (30,30))

pac_img_aberto_baixo = pygame.image.load('assets/img/pacman_baixo.png')
pac_img_aberto_baixo = pygame.transform.scale(pac_img_aberto_baixo, (30,30))

paclist_img = [pac_img_fechado, pac_img_aberto,pac_img_aberto_esquerda, pac_img_aberto_cima, pac_img_aberto_baixo]

img_fantasmas = []
for name in ['fantasma_azul.png', 'fantasma_laranja.png', 'fantasma_rosa.png', 'fantasma_vermelho.png']:
    img = pygame.image.load(f'assets/img/{name}')
    img = pygame.transform.scale(img, (30,30))
    img_fantasmas.append(img)

game= True

#ACERTANDO OS FPS
clock = pygame.time.Clock()
FPS = 10

# CRIANDO PERSONAGENS
player = Pacman02(paclist_img)
last_list = [0,0]

all_sprites.add(player)
lugar_inicial_fantasma = 13   
for fantasmas in img_fantasmas:
    f = Fantasma(fantasmas,lugar_inicial_fantasma, 11)
    all_sprites.add(f)
    all_fantasmas.add(f)
    lugar_inicial_fantasma += 3

# INICIANDO O JOGO
while game:
    clock.tick(FPS)

    # EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.speedx += 8
            if event.key == pygame.K_a:
                player.speedx -= 8
            if event.key == pygame.K_w:
                player.speedy -= 8
            if event.key == pygame.K_s:
                player.speedy += 8

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.speedx = 0
            if event.key == pygame.K_a:
                player.speedx = 0
            if event.key == pygame.K_w:
                player.speedy = 0
            if event.key == pygame.K_s:
                player.speedy = 0

    #ATUALIZA O JOGO
    all_sprites.update()

    last_list.append(player.rect.x)
    last_list.append(player.rect.y)

    
    hits = pygame.sprite.spritecollide(player,mapa_com_blocos, False)
    if len(hits)>0:
        player.speedx =0 
        player.speedy =0 
        player.rect.x = last_list[2] 
        player.rect.y = last_list[3] 
        print('SPEEDY {}'.format(player.speedy))
        print('SPEEDX {}'.format(player.speedx))

    print(last_list)

    del last_list[0]
    del last_list[1]
    print(last_list)
    # GERA SAIDAS
    window.fill((0,0,0))
    window.blit(player.image, player.rect)

    all_sprites.draw(window)
    pygame.display.update()

