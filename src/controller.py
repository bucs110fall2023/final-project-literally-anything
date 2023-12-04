import pygame
from player import Player
from obstacles import Obstacles

class Controller:
  
  def __init__(self):
    #setup pygame data
    self.screen = pygame.display.set_mode()
    self.screen.fill("white")
    self.width, self.height = pygame.display.get_window_size()
    self.player = Player(50,50)
    self.state = "Game_start"
    
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
        if event.type == pygame.K_SPACE:
          self.state = "Game_start"
      #update data

      #redraw
      
  def gameloop(self):
    #event loop
    while self.state == "Game_start":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE or pygame.K_UP:
            self.player.jump()
          elif event.key == pygame.K_DOWN:
            self.player.duck()
      #update data
      self.player.update()
      #redraw
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
