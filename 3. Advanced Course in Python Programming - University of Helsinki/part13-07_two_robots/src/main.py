# An animation where two robots move back and forth to the left and right. 
# The lower robot should move at double the speed of the upper one.
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
x2 = 0
y = 50
velocity = 1
velocity2 = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x2, 150))
    pygame.display.flip()
    
    x += velocity
    x2 += velocity2
    if velocity > 0 and x+robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity
    if velocity2 > 0 and x2+robot.get_width() >= 640:
        velocity2 = -velocity2
    if velocity2 < 0 and x2 <= 0:
        velocity2 = -velocity2

    clock.tick(60)