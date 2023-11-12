# Draws a thousand robots in random places.
import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
rwidth = robot.get_width()
rheight = robot.get_height()
maxwidth = 640 - rwidth
maxheight = 480 - rheight
window.fill((0, 0, 0))
for i in range(1000):
    width = randint(0, maxwidth)
    height = randint(0, maxheight)
    window.blit(robot, (width, height))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()