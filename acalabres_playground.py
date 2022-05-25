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