import pygame
import random

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, x, y, obstacle_type):
        super().__init__()
        self.obstacle_type = obstacle_type
        self.image = pygame.image.load(f"assets/{obstacle_type}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 5

class Asteroid(Obstacles):
    def __init__(self, x, y, obstacle_type):
        super().__init__(x, y, obstacle_type)
        asteroid_heights = [250, 290, 320]
        self.image = pygame.image.load("assets/Asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.centery = asteroid_heights[random.randrange(0,3)]
        self.x_speed = 0
    def update(self):
        self.x_speed += 1
        self.rect.x += self.x_speed
    def draw(self,screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))

class Radar(Obstacles):
    def __init__(self, x, y, obstacle_type):
        super().__init__(x, y, obstacle_type)
        self.image = pygame.image.load("assests/Radar.png")
        self.react = self.image.get_rect()
        self.x_speed = 0
    def update(self):
        self.x_speed += 1
        self.rect.x += self.x_speed
    def draw(self,screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))