import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Press Enter to Start Example")

# 1. Define colors and font
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont(None, 55)

# 2. Game state to track if the game has started
game_state = "START_SCREEN"

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # 3. Check if the ENTER key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_state = "PLAYING"

    # Screen drawing logic based on the state
    screen.fill(BLACK) # Clear the screen

    if game_state == "START_SCREEN":
        # Render and draw the "Press Enter to Start" text
        text_surface = font.render("Press Enter to Start", True, WHITE)
        text_rect = text_surface.get_rect(center=(400, 300))
        screen.blit(text_surface, text_rect)
        
    elif game_state == "PLAYING":
        # Draw the actual game elements here
        game_text = font.render("Game Started! Have fun!", True, WHITE)
        game_rect = game_text.get_rect(center=(400, 300))
        screen.blit(game_text, game_rect)

    pygame.display.flip()
