"""
Módulo do Jogador
Define a classe Player que representa o pássaro controlado pelo jogador.
"""

import pygame


class Player:
    """
    Classe que representa o pássaro jogável.

    Atributos:
        rect: retângulo que representa a posição e tamanho do pássaro
        velocity: velocidade vertical do pássaro (positivo = caindo, negativo = subindo)
        gravity: força da gravidade aplicada ao pássaro
        jump_strength: força do pulo quando o jogador pressiona espaço
        color: cor do pássaro (amarelo)
    """

    def __init__(self, x, y):
        """
        Inicializa o pássaro na posição especificada.

        Args:
            x: posição horizontal inicial
            y: posição vertical inicial
        """
        # Criar retângulo do pássaro (largura: 40, altura: 40)
        self.rect = pygame.Rect(x, y, 40, 40)

        # Física do movimento
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10

        # Aparência
        self.color = (255, 255, 0)  # Amarelo

    def jump(self):
        """
        Faz o pássaro pular (subir).
        Define a velocidade vertical para um valor negativo.
        """
        self.velocity = self.jump_strength

    def update(self):
        """
        Atualiza a posição e velocidade do pássaro.
        Aplica a gravidade e move o pássaro verticalmente.
        """
        # Aplicar gravidade (aumenta a velocidade de queda)
        self.velocity += self.gravity

        # Atualizar posição vertical baseado na velocidade
        self.rect.y += self.velocity

    def draw(self, screen):
        """
        Desenha o pássaro na tela.

        Args:
            screen: superfície do pygame onde o pássaro será desenhado
        """
        # Desenhar o corpo do pássaro como um círculo
        center_x = self.rect.centerx
        center_y = self.rect.centery
        radius = 20

        # Corpo (círculo amarelo)
        pygame.draw.circle(screen, self.color, (center_x, center_y), radius)

        # Olho (círculo branco)
        pygame.draw.circle(screen, (255, 255, 255), (center_x + 8, center_y - 5), 6)
        # Pupila (círculo preto)
        pygame.draw.circle(screen, (0, 0, 0), (center_x + 10, center_y - 5), 3)

        # Bico (triângulo laranja)
        beak_points = [
            (center_x + radius, center_y),
            (center_x + radius + 10, center_y - 5),
            (center_x + radius + 10, center_y + 5)
        ]
        pygame.draw.polygon(screen, (255, 140, 0), beak_points)
