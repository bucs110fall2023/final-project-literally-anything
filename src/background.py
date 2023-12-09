import pygame

class Background:
    def __init__(self,screen, width, height, x):
        self.x = x
        self.y = 0
        self.width = width 
        self.height = height
        self.bg_stretch = 1000
        self.background_speed = 7
        self.image = pygame.image.load("assets/spacebg.jpeg")
        self.image = pygame.transform.scale(self.image, (self.width + self.bg_stretch, self.height))
        screen.blit(self.image, (0,0))
        
    def update(self):
        self.x -= self.background_speed
        if self.x <= -self.width - self.bg_stretch:
            self.x = 0 
        
    def draw(self, screen):
        for i in range(1):
            screen.blit(self.image, (self.x, self.y))
            screen.blit(self.image, ((self.x + self.width + self.bg_stretch, self.y)))

        