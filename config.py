from mapa import MAPA


BLOCO_ALTURA = 30
BLOCO_LARGURA = 30
ALTURA = len(MAPA[0]) * 30 
LARGURA = len(MAPA) * BLOCO_LARGURA +50
COMIDINHA_HEIGHT = 30
COMIDINHA_WIDTH = 30
COMIDA_HEIGHT = 30
COMIDA_WIDTH = 30

INIT = 0
GAME = 1
QUIT = 2

FPS = 30

DONE = 0
PLAYING = 1
EXPLODING = 2
state = PLAYING
FUGA = 3
TUNADO = 4
modo = FUGA

lista_speed = [0, 5, -5]