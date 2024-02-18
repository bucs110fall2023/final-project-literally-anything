import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Initializes the player, its position, images, hitbox, and other constants

        Args:
            x (int): x position of the player 
            y (int): y poisition of the player
        """
        super().__init__()
        self.x = x
        self.y = y
        self.ducky = self.y + 40
        self.standing = pygame.image.load("assets/Dino_sprites/DinoStart.png")
        self.jumping = pygame.image.load("assets/Dino_sprites/DinoJump.png")
        self.running = [pygame.image.load("assets/Dino_sprites/DinoRun1.png"), pygame.image.load("assets/Dino_sprites/DinoRun2.png")]
        self.ducking = [pygame.image.load("assets/Dino_sprites/DinoDuck1.png"), pygame.image.load("assets/Dino_sprites/DinoDuck2.png")]
        self.image = self.jumping
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
        self.gravity = .6
        self.groundconstant = y
        
    def run(self, loop_count):
        """
        Controls the running animation of the player by switching between 2 sprites based on loop_count

        Args:
            loop_count (int): the amount of times that the game loop is ran
        """
        self.is_running = True
        self.rect = self.image.get_rect()
        self.rect.x = self.x - 50
        self.rect.y = self.y 
        if self.is_running == True:
            if loop_count % 8 == 0 and self.in_air == False and self.is_ducking == False:
                self.current_image = (self.current_image) % 2
                self.image = self.running[self.current_image]
                self.current_image += 1
            
        
    def jump(self):
        """
        Initializes jumping of player // switches image of player and hitbox
        """
        if self.is_ducking == False:
            self.is_jumping = True 
            self.image = self.jumping     
            self.rect = self.image.get_rect()
            self.rect.x = self.x - 50
            self.rect.y = self.y
        
    def duck(self, loop):
        """
        Handles the logic of ducking and animating sprite running while ducking

        Args:
            loop (int): used to track amount of times gameloop is ran for ducking animation
        """
        if self.is_jumping == False:
            self.is_ducking = True
            if self.is_ducking == True:
                if loop % 8 == 0:
                    self.current_image = (self.current_image) % 2
                    self.image = self.ducking[self.current_image]
                    self.current_image += 1

    def stand(self):
        """
        Used to overide sprite ducking
        """
        self.is_ducking = False
        
        
    def update(self):
        """
        Handles jumping logic and hitboxes
        """
        if self.is_jumping == True:
            self.in_air = True
            if self.y > self.max_height:
                self.y -= self.jump_height
                self.jump_height -= self.gravity
            else: #precaution to not pass max_height (not really needed)
                self.is_jumping = False
                self.jump_height = 0
        if not self.is_jumping and self.y < 700: #also precaution
            self.y += self.jump_height
            self.jump_height += self.gravity
            self.rect.y = self.y - 100
        if self.y >= self.groundconstant:
            self.is_jumping = False
            self.in_air = False
            self.y = self.groundconstant
            self.jump_height = 15
        if self.is_ducking:
            self.rect.y = self.y + 50
        if not self.is_ducking:
            self.rect = self.image.get_rect(topleft=(self.x - 30 , self.y - 50))
    
    def draw(self, screen):
        """
        Blits the player sprite onto the screen based on whether it is ducking or not

        Args:
            screen (Surface): surface of the game 
        """
        if self.is_ducking:
            screen.blit(self.image, (self.x, self.ducky))
        else:
            screen.blit(self.image, (self.x, self.y))
            
        