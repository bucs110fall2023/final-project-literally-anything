import pygame
import random

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.asteroid = pygame.image.load("assets/Dino game Asteroid.png.png")
        self.radar = pygame.image.load("Dino game Radar-1.png.png")
        self.rect = self.image.get_rect()
        
class Asteroid(Obstacles):
    def __init__(self):
        asteroid_heights = [250, 290, 320]
        self.rect.centery = asteroid_heights[random.randrange(0,3)]
        self.index = 0
        self.counter = 0
        self.y_speed = 0
    def update(self):
        self.y_speed += 1
        self.rect.y += self.y_speed