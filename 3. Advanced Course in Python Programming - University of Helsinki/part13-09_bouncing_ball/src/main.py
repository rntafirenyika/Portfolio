# An animation where a ball bounces from the edges of the window.
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

ball = pygame.image.load("ball.png")
x, y = (320, 240)

x_velocity = 2
y_velocity = 2
width = ball.get_width()
height = ball.get_height()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    x += x_velocity
    y += y_velocity
    if x + width >= 640 or x <= 0:
        x_velocity *= -1
    if y + height >= 480 or y <= 0:
        y_velocity *= -1

    clock.tick(60)
