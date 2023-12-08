import pygame

class Background:
    def __init__(self,screen, width, height, x):
        self.x = x
        self.y = 780
        self.width = width 
        self.height = height
        self.background_speed = 5
        self.image = pygame.image.load("assets/Track.png")
        screen.blit(self.image, (0,self.y))
        
    def update(self):
        self.x -= self.background_speed
        if self.x <= -self.width:
            self.x = 0 
        
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x + self.width, self.y))

        