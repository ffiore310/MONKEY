import random
from mapa import MAPA
import pygame
from classes import Bloco, Comidinha, Pacman02, Fantasma, Comida
from config import *

pygame.init()

# DEFINICAO MAPA

window = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption('PAC-MAN')

img_bloco = pygame.image.load('assets/img/bloco_jogo_pacman.jpg').convert()
img_bloco = pygame.transform.scale(img_bloco, (27,27))
mapa_com_blocos = pygame.sprite.Group()

img_comidinha = pygame.image.load('assets/img/bolinha.png').convert_alpha()
img_comidinha = pygame.transform.scale(img_comidinha, (10,10))

img_comida = pygame.image.load('assets/img/comidinha.png').convert_alpha()
img_comida = pygame.transform.scale(img_comida, (20,20))

all_comidas = pygame.sprite.Group()
all_comidinhas = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_fantasmas = pygame.sprite.Group()

for l in range(len(MAPA)):
    for c in range(len(MAPA[l])):
        if MAPA[l][c] == 0:
            bloco = Bloco(img_bloco, c, l)
            mapa_com_blocos.add(bloco)
            all_sprites.add(bloco)

for x in range(len(MAPA)):
    for y in range(len(MAPA[x])):
        if MAPA[x][y] == 1:
            bolinha = Comidinha(img_comidinha, y+0.35, x+0.35)
            all_comidinhas.add(bolinha)
            all_sprites.add(bolinha)

for x in range(len(MAPA)):
    for y in range(len(MAPA[x])):
        if MAPA[x][y] == 4:
            comida = Comida(img_comida, y+0.25, x+0.25)
            all_comidas.add(comida)
            all_sprites.add(comida)


# IMAGENS PACMAN

pac_img_fechado = pygame.image.load('assets/img/pacman_fechado.png')
pac_img_fechado = pygame.transform.scale(pac_img_fechado, (25,25))
pac_img_aberto = pygame.image.load('assets/img/pacman_direita.png')
pac_img_aberto = pygame.transform.scale(pac_img_aberto, (25,25))
pac_img_aberto_esquerda = pygame.image.load('assets/img/pacman_esquerdo .png')
pac_img_aberto_esquerda = pygame.transform.scale(pac_img_aberto_esquerda, (25,25))

pac_img_aberto_cima = pygame.image.load('assets/img/pacman_cima.png')
pac_img_aberto_cima = pygame.transform.scale(pac_img_aberto_cima, (25,25))

pac_img_aberto_baixo = pygame.image.load('assets/img/pacman_baixo.png')
pac_img_aberto_baixo = pygame.transform.scale(pac_img_aberto_baixo, (25,25))

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

assets = {}
assets["score_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)

score = 0
lives = 3

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
            if event.key == pygame.K_q:
                game = False

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

   #COLISÃO COMIDINHAS 
    hits_comidinhas = pygame.sprite.spritecollide(player, all_comidinhas, True)
    for comidinha in hits_comidinhas:
        score += 100

    #COLISÃO SUPER COMIDA 
    hits_comida = pygame.sprite.spritecollide(player, all_comidas, True)

    #COLISÃO FANTASMAS 
    hits_fantasmas = pygame.sprite.spritecollide(player, all_fantasmas, True)
    if len(hits_fantasmas)>0:
        player.kill()
        lives = - 1

    # COLISAO PAC-PAREDE
    hits = pygame.sprite.spritecollide(player,mapa_com_blocos, False)
    if len(hits)>0:
        if player.speedx > 0:
            player.rect.right =  hits[0].rect.left
        if player.speedx <0:
            player.rect.left =  hits[0].rect.right
        if player.speedy >0:
            player.rect.bottom =  hits[0].rect.top
        if player.speedy <0:
            player.rect.top   =  hits[0].rect.bottom
        player.speedx =0 
        player.speedy =0 

    # TELETRANSPORTE PACMAN
    if player.rect.right > ALTURA:
        player.rect.x = 0
        player.rect.y = 330
    if player.rect.left < 0:
        player.rect.x = 1080
        player.rect.y = 330

    # GERA SAIDAS
    window.fill((0,0,0))
    window.blit(player.image, player.rect)

    all_sprites.draw(window)

    # Desenhando o score
    text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (ALTURA/ 2,  700)
    window.blit(text_surface, text_rect)

    # Desenhando as vidas
    text_surface = assets['score_font'].render(chr(9829) * lives, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (10, LARGURA - 10)
    window.blit(text_surface, text_rect)

    pygame.display.update()

