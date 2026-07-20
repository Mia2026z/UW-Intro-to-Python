import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball game")
CLOCK = pygame.time.Clock()

# Paddle
player_paddle = pygame.Rect(WIDTH//2, 425, 75, 15)

# Ball

ball = pygame.Rect(WIDTH//2, 50, 20, 20)
x_speed, y_speed = 4, 4

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:
        if player_paddle.left > 0:
            player_paddle.left -= 7

    if keys_pressed[pygame.K_RIGHT]:
        if player_paddle.right < WIDTH:
            player_paddle.right += 7


    ball.x += x_speed
    ball.y += y_speed

    if ball.right >= WIDTH:
        ball.right = WIDTH
        x_speed *= -1
    elif ball.left <= 0:
        ball.left = 0
        x_speed *= -1

    if ball.bottom >= HEIGHT:
        ball.bottom = HEIGHT
        y_speed *= -1
    elif ball.top <= 0:
        ball.top = 0
        y_speed *= -1


    SCREEN.fill("black")
    pygame.draw.rect(SCREEN, "white", player_paddle)

    pygame.draw.circle(SCREEN, "white", (ball.x + 10, ball.y + 10), 10) 

    pygame.display.update()
    CLOCK.tick(60)