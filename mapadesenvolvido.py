from mapa import MAPA
import pygame
from classes import Bloco, Pacman02

pygame.init()

# DEFINICAO MAPA

BLOCO_ALTURA = 30
BLOCO_LARGURA = 30
ALTURA = len(MAPA[0]) * 30
LARGURA = len(MAPA) * BLOCO_LARGURA

window = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption('PAC-MAN')

img_bloco = pygame.image.load('assets/img/bloco_jogo_pacman.jpg').convert()
img_bloco = pygame.transform.scale(img_bloco, (30,30))
mapa_com_blocos = pygame.sprite.Group()

for l in range(len(MAPA)):
    for c in range(len(MAPA[l])):
        if MAPA[l][c] == 0:
            bloco = Bloco(img_bloco, c * 30, l * 30)
            mapa_com_blocos.add(bloco)

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

game= True

#ACERTANDO OS FPS
clock = pygame.time.Clock()
FPS = 10

# CRIANDO PERSONAGENS
player = Pacman02(paclist_img)

all_sprites = pygame.sprite.Group
all_sprites.add(player)
    

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
                player.speedx -= 8
            if event.key == pygame.K_a:
                player.speedx += 8
            if event.key == pygame.K_w:
                player.speedy += 8
            if event.key == pygame.K_s:
                player.speedy -= 8

    #ATUALIZA O JOGO
    mapa_com_blocos.update()
    player.update(paclist_img)

    # GERA SAIDAS
    window.fill((0,0,0))
    window.blit(player.image, player.rect)

    mapa_com_blocos.draw(window)
    pygame.display.update()

teste 