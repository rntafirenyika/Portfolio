# A game where asteroids fall from the sky. The player moves a robot left and right and tries to collect the falling rocks.
# The player gets a point for each asteroid collected, and the points total is shown at the top of the window.
# The game ends when the player misses an asteroid.
import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Asteroids")
game_font = pygame.font.SysFont("Arial", 24)

robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")
rock_width = rock.get_width()
rock_height = rock.get_height()
rock_max_width = 640 - rock_width
rock_max_height = 480 - rock_height

to_right = False
to_left = False
to_up = False
to_down = False

k = (640 - robot.get_width()) / 2
l = 480 - robot.get_height()

velocity = 1
clock = pygame.time.Clock()

rocks = []

running = True
game_over = False
paused = False
points = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_r:
                game_over = False
                points = 0
                rocks = []
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_SPACE:
                paused = not paused

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

    if len(rocks) < 5:
        x = randint(0, rock_max_width)
        y = randint(-rock_max_height-520, 0)
        rocks.append((x, y))

    if not paused:
        window.fill((0, 0, 0))
        if game_over:
            # Display "Game Over" message
            game_over_text = game_font.render("Game Over", True, (255, 0, 0))
            window.blit(game_over_text, (250, 200))

            # Display options to restart or exit
            restart_text = game_font.render("Press 'R' to Restart", True, (255, 0, 0))
            exit_text = game_font.render("Press 'Q' to Quit", True, (255, 0, 0))
            window.blit(restart_text, (250, 250))
            window.blit(exit_text, (250, 280))
        else:
            for i in range(len(rocks)):
                x, y = rocks[i]
                window.blit(rock, (x, y))
                y += velocity
                rocks[i] = (x, y)
                if ((k + robot.get_width() >= x) and (k <= x + rock_width) and (l + robot.get_height() >= y) and (l <= y + rock_height)):
                    points += 1
                    rocks.pop(i)
                    break
                # Checking if a rock has been missed
                if y + rock_height >= 480:
                    game_over = True

        cleared = 0    
        for j in rocks:
            if j[1] + rock_height >= 480:
                cleared += 1
        if cleared == 5:
                rocks = []

        if to_right and not (k+robot.get_width() >= 640):
            k += 2
        if to_left and not(k <= 0):
            k -= 2
    if paused:
        # Display "PAUSED" message
        game_fontp = pygame.font.SysFont("Arial", 32)
        pause_text = game_fontp.render("PAUSED", True, (0, 255, 0))
        text_rect = pause_text.get_rect(center=(320, 240))
        window.blit(pause_text, text_rect)
    window.blit(robot, (k, l))
    text = game_font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (550, 5))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
