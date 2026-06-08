"""
Módulo dos Obstáculos
Define a classe Pipe que representa os canos (obstáculos) do jogo.
"""

import pygame


class Pipe:
    """
    Classe que representa um cano (obstáculo).

    Atributos:
        rect: retângulo que representa a posição e tamanho do cano
        speed: velocidade de movimento do cano (da direita para esquerda)
        color: cor do cano (verde)
    """

    def __init__(self, x, y, width, height):
        """
        Inicializa o cano na posição especificada.

        Args:
            x: posição horizontal inicial
            y: posição vertical inicial
            width: largura do cano
            height: altura do cano
        """
        # Criar retângulo do cano
        self.rect = pygame.Rect(x, y, width, height)

        # Velocidade de movimento
        self.speed = 3

        # Aparência
        self.color = (0, 200, 0)  # Verde

    def update(self):
        """
        Atualiza a posição do cano.
        Move o cano da direita para a esquerda.
        """
        self.rect.x -= self.speed

    def draw(self, screen):
        """
        Desenha o cano na tela.

        Args:
            screen: superfície do pygame onde o cano será desenhado
        """
        pygame.draw.rect(screen, self.color, self.rect)

    def is_off_screen(self):
        """
        Verifica se o cano saiu completamente da tela.

        Returns:
            True se o cano saiu da tela, False caso contrário
        """
        return self.rect.right < 0
