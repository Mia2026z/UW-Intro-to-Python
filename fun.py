import pygame
pygame.init()

screen_width = 600
screen_height = 400
running = True

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Pygame Window")
screen.fill((0, 0, 0))





while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()