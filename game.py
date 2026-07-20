import pygame
import sys

pygame.init()

bounce = 0

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
            if game_state == "START":
                if event.key == pygame.K_RETURN:
                    game_state = "PLAYING"

            elif game_state == "GAME_OVER":
                if event.key == pygame.K_RETURN:
                    ball.x, ball.y = WIDTH//2 - 10, 50
                    x_speed, y_speed = 4, 4
                    player_paddle = pygame.Rect(WIDTH//2 - 37, 425, 75, 15)
                    game_state = "PLAYING"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


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

    SCREEN.fill("black")

    if game_state == "START":
        start_surface = font.render("bouncing ball", True, "white")
        start_rect = start_surface.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
        SCREEN.blit(start_surface, start_rect)

        starting_message = font.render("Press ENTER to start", True, "white")
        
        starting_location = starting_message.get_rect(center = (WIDTH//2, HEIGHT//2 - 100))
        SCREEN.blit(starting_message, starting_location)


    elif game_state == "PLAYING":
        # Draw game elements
        pygame.draw.rect(SCREEN, "white", player_paddle)
        pygame.draw.circle(SCREEN, "white", (ball.x + 10, ball.y + 10), 10)


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
        
        # Split message into two separate lines to avoid using '\n'
        line1 = continue_font.render("Would you like to play again or quit?", True, "red")
        line2 = continue_font.render("(PRESS ENTER TO TRY AGAIN) or (Q TO QUIT)", True, "red")
        
        rect1 = line1.get_rect(center=(WIDTH//2, HEIGHT//2 +75))
        rect2 = line2.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
        
        SCREEN.blit(line1, rect1)
        SCREEN.blit(line2, rect2)


    pygame.display.update()
    CLOCK.tick(60)