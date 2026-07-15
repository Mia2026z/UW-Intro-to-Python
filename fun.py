import pygame
pygame.init()

screen = pygame.display.set_mode((400, 400))

# Fill the screen with red
screen.fill((255, 0, 0))
pygame.display.update()
pygame.time.wait(100000)

# Fill the screen with green
screen.fill((0, 255, 0))
pygame.display.update()
pygame.time.wait(100000)

# Fill the screen with blue
screen.fill((0, 0, 255))
pygame.display.update()
pygame.time.wait(100000)

pygame.quit()

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.event.QUIT():
#             running = False