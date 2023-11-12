import pygame
from random import randint
import math

class OwnGame:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Own Game")
        self.game_font = pygame.font.SysFont("Arial", 24)

        self.load_images()
        # Coins
        self.coins = []
        self.max_coins = 5
        self.velocity = 1

        # Robot
        self.k, self.l = ((640 - self.robot.get_width()) / 2, 480 - self.robot.get_height())
        self.to_right = False
        self.to_left = False

        # Monsters setting up the speed and frequencies of the wave
        self.m, self.n = (0, 0)
        self.monsters = []
        self.speed = 2
        self.horizontal_frequency = 0.05
        self.vertical_frequency = 0.05
        self.amplitude = 1
        self.max_monsters = 4

        self.clock = pygame.time.Clock()

        self.intro_message_shown = False
        self.running = False
        self.game_over = False
        self.paused = False
        self.points = 0
        self.last_monster_increase_time = 0
        self.monster_increase_interval = 60000  # 60 seconds in milliseconds


    @classmethod
    def load_images(cls):
        cls.coin = pygame.image.load("coin.png")
        cls.robot = pygame.image.load("robot.png")
        cls.monster = pygame.image.load("monster.png")

        cls.coin_width = cls.coin.get_width()
        cls.coin_height = cls.coin.get_height()
        cls.coin_max_width = 640 - cls.coin_width
        cls.coin_max_height = 480 - cls.coin_height

        cls.monster_width = cls.monster.get_width()
        cls.monster_height = cls.monster.get_height()

    def toggle_pause(self):
        self.paused = not self.paused

    def increase_max_monsters(self):
        self.max_monsters += 1
        self.last_monster_increase_time = pygame.time.get_ticks()

    def display_intro_message(self):
        self.window.fill((10, 170, 180))
        intro_text = self.game_font.render("Collect as many coins as you can while avoiding the monsters.", True, (255, 0, 0))
        info_text = self.game_font.render("With every minute in the game, the monsters increase by 1.", True, (255, 0, 0))
        start_text = self.game_font.render("Press Enter to start. Press Spacebar to pause during game play.", True, (255, 0, 0))
        intro_rect = intro_text.get_rect(center=(320, 160))
        info_rect = info_text.get_rect(center=(320, 200))
        start_rect = start_text.get_rect(center=(320, 240))
        self.window.blit(intro_text, intro_rect)
        self.window.blit(info_text, info_rect)
        self.window.blit(start_text, start_rect)

    def display_paused_message(self):
        game_fontp = pygame.font.SysFont("Arial", 32)
        pause_text = game_fontp.render("PAUSED", True, (0, 255, 0))
        text_rect = pause_text.get_rect(center=(320, 240))
        self.window.blit(pause_text, text_rect)

    def display_game_over_message(self):
        # Display "Game Over" message
        game_over_text = self.game_font.render("Game Over", True, (255, 0, 0))
        self.window.blit(game_over_text, (250, 200))

        # Display options to restart or exit
        restart_text = self.game_font.render("Press 'R' to Restart", True, (255, 0, 0))
        exit_text = self.game_font.render("Press 'Q' to Quit", True, (255, 0, 0))
        self.window.blit(restart_text, (250, 250))
        self.window.blit(exit_text, (250, 280))

    def update_game_state(self):
        current_time = pygame.time.get_ticks()

        if len(self.coins) < self.max_coins:
            x = randint(0, self.coin_max_width)
            y = randint(-self.coin_max_height - 520, 0)
            self.coins.append((x, y))

        if current_time - self.last_monster_increase_time >= self.monster_increase_interval:
            self.increase_max_monsters()

        if len(self.monsters) < self.max_monsters:
            self.m, self.n = (randint(0, 640 - self.monster_width), randint(-1000, 0))
            self.monsters.append((self.m, self.n))

        if not self.paused:
            self.window.fill((10, 170, 180))
            if self.game_over:
                self.display_game_over_message()

            else:
                for i in range(len(self.coins)):
                    x, y = self.coins[i]
                    self.window.blit(self.coin, (x, y))
                    y += self.velocity
                    self.coins[i] = (x, y)
                    if ((self.k + self.robot.get_width() >= x) and (self.k <= x + self.coin_width) and
                            (self.l + self.robot.get_height() >= y) and (self.l <= y + self.coin_height)):
                        self.points += 1
                        self.coins.pop(i)
                        break
                for i in range(len(self.monsters)):
                    m, n = self.monsters[i]
                    n += self.speed
                    m += self.amplitude * math.sin(self.horizontal_frequency * n)
                    m += self.amplitude * math.cos(self.vertical_frequency * n)
                    self.window.blit(self.monster, (m, n))
                    self.monsters[i] = (m, n)
                    if ((self.k + self.robot.get_width() >= m) and (self.k <= m + self.monster_width) and
                            (self.l + self.robot.get_height() >= n) and (self.l <= n + self.monster_height)):
                        self.game_over = True
                        break

                cleared = 0
                for j in self.coins:
                    if j[1] + self.coin_height >= 480:
                        cleared += 1
                if cleared == self.max_coins:
                    self.coins = []

                monster_count = 0
                for a in self.monsters:
                    if a[1] + self.monster_height >= 480:
                        monster_count += 1
                if monster_count == self.max_monsters:
                    self.monsters = []

                if self.to_right and not (self.k + self.robot.get_width() >= 640):
                    self.k += 2
                if self.to_left and not (self.k <= 0):
                    self.k -= 2

    def start_game(self):
        self.running = True
        self.intro_message_shown = True

    def run(self):
        clock = pygame.time.Clock()

        while not self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN  or event.key == pygame.K_KP_ENTER:
                        self.start_game()

            if not self.intro_message_shown:
                self.display_intro_message()

            pygame.display.flip()
            clock.tick(60)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.to_left = True
                    if event.key == pygame.K_RIGHT:
                        self.to_right = True
                    if event.key == pygame.K_r:
                        self.game_over = False
                        self.points = 0
                        self.coins = []
                        self.monsters = []
                    if event.key == pygame.K_q:
                        self.running = False
                    if event.key == pygame.K_SPACE:
                        self.toggle_pause()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.to_left = False
                    if event.key == pygame.K_RIGHT:
                        self.to_right = False

            self.update_game_state()

            if self.paused:
                self.display_paused_message()

            self.window.blit(self.robot, (self.k, self.l))
            text = self.game_font.render(f"Coins: {self.points}", True, (255, 0, 0))
            self.window.blit(text, (550, 5))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = OwnGame()
    game.run()
