import pygame
import random

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, x, y, obstacle_type):
        super().__init__()
        self.x = x
        self.y = y
        self.obstacle_type = obstacle_type

    def update(self):
        self.rect.x -= 5

    def obstacle_select(self):
        if self.obstacle_type == 0:
            Asteroid(self.x, self.y)
        elif self.obstacle_type == 1:
            Radar(self.x, self.y)
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Asteroid(Obstacles):
    def __init__(self, x, y):
        super().__init__(x,y, obstacle_type=0)
        asteroid_heights = [250, 290, 320]
        self.image = pygame.image.load("assets/Asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.centery = asteroid_heights[random.randrange(0,3)]

class Radar(Obstacles):
    def __init__(self, x, y):
        super().__init__(x,y, obstacle_type=1)
        self.image = pygame.image.load("assets/Radar.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y