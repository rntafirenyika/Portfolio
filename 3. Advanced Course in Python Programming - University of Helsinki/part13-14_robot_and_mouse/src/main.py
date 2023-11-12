# The robot follows the mouse cursor so that the centre of the robot is always directly at the mouse cursor.
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")


target_x = 0
target_y = 0
robot_x = target_x
robot_y = target_y

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            target_x = event.pos[0]-robot.get_width()/2
            target_y = event.pos[1]-robot.get_height()/2

        if event.type == pygame.QUIT:
            exit(0)

    if robot_x > target_x:
        robot_x = target_x
    if robot_x < target_x:
        robot_x = target_x
    if robot_y > target_y:
        robot_y = target_y
    if robot_y < target_y:
        robot_y = target_y

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)