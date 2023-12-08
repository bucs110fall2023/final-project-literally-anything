import random
import pygame
from src.player import Player
from src.obstacles import Obstacles
from src.score import Score, Highscore
from src.background import Background

class Controller:
  
  def __init__(self):
    #setup pygame data
    self.screen = pygame.display.set_mode((1470, 956))
    self.screen.fill("white")
    self.width, self.height = pygame.display.get_window_size()
    x_pos = 50
    y_pos = 720
    self.player = Player(x_pos,y_pos)
    self.bg = Background(self.screen, self.width, self.height, 0)
    self.obstacle = Obstacles(1480,685)
    self.highscore = Highscore()
    self.state = "Menu"
    self.current_high = self.highscore.open_high()
  def mainloop(self):
    running = True
    #select state loop
    while running == True:
      if self.state == "Menu":
        self.menuloop()
      if self.state == "Game_start":
        self.gameloop()
      if self.state == "Game_over":
        self.gameoverloop()
  
  ### below are some sample loop states ###

  def menuloop(self):
    #event loop
    while self.state == "Menu":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            self.state = "Game_start"
      
      self.bg.draw(self.screen)
      font = pygame.font.Font(None, 48)
      msg = font.render("Click space to begin!", False, "black")
      self.screen.blit(msg, (575, 400))
      self.player.draw(self.screen)
      pygame.display.flip()
      #update data

      #redraw
      
  def gameloop(self):
    #event loop
    loop = 0
    duckloop = 0
    self.score = Score()
    while self.state == "Game_start":
      self.bg.update()
      key = pygame.key.get_pressed()
      if key[pygame.K_DOWN]:
        self.player.duck(duckloop)
        duckloop += 1
      else:
        self.player.stand()
      self.player.run(loop)
      loop += 1
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
            self.player.jump()

      #update data
      self.player.update()
      #redraw
      self.screen.fill("white")
      self.bg.draw(self.screen)
      self.player.draw(self.screen)
      self.score.update(self.current_high)
      font = pygame.font.Font(None, 48)
      if self.score.score >= self.current_high:
        msg = font.render("HIGHSCORE: " + str(self.score.score) + " SCORE:" + str(self.score.score), False, "black")
      else:
        msg = font.render("HI " + str(self.current_high) + " " + str(self.score.score), False, "black")
      self.screen.blit(msg, (50,50))
      spawn_rate = random.randint(0,100)
      if spawn_rate == 10:
        self.obstacle.obstacle_select(random.randint(0,2))
      self.obstacle.update()
      self.obstacle.draw(self.screen)
      # print(f'"Obstacle content:"{self.obstacle.obstacle_group}')
      collisions = pygame.sprite.spritecollide(self.player, self.obstacle.obstacle_group, False)
      if collisions:
        self.state = "Game_over"
        print("collision detected")
      pygame.display.flip()
    
  def gameoverloop(self):
    #event loop
    while self.state == "Game_over":
      # print("game over")
      
      if self.score.score > self.current_high:
        self.score.save_high(self.score.score)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            self.state = "Game_start"
            self.obstacle.obstacle_group.empty()
      font = pygame.font.Font(None, 48)
      msg = font.render("Click space to try again!", False, "black")
      self.screen.blit(msg, (575, 400))
      pygame.display.flip()
      #update data

      #redraw
