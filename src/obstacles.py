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

class Asteroid(Obstacles):
    def __init__(self, x, y):
        super().__init__(x, y)
        asteroid_heights = [250, 290, 320]
        self.asteroid_image = pygame.image.load("assets/Asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.centery = asteroid_heights[random.randrange(0,3)]
    def draw(self,screen):
        screen.blit(self.asteroid_image, (self.rect.x,self.rect.centery))

class Radar(Obstacles):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radar_image = pygame.image.load("assests/Radar.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self,screen):
        screen.blit(self.radar_image, (self.rect.x,self.rect.y))