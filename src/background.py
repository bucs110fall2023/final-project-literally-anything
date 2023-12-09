import pygame

class Background:
    """
    initializes background values,scales image and blits onto screen
    """
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
        """
        Moves the background to the left to create effect of a moving screen // resets x value after it goes offscreen 
        """
        self.x -= self.background_speed
        if self.x <= -self.width - self.bg_stretch:
            self.x = 0 
        
    def draw(self, screen):
        """
        Draws two background images onto screen to create a continous loop

        Args:
            screen (Surface): surface for background to be blitted onto
        """
        for i in range(1):
            screen.blit(self.image, (self.x, self.y))
            screen.blit(self.image, ((self.x + self.width + self.bg_stretch, self.y)))

        