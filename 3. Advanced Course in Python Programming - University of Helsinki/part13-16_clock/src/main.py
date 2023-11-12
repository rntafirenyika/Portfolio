# Displays a clock face which displays the system time.
import pygame
import time
import math

pygame.init()
display = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    current_time = time.strftime("%H:%M:%S")
    pygame.display.set_caption(current_time)

    hours = int(current_time.split(":")[0])
    minutes = int(current_time.split(":")[1])
    seconds = int(current_time.split(":")[2])

    sx = 320 + math.cos((seconds - 15) * 2 * math.pi / 60) * 180
    sy = 240 + math.sin((seconds - 15) * 2 * math.pi / 60) * 180
    mx = 320 + math.cos((minutes - 15) * 2 * math.pi / 60) * 180
    my = 240 + math.sin((minutes - 15) * 2 * math.pi / 60) * 180
    hx = 320 + math.cos((hours % 12 + minutes / 60-3) * 2 * math.pi / 12) * 140
    hy = 240 + math.sin((hours % 12 + minutes / 60-3) * 2 * math.pi / 12) * 140

    display.fill((0, 0, 0))
    pygame.draw.circle(display, (255, 0, 0), (640/2, 480/2), 200)
    pygame.draw.circle(display, (0, 0, 0), (640/2, 480/2), 195)
    pygame.draw.circle(display, (255, 0, 0), (640/2, 480/2), 10)
    pygame.draw.line(display, (0, 0, 255), (hx, hy), (640/2, 480/2), 4)
    pygame.draw.line(display, (0, 0, 255), (mx, my), (640/2, 480/2), 3)
    pygame.draw.line(display, (0, 0, 255), (sx, sy), (640/2, 480/2), 1)

    pygame.display.flip()
    clock.tick(1)