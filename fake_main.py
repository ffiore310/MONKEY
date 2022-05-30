import pygame
from classe_pacman import Pacman, Pacman02

# INICIANDO O JOGO

pygame.init()

#CRIANDO A JANELA
largura = 500
altura = 500
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Fake main- PACMAN')

#DEFININDO IMAGENS
pac_img_fechado = pygame.image.load('assets/img/pacman_fechado.png')
pac_img_fechado = pygame.transform.scale(pac_img_fechado, (50,50))
pac_img_aberto = pygame.image.load('assets/img/pacman_direita.png')
pac_img_aberto = pygame.transform.scale(pac_img_aberto, (50,50))
pac_img_aberto_esquerda = pygame.image.load('assets/img/pacman_esquerdo .png')
pac_img_aberto_esquerda = pygame.transform.scale(pac_img_aberto_esquerda, (50,50))

pac_img_aberto_cima = pygame.image.load('assets/img/pacman_cima.png')
pac_img_aberto_cima = pygame.transform.scale(pac_img_aberto_cima, (50,50))

pac_img_aberto_baixo = pygame.image.load('assets/img/pacman_baixo.png')
pac_img_aberto_baixo = pygame.transform.scale(pac_img_aberto_baixo, (50,50))

paclist_img = [pac_img_fechado, pac_img_aberto,pac_img_aberto_esquerda, pac_img_aberto_cima, pac_img_aberto_baixo]

#DEFININDO PARAMETROS
player = Pacman02(paclist_img)

all_sprites = pygame.sprite.Group
all_sprites.add(player)
    
game = True

#ACERTANDO OS FPS
clock = pygame.time.Clock()
FPS = 10

#INICIANDO A LOGICA DO JOGO
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

    # ATUALIZAR O JOGO
    player.update(paclist_img)

    #GERA SAIDAS
    window.fill((7, 3, 252))
    window.blit(player.image, player.rect)

    pygame.display.update()






pygame.quit()