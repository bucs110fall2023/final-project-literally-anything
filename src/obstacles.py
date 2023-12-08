import random
import pygame


class Obstacles(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = None
        self.obstacle = None

    def update(self):
        if self.obstacle:
            self.obstacle.update()

    def obstacle_select(self, obstacle_type):
        if obstacle_type == 0:
            self.obstacle = Asteroid(self.x, self.y)
        elif obstacle_type == 1:
            self.obstacle = Radar(self.x, self.y)

    def draw(self, screen):
        if self.obstacle:
            self.image = self.obstacle.image  # Set the image attribute to the obstacle's image
            self.obstacle.draw(screen)
        elif self.image is not None:
            screen.blit(self.image, (self.x, self.y))

class Asteroid(Obstacles):
    def __init__(self, x, y):
        super().__init__(x,y)
        asteroid_heights = [450, 500, 600]
        self.image = pygame.transform.scale(pygame.image.load("assets/Asteroid.png"), (200,200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.centery = asteroid_heights[random.randrange(0,3)]
    def draw(self, screen):
        if self.image is not None:
            screen.blit(self.image, (self.x, self.y))
        print("drawing Ast")
    def update(self):
        self.rect.x -= 5
        print("updating Asteroid")

class Radar(Obstacles):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.image = pygame.transform.scale(pygame.image.load("assets/Radar.png"), (250,250))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, screen):
        if self.image is not None:
            screen.blit(self.image, (self.x, self.y))
        print("drawing radar")
    def update(self):
        self.rect.x -= 5
        print("updating radar")
