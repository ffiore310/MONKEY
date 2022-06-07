import pygame
import random
from mapa import MAPA
from config import *

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
        
import random
from mapa import MAPA
import pygame
from classes import Bloco, Comidinha, Fantasma, Comida
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

# IMAGENS PAC-EXPLOSAO
explosion_anim = []
for i in range(10):
    filename = 'assets/img/fecha{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img, (25, 25))
    explosion_anim.append(img)

img_fantasmas = []
for name in ['fantasma_azul.png', 'fantasma_laranja.png', 'fantasma_rosa.png', 'fantasma_vermelho.png']:
    img = pygame.image.load(f'assets/img/{name}')
    img = pygame.transform.scale(img, (30,30))
    img_fantasmas.append(img)

DONE = 0
PLAYING = 1
EXPLODING = 2
state = PLAYING
FUGA = 3
TUNADO = 4
modo = FUGA


assets = {}
assets["score_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
score = 0
lives = 3

keys_down = {}

#ACERTANDO OS FPS
clock = pygame.time.Clock()
FPS = 30

# CRIANDO PERSONAGENS
player = Pacman02(paclist_img)


all_sprites.add(player)
lugar_inicial_fantasma = 13   
for fantasmas in img_fantasmas:
    f = Fantasma(fantasmas,lugar_inicial_fantasma, 11, mapa_com_blocos  )
    all_sprites.add(f)
    all_fantasmas.add(f)
    lugar_inicial_fantasma += 3



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

        #COLISÃO SUPER COMIDA 
        hits_comida = pygame.sprite.spritecollide(player, all_comidas, True)
        if len(hits_comida) >0:
            modo = TUNADO
            hits_fantasmas01 = pygame.sprite.spritecollide(player, all_fantasmas, False)
            if len(hits_fantasmas01)>0:
                hits_fantasmas01[0].rect.x = l * BLOCO_LARGURA
                hits_fantasmas01[0].rect.y = c * BLOCO_ALTURA
            

    
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
        elif modo == TUNADO:
            if len(hits_fantasmas) >0:
                hits_fantasmas[0].kill()
                f = Fantasma(fantasmas,lugar_inicial_fantasma, 11, mapa_com_blocos  )
                all_sprites.add(f)
                all_fantasmas.add(f)

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




