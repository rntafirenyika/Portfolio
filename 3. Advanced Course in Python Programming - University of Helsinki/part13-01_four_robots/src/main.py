# Draws a robot in each of the four corners of the window.
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

window.fill((0, 0, 0))
window.blit(robot, (0, 0))
window.blit(robot, (640-width, 0))
window.blit(robot, (0, 480-height))
window.blit(robot, (640-width, 480-height))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()