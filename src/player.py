import pygame


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.color = (255, 255, 0)

    def jump(self):
        self.velocity = self.jump_strength

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

    def draw(self, screen):
        center_x = self.rect.centerx
        center_y = self.rect.centery
        radius = 20
        pygame.draw.circle(screen, self.color, (center_x, center_y), radius)
        pygame.draw.circle(screen, (255, 255, 255), (center_x + 8, center_y - 5), 6)
        pygame.draw.circle(screen, (0, 0, 0), (center_x + 10, center_y - 5), 3)
        beak_points = [
            (center_x + radius, center_y),
            (center_x + radius + 10, center_y - 5),
            (center_x + radius + 10, center_y + 5)
        ]
        pygame.draw.polygon(screen, (255, 140, 0), beak_points)
