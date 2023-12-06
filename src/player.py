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
        self.jump_height = 15
        self.max_height = 550
        
    def run(self, loop_count):
        if loop_count % 8 == 0 and self.is_jumping == False:
            self.current_image = (self.current_image) % 2
            self.image = self.running[self.current_image]
            self.current_image += 1
            
        
    def jump(self):
        self.is_jumping = True
        self.image = self.jumping
        
    def duck(self):
        self.image = self.ducking[0]
        
    def update(self):
        if self.is_jumping == True:
            if self.y > self.max_height:
                self.y -= self.jump_height
                self.jump_height -= 1
                print("jumping")
        if self.y <= self.max_height:
            print("falling")
            self.y += self.jump_height
            self.jump_height += 1
        if self.y >= 700:
            self.y = 700
            self.is_jumping = False
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        