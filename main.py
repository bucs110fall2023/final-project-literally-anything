import pygame
from src.controller import Controller

def main():
    """
    Initializes pygame, creates instance of controller object, calls mainloop through controller
    """
    pygame.init()
    game_controller = Controller()
    game_controller.mainloop()

if __name__ == '__main__':
    main()
