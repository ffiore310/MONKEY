import pygame
import random
from mapa import MAPA
from config import *
from classes import Bloco, Comidinha, Comida, Fantasma, Explosion, Pacman02
import time

pygame.init()
pygame.mixer.init()

#CRIANDO SOM
pygame.mixer.music.load('assets/snd/pacman_music.wav')
pygame.mixer.music.set_volume(0.3)
eating_sound = pygame.mixer.Sound('assets/snd/comidinha.wav')
comida_sound= pygame.mixer.Sound('assets/snd/comida_sound.wav')

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

# IMAGENS PAC-EXPLOSAO
explosion_anim = []
for i in range(10):
    filename = 'assets/img/fecha{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img, (25, 25))
    explosion_anim.append(img)

# IMAGENS FANTASMAS
img_fantasmas = []
for name in ['fantasma_azul.png', 'fantasma_laranja.png', 'fantasma_rosa.png', 'fantasma_vermelho.png']:
    img = pygame.image.load(f'assets/img/{name}')
    img = pygame.transform.scale(img, (30,30))
    img_fantasmas.append(img)
img_fantasma_puto = pygame.image.load('assets/img/super_fantasma.png')
img_fantasma_puto = pygame.transform.scale(img_fantasma_puto, (30,30))


assets = {}
assets["score_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
score = 0
lives = 3

keys_down = {}

#ACERTANDO OS FPS
clock = pygame.time.Clock()

#   CRIANDO VARIAVEL SUPER COLISAO
time_colisao_super = 0

# CRIANDO PERSONAGENS
player = Pacman02(paclist_img)


all_sprites.add(player)

# CRIANDO FANTASMAS F0
linha_inicial_fantasmas = 5
coluna_inicial_fantasmas = 8 
img_fantasmas[0]
lista_img_f0 = [img_fantasma_puto,img_fantasmas[0]]
f0 = Fantasma(lista_img_f0,coluna_inicial_fantasmas, linha_inicial_fantasmas, mapa_com_blocos,modo)
all_sprites.add(f0)
all_fantasmas.add(f0)

# CRIANDO FANTASMAS F1
linha_inicial_fantasmas = 5
coluna_inicial_fantasmas = 28
img_fantasmas[1]
lista_img_f1 = [img_fantasma_puto,img_fantasmas[1]]
f1 = Fantasma(lista_img_f1, coluna_inicial_fantasmas, linha_inicial_fantasmas, mapa_com_blocos, modo)
all_sprites.add(f1)
all_fantasmas.add(f1)

# CRIANDO FANTASMAS F2
linha_inicial_fantasmas = 17
coluna_inicial_fantasmas = 8 
img_fantasmas[2]
lista_img_f2 = [img_fantasma_puto,img_fantasmas[2]]
f2 = Fantasma(lista_img_f2,coluna_inicial_fantasmas, linha_inicial_fantasmas, mapa_com_blocos,modo)
all_sprites.add(f2)
all_fantasmas.add(f2)

# CRIANDO FANTASMAS F3
linha_inicial_fantasmas = 17
coluna_inicial_fantasmas = 28   
img_fantasmas[3]
lista_img_f3 = [img_fantasma_puto,img_fantasmas[3]]
f3 = Fantasma(lista_img_f3,coluna_inicial_fantasmas, linha_inicial_fantasmas, mapa_com_blocos,modo)
all_sprites.add(f3)
all_fantasmas.add(f3)

pygame.mixer.music.play(loops=-1)

tela_inicial = pygame.image.load('assets/img/tela_inicial.png')
tela_inicial2 = pygame.image.load('assets/img/tela_inicial2.png')
tela_final = pygame.image.load('assets/img/tela_gameover.png')
tela_final2 = pygame.image.load('assets/img/tela_gameover2.png')

black=(0,0,0)
fecha=False
while (fecha==False):
    window.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fecha=True
    window.blit(tela_inicial,(150, 150))

    pygame.display.flip()

black=(0,0,0)
fecha=False
while (fecha==False):
    window.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fecha=True
    window.blit(tela_inicial2,(100, 100))
    pygame.display.flip()

comidinha_total = 318
# INICIANDO O JOGO
while state != DONE:
    clock.tick(FPS)

    # EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = DONE
        if state == PLAYING:
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_d:
                    player.speedx += 5
                if event.key == pygame.K_a:
                    player.speedx -= 5
                if event.key == pygame.K_w:
                    player.speedy -= 5
                if event.key == pygame.K_s:
                    player.speedy += 5
                if event.key == pygame.K_q:
                    game = False

            if event.type == pygame.KEYUP:
                if event.key in keys_down and keys_down[event.key]:
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

    if state == PLAYING:

    #COLISÃO COMIDINHAS 
        hits_comidinhas = pygame.sprite.spritecollide(player, all_comidinhas, True)
        for comidinha in hits_comidinhas:
            score += 100
        if len(hits_comidinhas) > 0:
        # Toca o som da colisão
            eating_sound.play()
            time.sleep(0.01) # Precisa esperar senão fecha
            comidinha_total -=1
        if comidinha_total == 0:
            fecha=False
            while (fecha==False):
                window.fill(black)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                            fecha=True
                window.blit(tela_final2,(100, 100))
                pygame.display.flip()

        #COLISÃO SUPER COMIDA 
        hits_comida = pygame.sprite.spritecollide(player, all_comidas, True)
        if len(hits_comida) >0:
            modo = TUNADO
            f0.state = TUNADO
            f1.state = TUNADO
            f2.state = TUNADO
            f3.state = TUNADO
            time_colisao_super = pygame.time.get_ticks()
            comida_sound.play()
            time.sleep(0.01) # Precisa esperar senão fecha
        
        #TEMPO MODO TUNADO
        agr = pygame.time.get_ticks()
        a = (agr - time_colisao_super) /300
        if a  > 25.5:
            modo = FUGA
            f0.state = FUGA
            f1.state = FUGA
            f2.state = FUGA
            f3.state = FUGA
            
        #COLISÃO FANTASMAS 
        hits_fantasmas = pygame.sprite.spritecollide(player, all_fantasmas, False)
        if modo == FUGA:
            if len(hits_fantasmas) >0:
                player.kill()
                explosao = Explosion(player.rect.center, explosion_anim)
                all_sprites.add(explosao)
                lives = - 1
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
                if lives == 0:
                    black=(0,0,0)
                    fecha=False
                    while (fecha==False):
                        window.fill(black)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    fecha=True
                        window.blit(tela_final,(150, 150))
                        pygame.display.flip()
        elif modo == TUNADO:
            if len(hits_fantasmas) >0:
                conta_fts += 1
                if conta_fts > 3:
                    conta_fts = 0
                # CRIANDO FANTASMAS F0
                if conta_fts == 0: 
                    hits_fantasmas[0].rect.x = 8* BLOCO_LARGURA
                    hits_fantasmas[0].rect.y = 5* BLOCO_ALTURA
                # CRIANDO FANTASMAS F1
                if conta_fts == 1:
                    hits_fantasmas[0].rect.x = 28* BLOCO_LARGURA
                    hits_fantasmas[0].rect.y = 5* BLOCO_ALTURA
                # CRIANDO FANTASMAS F2
                if conta_fts == 2:
                    hits_fantasmas[0].rect.x = 8* BLOCO_LARGURA
                    hits_fantasmas[0].rect.y = 17* BLOCO_ALTURA
                # CRIANDO FANTASMAS F2
                if conta_fts == 3:
                    hits_fantasmas[0].rect.x = 28* BLOCO_LARGURA
                    hits_fantasmas[0].rect.y = 17 * BLOCO_ALTURA
                score += 500

    elif state == EXPLODING:
        now = pygame.time.get_ticks()
        if now - explosion_tick > explosion_duration:
            if lives == 0:
                state = DONE
            else:
                state = PLAYING
                player =  Pacman02(paclist_img)
                all_sprites.add(player)

    # COLISAO PAC-PAREDE
    hits = pygame.sprite.spritecollide(player,mapa_com_blocos, False)
    if len(hits)>0:
        if player.speedx > 0:
            player.rect.right =  hits[0].rect.left
            player.speedx =0
        if player.speedx <0:
            player.rect.left =  hits[0].rect.right
            player.speedx =0
        if player.speedy >0:
            player.rect.bottom =  hits[0].rect.top
            player.speedy =0
        if player.speedy <0:
            player.rect.top   =  hits[0].rect.bottom
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

