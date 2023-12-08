import random
import pygame


class Obstacles(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # super().__init__()
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
        #print(f'"number of sprites"{len(self.obstacle_group.sprites())}')

    def draw(self, screen):
        for i in self.obstacle_group:
            i.draw(screen)

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        asteroid_heights = [650, 700, 750]
        self.image = pygame.transform.scale(pygame.image.load("assets/Asteroid.png"), (150,150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.centery = asteroid_heights[random.randrange(0,3)]
    def draw(self, screen):
        if self.image is not None:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        # print("drawing Ast")
    def update(self):
        self.rect.x -= 10
        if self.rect.x <= -100:
            self.kill()
        # print("updating Asteroid")

class Radar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/Radar.png"), (200,200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, screen):
        if self.image is not None:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        # print("drawing radar")
    def update(self):
        self.rect.x -= 5
        if self.rect.x <= -100:
            self.kill()
        # print("updating radar")
