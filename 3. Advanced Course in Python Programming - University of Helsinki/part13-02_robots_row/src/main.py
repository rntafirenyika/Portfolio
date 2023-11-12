# Draws ten robots in a row.
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))
width = robot.get_width()
height = robot.get_height()

for i in range(10):
    window.blit(robot, (width + (i*width), height))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()