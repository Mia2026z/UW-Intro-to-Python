# import pygame

# pygame.init()

# # Set window size
# screen_width = 640
# screen_height = 480


# # Create display window
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("My First Pygame Window")

# while True:
#     pygame.display.flip()
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    # This event loop prevents the jumping/freezing on macOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()

pygame.quit()
sys.exit()
