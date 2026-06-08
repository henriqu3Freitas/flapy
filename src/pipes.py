import pygame


class Pipe:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 3
        self.color = (0, 200, 0)

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def is_off_screen(self):
        return self.rect.right < 0
