import pygame
from Inicio import Jogo

pygame.init()

LARGURA = 832
ALTURA = 608

botoes = []

for i in range(0, 6):
    botoes.append((123*i, 0, 123, 28))

class Principal:
    def __init__(self):
        self.mostrar_principal = pygame.display.set_mode((LARGURA, ALTURA))

        self.fundo = pygame.image.load('fundo.jpg')

        self.fonte = pygame.font.Font('Pixel Operator/PixelOperator8-Bold.ttf', 50)

        self.botao = pygame.image.load('botões.png')

        self.text_titulo = self.fonte.render('ARQUIVO: 666', True, (255, 0, 0))

        self.frame = []

        for e in range(0, 6):
            self.frame.append(self.botao.subsurface(botoes[e]))
        
        self.fundo = pygame.transform.scale(self.fundo, (LARGURA, ALTURA))

        for e in range(0, 6):
            self.frame[e] = pygame.transform.scale(self.frame[e], (262, 56))

        self.centro = self.frame[0].get_rect(center=(LARGURA // 2, ALTURA // 2))

        self.centro_novo = self.frame[2].get_rect(center=(LARGURA // 2, self.centro.bottom + 40))

        self.outro_centro = self.frame[4].get_rect(center=(LARGURA // 2, self.centro_novo.bottom + 40))

        self.titulo = self.text_titulo.get_rect(center=(LARGURA // 2, self.centro.top - 200))

        pygame.display.set_caption('Jogo')

principal = Principal()

class Rodando:
    def __init__(self):
        self.principal = principal

        self.rodando = True

        self.estado_jogar = 0

        self.estado_creditos = 2

        self.estado_sair = 4

        while self.rodando:

            pos_mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.rodando = False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.principal.centro.collidepoint(pos_mouse):
                        Jogo().rodar()

                    if self.principal.outro_centro.collidepoint(pos_mouse):
                        self.rodando = False

            if self.principal.centro.collidepoint(pos_mouse):
                self.estado_jogar = 1
            
            else:
                self.estado_jogar = 0

            if self.principal.centro_novo.collidepoint(pos_mouse):
                self.estado_creditos = 3
            
            else:
                self.estado_creditos = 2

            if self.principal.outro_centro.collidepoint(pos_mouse):
                self.estado_sair = 5

            else:
                self.estado_sair = 4

            self.principal.mostrar_principal.blit(self.principal.fundo, (0, 0))
            self.principal.mostrar_principal.blit(self.principal.frame[self.estado_jogar], self.principal.centro)
            self.principal.mostrar_principal.blit(self.principal.frame[self.estado_creditos], self.principal.centro_novo)
            self.principal.mostrar_principal.blit(self.principal.frame[self.estado_sair], self.principal.outro_centro)
            self.principal.mostrar_principal.blit(self.principal.text_titulo, self.principal.titulo)
            pygame.display.update()

loop = Rodando()