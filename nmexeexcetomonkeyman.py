
for mapa import MAPA
COMIDINHA_HEIGHT = 10
COMIDINHA_WIDTH = 10
class comidinhas:
    def __init__(self):
        self.image = pygame.image.load('assets/img/comidinha.png').convert_alpha()
        self.comidinhas = []

    def update(self):
        for l in len(MAPA):
            for c in range(len(MAPA[l])):
                if MAPA[l][c] == '1':
                    comida = comidinhas(self.image, c*20, l*20)
                    self.comidinhas.append(comida(l,c))
