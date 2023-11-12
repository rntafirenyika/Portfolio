# Draws a hundred robots, ten rows with ten robots in each row.
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))
width = 40
iheight = 100
iwidth = 50
for i in range(10):
    for j in range(10):
        window.blit(robot, (iwidth + (j*width), iheight))
    iheight += 20
    iwidth += 10

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()