"""
Módulo Principal do Jogo
Contém a lógica principal do jogo, incluindo o loop de execução.
"""

import sys
import pygame
from src.player import Player
from src.pipes import Pipe


def run_game():
    """
    Função principal que executa o jogo.
    Inicializa o pygame, cria a janela, instancia objetos e executa o loop principal.
    """
    # ===========================
    # INICIALIZAÇÃO
    # ===========================
    pygame.init()

    # Configurações da janela
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flapy")

    # Configurar relógio para controlar FPS
    clock = pygame.time.Clock()
    FPS = 60

    # Cores
    BACKGROUND_COLOR = (135, 206, 235)  # Azul claro (céu)
    GROUND_COLOR = (139, 69, 19)  # Marrom (chão)
    TEXT_COLOR = (255, 255, 255)  # Branco

    # Altura do chão
    GROUND_HEIGHT = 100
    GROUND_Y = SCREEN_HEIGHT - GROUND_HEIGHT

    # ===========================
    # CRIAR OBJETOS DO JOGO
    # ===========================

    def reset_game():
        """Reinicia o jogo criando novos objetos"""
        player = Player(100, 250)  # Posição mais alta
        pipe = Pipe(SCREEN_WIDTH + 200, 0, 80, 200)  # Cano mais longe e mais baixo
        return player, pipe, False

    # Criar objetos iniciais
    player, pipe, game_over = reset_game()

    # Configurar fonte para texto
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)

    # ===========================
    # LOOP PRINCIPAL DO JOGO
    # ===========================

    running = True

    while running:
        # Controlar taxa de atualização (FPS)
        clock.tick(FPS)

        # ===========================
        # CAPTURAR EVENTOS
        # ===========================
        for event in pygame.event.get():
            # Evento de fechar janela
            if event.type == pygame.QUIT:
                running = False

            # Evento de tecla pressionada
            if event.type == pygame.KEYDOWN:
                # Pressionar ESPAÇO para pular (apenas se o jogo não acabou)
                if event.key == pygame.K_SPACE and not game_over:
                    player.jump()

                # Pressionar R para reiniciar após game over
                if event.key == pygame.K_r and game_over:
                    player, pipe, game_over = reset_game()

                # Pressionar ESC para sair
                if event.key == pygame.K_ESCAPE:
                    running = False

        # ===========================
        # ATUALIZAR OBJETOS
        # ===========================
        if not game_over:
            # Atualizar jogador
            player.update()

            # Atualizar cano
            pipe.update()

            # Se o cano saiu da tela, reposicionar
            if pipe.is_off_screen():
                pipe.rect.x = SCREEN_WIDTH

            # ===========================
            # VERIFICAR COLISÕES
            # ===========================

            # Colisão com o cano
            if player.rect.colliderect(pipe.rect):
                game_over = True
                print("GAME OVER - Colidiu com o cano!")

            # Colisão com o chão
            if player.rect.bottom >= GROUND_Y:
                game_over = True
                print("GAME OVER - Bateu no chão!")

            # Colisão com o teto
            if player.rect.top <= 0:
                player.rect.top = 0
                player.velocity = 0

        # ===========================
        # DESENHAR NA TELA
        # ===========================

        # Limpar tela com cor de fundo
        screen.fill(BACKGROUND_COLOR)

        # Desenhar chão
        ground_rect = pygame.Rect(0, GROUND_Y, SCREEN_WIDTH, GROUND_HEIGHT)
        pygame.draw.rect(screen, GROUND_COLOR, ground_rect)

        # Desenhar objetos do jogo
        player.draw(screen)
        pipe.draw(screen)

        # Desenhar título
        title_text = font.render("Flapy - Prototipo Inicial", True, TEXT_COLOR)
        screen.blit(title_text, (10, 10))

        # Desenhar instruções
        if not game_over:
            instruction_text = small_font.render("Pressione ESPACO para pular", True, TEXT_COLOR)
            screen.blit(instruction_text, (10, 50))

        # Se game over, mostrar mensagem
        if game_over:
            # Desenhar fundo semi-transparente atrás do texto
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            # Mensagem principal
            game_over_text = font.render("GAME OVER", True, (255, 50, 50))
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
            screen.blit(game_over_text, text_rect)

            # Instruções de reinício
            restart_text = small_font.render("Pressione R para reiniciar", True, TEXT_COLOR)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
            screen.blit(restart_text, restart_rect)

            # Instrução de sair
            exit_text = small_font.render("Pressione ESC para sair", True, TEXT_COLOR)
            exit_rect = exit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            screen.blit(exit_text, exit_rect)

        # Atualizar a tela
        pygame.display.flip()

    # ===========================
    # ENCERRAR
    # ===========================
    pygame.quit()
    sys.exit()
