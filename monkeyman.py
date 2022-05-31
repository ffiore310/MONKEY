<<<<<<< HEAD
class Comidinhas:
    pygame.sprite.Sprite.__init__(self)
    c = pygame.image.load('assets/img/comidinha.png').convert()
    def posicao_comidinhas(self):
        while game:
            window.blit(image, ())
=======
import pygame
import random
from mapa import MAPA
from fiorao import Bloco, Fantasma



class Pacman (pygame.sprite.Sprite):

    def __init__(self, images):

        pygame.sprite.Sprite.__init__(self)
        self.index_image = 0
        self.images = images
        self.image = self.images[self.index_image]
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.speedx = 0
        self.speedy = 0

    def update(self): 
        self.index_image = (self.index_image + 1) % len(self.images)
        self.image = self.images[self.index_image]
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

        self.rect.x += self.speedx 
        self.rect.y += self.speedy



pygame.init()

#-------------------- GERAR TELA PRINCIPAL--------------

BLOCO_ALTURA = 20
BLOCO_LARGURA = 20
ALTURA = len(MAPA[0]) * 20
LARGURA = len(MAPA) * BLOCO_LARGURA
window = pygame.display.set_mode((ALTURA, LARGURA))
lista_posicoes_disponiveis = []
lista_fantasmas = ['assets/img/fantasma azul .png', 'assets/img/fantasma laranja.png', 'assets/img/fantasma rosa 11.30.35.png', 'assets/img/fantasma vermelho .png']
lista_fantasmas_melhorados = []

altura_pac = 20
largura_pac = 20
pac_img = pygame.image.load('assets/img/pacman_direita.png').convert()
pac_img = pygame.transform.scale(pac_img, (altura_pac, largura_pac))
pac_imgs = [pac_img]

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

clock = pygame.time.Clock()
FPS = 30

player = Pacman(pac_imgs)

all_sprites = pygame.sprite.Group()

all_sprites.add(player)

while game:
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.speedx += 8
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_UP:
                player.speedy += 8
            if event.type == pygame.K_DOWN:
                player.speedy -= 8

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_UP:
                player.speedy -= 8
            if event.type == pygame.K_DOWN:
                player.speedy += 8

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
>>>>>>> f01ad279a1c27bbb85ed7763f9e1a90b15ecb0a4
