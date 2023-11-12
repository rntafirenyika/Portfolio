# An animation where robots fall from the sky randomly.
# When a robot reaches the ground, it starts moving to the left or to the right, and finaly disappears off the screen.
import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()
max_width = 640 - robot_width
max_height = 480 - robot_height

velocity = 1
clock = pygame.time.Clock()

robots = []

window.fill((0, 0, 0))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if len(robots) < 10:
        x = randint(0, max_width)
        y = randint(-max_height, 0)
        robots.append((x, y))

    for i in range(len(robots)):
        x, y = robots[i]
        window.blit(robot, (x, y))
        y += velocity
        if velocity > 0 and y + robot_height >= 480 and x >= max_width / 2:
            y = max_height
            x += velocity
        elif velocity > 0 and y + robot_height >= 480 and x < max_width / 2:
            y = max_height
            x -= velocity
        robots[i] = (x, y)
    
    cleared = 0    
    for j in robots:
        if j[0] + robot_width < 0 or j[0] - robot_width > 640:
            cleared += 1
    if cleared == 10:
            robots = []

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
