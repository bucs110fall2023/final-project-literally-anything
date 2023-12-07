import pygame
import random
from player import Player
from obstacles import Obstacles

class Controller:
  
  def __init__(self):
    #setup pygame data
    self.screen = pygame.display.set_mode()
    self.screen.fill("white")
    self.width, self.height = pygame.display.get_window_size()
    self.player = Player(50,700)
    self.obstacle = Obstacles(50,700, random.randrange(0,2))
    self.state = "Menu"
    
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
      
      font = pygame.font.Font(None, 48)
      msg = font.render("Click space to begin!", False, "black")
      self.screen.blit(msg, (50,50))
      self.player.draw(self.screen)
      pygame.display.flip()
      #update data

      #redraw
      
  def gameloop(self):
    #event loop
    loop = 0
    while self.state == "Game_start":
      self.player.run(loop)
      loop += 1
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
            self.player.jump()
            print("jump")
          elif event.key == pygame.K_DOWN:
            self.player.duck()
      #update data
      self.player.update()
      #redraw
      self.screen.fill("white")
      self.player.draw(self.screen)
      pygame.display.flip()
    
  def gameoverloop(self):
    #event loop
    while self.state == "Game_over":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
      #update data

      #redraw
