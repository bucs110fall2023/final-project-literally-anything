import pygame
from src.controller import Controller

def main():
    """main loop
    """
    pygame.init()
    game_controller = Controller()
    game_controller.mainloop()

main()