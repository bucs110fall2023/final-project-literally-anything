import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.standing = pygame.image.load("assets/Dino_sprites/DinoStart.png")
        self.jumping = pygame.image.load("assets/Dino_sprites/DinoJump.png")
        self.running = [pygame.image.load("assets/Dino_sprites/DinoRun1.png"), pygame.image.load("assets/Dino_sprites/DinoRun2.png")]
        self.ducking = [pygame.image.load("assets/Dino_sprites/DinoDuck1.png"), pygame.image.load("assets/Dino_sprites/DinoDuck2.png")]
        self.image = self.standing
        self.is_running = False
        self.is_jumping = False
        self.is_ducking = False
        self.current_image = 0
        self.rect = self.image.get_rect()
        
    def run(self, loop_count):
        if loop_count % 5 == 0:
            self.current_image = (self.current_image) % 2
            self.image = self.running[self.current_image]
            self.current_image += 1
            
        
    def jump(self):
        self.image = self.jumping
        
    def duck(self):
        self.image = self.ducking[0]
        
    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        