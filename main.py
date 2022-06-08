import pygame
from mapa import MAPA
from config import *
from jogo import jogo

pygame.init()
pygame.mixer.init()

#-------------------- GERAR TELA PRINCIPAL--------------
window = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption('PAC-MAN')

jogo(window)

pygame.quit()