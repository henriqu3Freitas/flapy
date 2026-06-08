import sys
import pygame
from src.player import Player
from src.pipes import Pipe


def run_game():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flapy")

    clock = pygame.time.Clock()
    FPS = 60

    BACKGROUND_COLOR = (135, 206, 235)
    GROUND_COLOR = (139, 69, 19)
    TEXT_COLOR = (255, 255, 255)

    GROUND_HEIGHT = 100
    GROUND_Y = SCREEN_HEIGHT - GROUND_HEIGHT

    def reset_game():
        player = Player(100, 250)
        pipe = Pipe(SCREEN_WIDTH + 200, 0, 80, 200)
        return player, pipe, False

    player, pipe, game_over = reset_game()

    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    player.jump()

                if event.key == pygame.K_r and game_over:
                    player, pipe, game_over = reset_game()

                if event.key == pygame.K_ESCAPE:
                    running = False

        if not game_over:
            player.update()

            pipe.update()

            if pipe.is_off_screen():
                pipe.rect.x = SCREEN_WIDTH

            if player.rect.colliderect(pipe.rect):
                game_over = True
                print("GAME OVER - Colidiu com o cano!")

            if player.rect.bottom >= GROUND_Y:
                game_over = True
                print("GAME OVER - Bateu no chão!")

            if player.rect.top <= 0:
                player.rect.top = 0
                player.velocity = 0

        screen.fill(BACKGROUND_COLOR)

        ground_rect = pygame.Rect(0, GROUND_Y, SCREEN_WIDTH, GROUND_HEIGHT)
        pygame.draw.rect(screen, GROUND_COLOR, ground_rect)

        player.draw(screen)
        pipe.draw(screen)

        title_text = font.render("Flapy - Prototipo Inicial", True, TEXT_COLOR)
        screen.blit(title_text, (10, 10))

        if not game_over:
            instruction_text = small_font.render("Pressione ESPACO para pular", True, TEXT_COLOR)
            screen.blit(instruction_text, (10, 50))

        if game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            game_over_text = font.render("GAME OVER", True, (255, 50, 50))
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
            screen.blit(game_over_text, text_rect)

            restart_text = small_font.render("Pressione R para reiniciar", True, TEXT_COLOR)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
            screen.blit(restart_text, restart_rect)

            exit_text = small_font.render("Pressione ESC para sair", True, TEXT_COLOR)
            exit_rect = exit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            screen.blit(exit_text, exit_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
