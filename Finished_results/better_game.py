import pygame
import sys

pygame.init()

# Part of scoring (keeps track of how many bounces player got)
bounce = 0

# Blocks
blocks_active = False
blocks = []

# Width and Hegiht of screen
WIDTH, HEIGHT = 800, 600

# Font used for screen
font = pygame.font.Font(None, 74)
continue_font = pygame.font.Font(None, 30)
my_font = pygame.font.Font(None, 50)

# Screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball game")
CLOCK = pygame.time.Clock()

# The current state of the game
game_state = "START"

# Paddle
player_paddle = pygame.Rect(WIDTH//2 - 37, 425, 75, 15)

# Ball
ball = pygame.Rect(WIDTH//2, 50, 20, 20)
x_speed, y_speed = 4, 4

# Main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Game modes
        if event.type == pygame.KEYDOWN:

            # Game levels
            if game_state == "START":

                # Training level
                if event.key == pygame.K_t:
                    ball.x, ball.y = WIDTH//2 - 10, 50
                    x_speed, y_speed = 4, 4
                    player_paddle = pygame.Rect(WIDTH//2 - 37, 425, 75, 15)
                    blocks_active = False
                    game_state = "PLAYING"

                # Level Easy: Blocks
                elif event.key == pygame.K_e:
                    ball.x, ball.y = WIDTH//2 - 10, 50
                    x_speed, y_speed = 3, 3
                    player_paddle = pygame.Rect(WIDTH//2 - 37, 425, 75, 15)
                    blocks_active = True
                    blocks = [pygame.Rect(100, 150, 75, 75),
                                pygame.Rect(180, 150, 75, 75),
                                pygame.Rect(260, 150, 75, 75),
                                pygame.Rect(480, 150, 75, 75),
                                pygame.Rect(560, 150, 75, 75),
                                pygame.Rect(640, 150, 75, 75)]
                    game_state = "PLAYING"

                # Level Medium: Blocks + speed
                elif event.key == pygame.K_m:
                    ball.x, ball.y = WIDTH//2 - 10, 50
                    x_speed, y_speed = 5, 5
                    player_paddle = pygame.Rect(WIDTH//2 - 37, 425, 75, 15)
                    blocks_active = True
                    blocks = [pygame.Rect(100, 150, 75, 75),
                                pygame.Rect(180, 150, 75, 75),
                                pygame.Rect(260, 150, 75, 75),
                                pygame.Rect(400, 150, 75, 75),
                                pygame.Rect(480, 150, 75, 75),
                                pygame.Rect(560, 150, 75, 75),
                                pygame.Rect(640, 150, 75, 75)]
                    game_state = "PLAYING"

                # Level Hard: Platform small + blocks
                elif event.key == pygame.K_h:
                    ball.x, ball.y = WIDTH//2 - 10, 50
                    x_speed, y_speed = 3, 3
                    player_paddle = pygame.Rect(WIDTH//2 - 37, 425, 40, 15)
                    blocks_active = True
                    blocks = [pygame.Rect(180, 150, 75, 75),
                                pygame.Rect(260, 150, 75, 75),
                                pygame.Rect(400, 150, 75, 75),
                                pygame.Rect(480, 150, 75, 75),
                                pygame.Rect(560, 150, 75, 75),
                                pygame.Rect(640, 150, 75, 75)]
                    game_state = "PLAYING"

                # Level Extreme: Blocks + speed + platform small
                elif event.key == pygame.K_x:
                    ball.x, ball.y = WIDTH//2 - 10, 50
                    x_speed, y_speed = 6, 6
                    player_paddle = pygame.Rect(WIDTH//2 - 37, 425, 40, 15)
                    blocks_active = True
                    blocks = [pygame.Rect(100, 150, 75, 75),
                                pygame.Rect(180, 150, 75, 75),
                                pygame.Rect(260, 150, 75, 75),
                                pygame.Rect(400, 150, 75, 75),
                                pygame.Rect(480, 150, 75, 75),
                                pygame.Rect(560, 150, 75, 75),
                                pygame.Rect(640, 150, 75, 75)]
                    game_state = "PLAYING"

                # Quitting the game
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

            # If game over or victory
            elif game_state == "GAME_OVER" or game_state == "VICTORY":
                if event.key == pygame.K_SPACE:
                    bounce = 0
                    game_state = "PLAYING"
                elif event.key == pygame.K_RETURN:
                    bounce = 0
                    game_state = "START"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

    # Left and right keys to move paddle
    if game_state == "PLAYING":
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT] and player_paddle.left > 0:
            player_paddle.left -= 7

        if keys_pressed[pygame.K_RIGHT] and player_paddle.right < WIDTH:
            player_paddle.right += 7

        ball.x += x_speed
        ball.y += y_speed

        # Ball bouncing off paddle
        if ball.colliderect(player_paddle):
            if y_speed > 0 and ball.bottom >= player_paddle.top and ball.top < player_paddle.top:
                ball.bottom = player_paddle.top
                y_speed *= -1
                bounce += 1

        # Ball bouncing off blocks
        if blocks_active:
            hit_index = ball.collidelist(blocks)
            if hit_index != -1:
                y_speed *= -1
                blocks.pop(hit_index)

            # If player breaks all blocks, victory
            if len(blocks) == 0:
                game_state = "VICTORY"

        #Ball bouncing off sides
        if ball.right >= WIDTH:
            ball.right = WIDTH
            x_speed *= -1
        elif ball.left <= 0:
            ball.left = 0
            x_speed *= -1

        if ball.top <= 0:
            ball.top = 0
            y_speed *= -1

        if ball.bottom >= HEIGHT:
            game_state = "GAME_OVER"

    # Screen background
    SCREEN.fill("black")

    # Opening page when game start
    if game_state == "START":

        line3 = font.render("Welcome to PING!", True, "white")
        line4 = my_font.render("Enter the difficulty you would like", True, "white")
        line5 = my_font.render("Difficulty levels:", True, "cyan")
        line6 = my_font.render("Training level --> enter (t)", True, "white")
        line7 = my_font.render("Easy level --> enter (e)", True, "green")
        line8 = my_font.render("Medium level --> enter (m)", True, "orange")
        line9 = my_font.render("Hard level --> enter (h)", True, "red")
        line10 = my_font.render("Extreme level --> enter (x)", True, "purple")
        line11 = continue_font.render("Q to quit --> enter (q)", True, "grey")

        rect3 = line3.get_rect(center = (WIDTH//2, HEIGHT//2 - 240))
        rect4 = line4.get_rect(center=(WIDTH//2, HEIGHT//2 - 190))
        rect5 = line5.get_rect(center=(WIDTH//2, HEIGHT//2 - 115))
        rect6 = line6.get_rect(center=(WIDTH//2 , HEIGHT//2 - 25))
        rect7 = line7.get_rect(center=(WIDTH//2 - 20, HEIGHT//2 + 15))
        rect8 = line8.get_rect(center=(WIDTH//2 + 10, HEIGHT//2 + 55))
        rect9 = line9.get_rect(center=(WIDTH//2 - 15, HEIGHT//2 + 95))
        rect10 = line10.get_rect(center=(WIDTH//2 - 15, HEIGHT//2 +140))
        rect11 = line11.get_rect(center=(WIDTH//2 - 15, HEIGHT//2 +225))

        SCREEN.blit(line3, rect3)
        SCREEN.blit(line4, rect4)        
        SCREEN.blit(line5, rect5)
        SCREEN.blit(line6, rect6)
        SCREEN.blit(line7, rect7)
        SCREEN.blit(line8, rect8)
        SCREEN.blit(line9, rect9)
        SCREEN.blit(line10, rect10)
        SCREEN.blit(line11, rect11)

    # When player is playing the game
    elif game_state == "PLAYING":
        # Draw game elements
        if blocks_active:
            for block in blocks:
                pygame.draw.rect(SCREEN, "brown", block)

        pygame.draw.rect(SCREEN, "white", player_paddle)
        pygame.draw.circle(SCREEN, "white", (ball.x + 10, ball.y + 10), 10)

    # When player fails to bounce the ball
    elif game_state == "GAME_OVER":
        # Draw Game Over Text
        game_over_surface = font.render("GAME OVER", True, "white")
        text_rect = game_over_surface.get_rect(center=(WIDTH//2, HEIGHT//2 - 80))
        SCREEN.blit(game_over_surface, text_rect)

        # Calculate final score
        final_score = bounce

        display_score = font.render(f"Your final score is: {final_score} times", True, "white")
        display_place = display_score.get_rect(center = (WIDTH//2, HEIGHT//2))
        SCREEN.blit(display_score, display_place)

        # Message after player loses
        line1 = continue_font.render("Would you like to play again or quit?", True, "red")
        line2 = continue_font.render("Press (SPACE) to try again | Press (ENTER) to go back to menu | (Q TO QUIT)", True, "red")
        
        rect1 = line1.get_rect(center=(WIDTH//2, HEIGHT//2 +75))
        rect2 = line2.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))

        SCREEN.blit(line1, rect1)
        SCREEN.blit(line2, rect2)

    # When player wins
    elif game_state == "VICTORY":
        victory1 = font.render("VICTORY!", True, "yellow")
        victory2 = my_font.render("YOU DESTROYED ALL THE BLOCKS!", True, "yellow")
        victory3 = continue_font.render("Press (ENTER) to go back to menu or (Q to QUIT)", True, "red")
        victory1_rect = victory1.get_rect(center=(WIDTH//2, HEIGHT//2 - 125))
        victory2_rect = victory2.get_rect(center=(WIDTH//2, HEIGHT//2 - 75))
        victory3_rect = victory3.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
        SCREEN.blit(victory1, victory1_rect)
        SCREEN.blit(victory2, victory2_rect)
        SCREEN.blit(victory3, victory3_rect)

    pygame.display.update()
    CLOCK.tick(60)