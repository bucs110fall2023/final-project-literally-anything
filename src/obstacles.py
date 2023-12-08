import random
import pygame


class Obstacles(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = None
        self.obstacle = None
        self.obstacle_group = pygame.sprite.Group()

    def update(self):
        self.obstacle_group.update()

    def obstacle_select(self, obstacle_type):
        if obstacle_type == 0:
            self.obstacle_group.add(Asteroid(self.x, self.y))
        elif obstacle_type == 1:
            self.obstacle_group.add(Radar(self.x, self.y))

    def draw(self, screen):
        if self.obstacle:
            self.image = self.obstacle.image  # Set the image attribute to the obstacle's image
            self.obstacle.draw(screen)
        elif self.image is not None:
            screen.blit(self.image, (self.x, self.y))

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x,y)
        asteroid_heights = [500, 550, 600]
        self.image = pygame.transform.scale(pygame.image.load("assets/Asteroid.png"), (150,150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.centery = asteroid_heights[random.randrange(0,3)]
    def draw(self, screen):
        if self.image is not None:
            screen.blit(self.image, (self.x, self.y))
        print("drawing Ast")
    def update(self):
        self.x -= 1
        self.y = self.rect.centery
        print("updating Asteroid")

class Radar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.image = pygame.transform.scale(pygame.image.load("assets/Radar.png"), (200,200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, screen):
        if self.image is not None:
            screen.blit(self.image, (self.x, self.y))
        print("drawing radar")
    def update(self):
        self.x -= 1
        print("updating radar")
