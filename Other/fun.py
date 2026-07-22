import pygame
import sys

pygame.init()
WIDTH = 800
HEIGHT = 600
running = True


# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Game")
clock = pygame.time.Clock()

# Rectangle object and speed
rect = pygame.Rect(225, 450, 80, 15)
speed = 10


player_rect = pygame.Rect(100, 100, 40, 40)
barrier_rect = pygame.Rect(300, 200, 200, 50)
player_speed = 15

# Ball Properties
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2

speed_x = 5
speed_y = 4

bricks = [
        pygame.Rect(0, 0, 800, 25),
        pygame.Rect(200, 200, 55, 55),
        pygame.Rect(144, 200, 55, 55),
        pygame.Rect(440, 200, 55, 55),
        pygame.Rect(496, 200, 55, 55),
        pygame.Rect(552, 200, 55, 55)
]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    #Update ball position
    ball_x += speed_x
    ball_y += speed_y

    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)

    if ball_rect.colliderect(rect):
        if speed_y > 0 and ball_rect.bottom >= rect.top and ball_rect.bottom - speed_y <= rect.top:
            speed_y = -speed_y
            ball_y = rect.top - ball_radius

     # Bounce off Left and Right walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        speed_x = -speed_x 

    # Bounce off Top and Bottom walls
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        speed_y = -speed_y

    for brick in bricks:
        if ball_rect.colliderect(brick):
            overlap_left = ball_rect.right - brick.left
            overlap_right = brick.right - ball_rect.left
            overlap_top = ball_rect.bottom - brick.top
            overlap_bottom = brick.bottom - ball_rect.top

            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

            if min_overlap == overlap_top and speed_y > 0:
                speed_y = -speed_y  # Hit top of brick
                ball_y = brick.top - ball_radius
                break
            elif min_overlap == overlap_bottom and speed_y < 0:
                speed_y = -speed_y  # Hit bottom of brick
                ball_y = brick.bottom + ball_radius
                break
            elif min_overlap == overlap_left and speed_x > 0:
                speed_x = -speed_x  # Hit left side of brick
                ball_x = brick.left - ball_radius
                break
            elif min_overlap == overlap_right and speed_x < 0:
                speed_x = -speed_x  # Hit right side of brick
                ball_x = brick.right + ball_radius
                break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect.x -= speed
    if keys[pygame.K_RIGHT]:
        rect.x += speed

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 255, 0), (int(ball_x), int(ball_y)), ball_radius)

    pygame.draw.rect(screen, (255, 255, 255), rect)

    for brick in bricks:
        pygame.draw.rect(screen, (188, 74, 60), brick)


    pygame.display.flip()

    clock.tick(60)