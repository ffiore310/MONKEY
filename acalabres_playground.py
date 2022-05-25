import pygame
mapa = [
    '0000000000000000000000000000000000',
    '0               00               0',
    '0   0   0 0 0    0'
]

for l in range(len(mapa)):
    for c in range(len(mapa[l])):
        if mapa[l][c] == '0':
            b = Bloco(img, l * 20, c * 20)
            all_blocks.add(b)

class Pacman (pygame.sprite.Sprite):

    def __init__(self, images):

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


game = True

clock = pygame.time.Clock()
FPS = 30


player = Pacman(pac_img)

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

    all_sprites.update()