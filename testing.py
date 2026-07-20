import pygame
import sys

# 1. Start Pygame and build a window
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# 2. Setup our font and an empty box to hold our text
my_font = pygame.font.Font(None, 50)  # None means standard font, 50 is the size
typed_text = ""                       # This starts empty

# --- THE GAME LOOP (Runs forever at 60 frames per second) ---
while True:
    
    # STEP 1 & 2: LISTEN AND REMEMBER
    for event in pygame.event.get():
        # If the user clicks the X button, close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # If the user presses ANY key down
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_BACKSPACE:
                # If they hit Backspace, chop off the last letter
                typed_text = typed_text[:-1]
            else:
                # event.unicode is the exact letter they typed (like 'a', 'S', or '!')
                # We glue it to our typed_text string
                typed_text += event.unicode

    # STEP 3: DRAW IT TO THE SCREEN
    screen.fill((30, 30, 30))  # Clear the screen with a dark gray color
    
    # Turn our text string into a flat pixel picture. (True makes it smooth)
    text_picture = my_font.render(typed_text, True, (255, 255, 255))
    
    # Paste that picture onto the screen at coordinates X=50, Y=150
    screen.blit(text_picture, (50, 150))
    
    # Show our drawings to the player
    pygame.display.flip()
    clock.tick(60)  # Run the loop 60 times a second



    WIDTH, HEIGHT = 4545, 545453

    SCREEN = WIDTH, HEIGHT


    if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    typed_text = typed_text[:-1]
                else:
                    typed_text += event.unicode

    text_picture = my_font.render(typed_text, True, (255, 255, 255))
    SCREEN.blit(text_picture, (WIDTH//2, HEIGHT//2 + 100))

    pygame.display.update()
    pygame.time.wait(100000)