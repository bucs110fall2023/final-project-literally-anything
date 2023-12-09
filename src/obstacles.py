import random
import pygame

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Initializes obstacles

        Args:
            x (int): initial x value of obstacles
            y (int): initial y value of obstacles
        """
        # super().__init__()
        self.x = x
        self.y = y
        self.image = None
        self.obstacle = None
        self.obstacle_group = pygame.sprite.Group()

    def update(self):
        """updates the obstacles
        """
        self.obstacle_group.update()

    def obstacle_select(self, obstacle_type):
        """selects the type of obstacle

        Args:
            obstacle_type (int): an integer 0 or 1 that determines the obstacle type
        """
        if obstacle_type == 0:
            self.obstacle_group.add(Asteroid(self.x, self.y))
        elif obstacle_type == 1:
            self.obstacle_group.add(Radar(self.x, self.y))
        # print(f'"number of sprites"{len(self.obstacle_group.sprites())}')

    def draw(self, screen):
        """draws the obstacles

        Args:
            screen (surface): the surface to draw on
        """
        for i in self.obstacle_group:
            i.draw(screen)

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """initializes asteroid obstacles

        Args:
            x (int): initial x position
            y (int): initial y potion
        """
        super().__init__()
        asteroid_heights = [685, 690, 700, 750]
        self.image = pygame.transform.scale(pygame.image.load("assets/Asteroid.png"), (130,130))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.centery = asteroid_heights[random.randrange(0,4)]
    def draw(self, screen):
        """draws the asteroids

        Args:
            screen (surface): the surface to draw the asteroids
        """
        if self.image is not None:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        # print("drawing Ast")
    def update(self):
        """Updates the location of the asteroids and deletes any off screen
        """
        self.rect.x -= 8
        if self.rect.x <= -50:
            self.kill()
        # print("updating Asteroid")


class Radar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """initializes the radar obstacles

        Args:
            x (int): initial x position of obstacle
            y (int): initial y position of obstacle
        """
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/Radar.png"), (150,150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, screen):
        """draws the radars

        Args:
            screen (surface): the surface the radars are drawn on
        """
        if self.image is not None:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        # print("drawing radar")
    def update(self):
        """updates the location of the radar and deletes any that are off the screen
        """
        self.rect.x -= 7
        if self.rect.x <= -50:
            self.kill()
        # print("updating radar")
