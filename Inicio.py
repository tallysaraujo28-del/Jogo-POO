import pygame
import random

LARGURA = 832
ALTURA = 608

LARGURA_MUNDO = 1920
ALTURA_MUNDO = 1080


class Jogador:
    def __init__(self):
        self.x = LARGURA_MUNDO // 2
        self.y = ALTURA_MUNDO // 2
        self.tamanho = 32
        self.velocidade = 4

    def mover(self, teclas):
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.x -= self.velocidade

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.x += self.velocidade

        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.y += self.velocidade

        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.y -= self.velocidade

        # limites do mundo
        self.x = max(0, min(self.x, LARGURA_MUNDO - self.tamanho))
        self.y = max(0, min(self.y, ALTURA_MUNDO - self.tamanho))

    def desenhar(self, tela, camera_x, camera_y):
        pygame.draw.rect(tela, (0, 0, 255),
                         (self.x - camera_x, self.y - camera_y, self.tamanho, self.tamanho))


class Jogo:
    def __init__(self):
        self.tela = pygame.display.get_surface()  # usa a mesma janela do menu
        self.fundo = pygame.image.load('fundo de jogo.png')
        self.relogio = pygame.time.Clock()
        self.jogador = Jogador()
        self.camera_x = 0
        self.camera_y = 0
        self.rodando = True

        pygame.display.set_caption('Jogo')

    def atualizar_camera(self):
        self.camera_x = self.jogador.x - LARGURA // 2
        self.camera_y = self.jogador.y - ALTURA // 2

        self.camera_x = max(0, min(self.camera_x, LARGURA_MUNDO - LARGURA))
        self.camera_y = max(0, min(self.camera_y, ALTURA_MUNDO - ALTURA))

    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.rodando = False  # ESC volta para o menu

    def desenhar(self):
        self.tela.blit(self.fundo, (-self.camera_x, -self.camera_y))
        self.jogador.desenhar(self.tela, self.camera_x, self.camera_y)
        pygame.display.update()

    def rodar(self):
        while self.rodando:
            self.eventos()
            self.jogador.mover(pygame.key.get_pressed())
            self.atualizar_camera()
            self.desenhar()
            self.relogio.tick(60)