dino = ""
# Dinosuar
if dino:

    import pygame
    pygame.init()

    screen_width = 640
    screen_height = 480
    running = True

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("My First Pygame Window")
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 255, 50), (100, 150, 70, 30))
    pygame.draw.rect(screen, (0, 255, 50), (185, 150, 35, 115))
    pygame.draw.rect(screen, (0, 255, 50), (235, 150, 35, 90))
    pygame.draw.rect(screen, (0, 255, 50), (285, 150, 35, 115))
    pygame.draw.rect(screen, (0, 255, 50), (335, 135, 35, 45))
    pygame.draw.rect(screen, (0, 255, 50), (385, 105, 50, 55))
    pygame.draw.rect(screen, (0, 255, 50), (385, 120, 85, 50))
    pygame.draw.rect(screen, (0, 0, 0), (395, 115, 10, 15))
    pygame.draw.rect(screen, (0, 0, 0), (410, 115, 10, 15))

    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.display.flip()

llama = ""
# Llama
if llama:

    import pygame
    pygame.init()
    
    screen_width = 600
    screen_height = 400
    running = True

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("My First Pygame Window")
    screen.fill((0, 0, 0))

    # Head
    pygame.draw.rect(screen, (255, 255, 255), (300, 150, 65, 55))
    # Ears
    pygame.draw.rect(screen, (255, 255, 255), (312, 125, 15, 25))
    pygame.draw.rect(screen, (255, 255, 255), (340, 125, 15, 25))
    pygame.draw.rect(screen, (255, 182, 193), (345, 130, 7, 20))
    pygame.draw.rect(screen, (255, 182, 193), (317, 130, 7, 20))
    # Body
    pygame.draw.rect(screen, (255, 255, 255), (225, 205, 130, 65))
    # Legs
    pygame.draw.rect(screen, (255, 255, 255), (250, 270, 20, 45))
    pygame.draw.rect(screen, (255, 255, 255), (305, 270, 20, 45))
    # Eyes
    pygame.draw.rect(screen, (0, 0, 0), (315, 160, 10, 20))
    pygame.draw.rect(screen, (0, 0, 0), (340, 160, 10, 20))
    # Tail
    pygame.draw.circle(screen, (255, 255, 255), (217, 225), (10))

    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()