import pygame
import random

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, x, y, obstacle_type):
        super().__init__()
        self.x = x
        self.y = y
        self.obstacle_type = obstacle_type
        self.image = pygame.image.load(f"assets/{obstacle_type}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 5

class Asteroid(Obstacles):
    def __init__(self):
        super().__init__()
        asteroid_heights = [250, 290, 320]
        self.image = pygame.image.load("assets/Asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.centery = asteroid_heights[random.randrange(0,3)]
        self.y_speed = 0
    def update(self):
        self.y_speed += 1
        self.rect.y += self.y_speed
    def draw(self,screen):
        screen.blit(self.image, (self.x,self.y))