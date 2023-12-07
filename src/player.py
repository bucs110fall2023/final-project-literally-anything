import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.ducky = self.y - 50
        self.standing = pygame.image.load("assets/Dino_sprites/DinoStart.png")
        self.jumping = pygame.image.load("assets/Dino_sprites/DinoJump.png")
        self.running = [pygame.image.load("assets/Dino_sprites/DinoRun1.png"), pygame.image.load("assets/Dino_sprites/DinoRun2.png")]
        self.ducking = [pygame.image.load("assets/Dino_sprites/DinoDuck1.png"), pygame.image.load("assets/Dino_sprites/DinoDuck2.png")]
        self.image = self.standing
        self.is_running = False
        self.is_jumping = False
        self.is_ducking = False
        self.in_air = False
        self.current_image = 0
        self.current_duck = 0
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.jump_height = 15
        self.max_height = 450
        self.duckloop = 0
        
    def run(self, loop_count):
        self.is_running = True
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        if self.is_running == True:
            if loop_count % 8 == 0 and self.in_air == False and self.is_ducking == False:
                self.current_image = (self.current_image) % 2
                self.image = self.running[self.current_image]
                self.current_image += 1
            
        
    def jump(self):
        self.is_jumping = True
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image = self.jumping
        
    def duck(self, loop):
        self.is_ducking = True
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.ducky
        if self.is_ducking == True:
            if loop % 8 == 0:
                self.current_image = (self.current_image) % 2
                self.image = self.ducking[self.current_image]
                self.current_image += 1
            
    def stand(self):
        self.is_ducking = False
        
        
    def update(self):
        if self.is_jumping == True:
            self.in_air = True
            if self.y > self.max_height:
                self.y -= self.jump_height
                self.jump_height -= .6
            else: #precaution to not pass max_height (not really needed)
                self.is_jumping = False
                self.jump_height = 0
        if not self.is_jumping and self.y < 700: #also precaution
            self.y += self.jump_height
            self.jump_height += .6
        if self.y >= 700:
            self.is_jumping = False
            self.in_air = False
            self.y = 700
            self.jump_height = 15
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        