import pygame
from pygame.locals import *
from sys import exit
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Set the width and height of each cell
WIDTH = 40
HEIGHT = 40
# Grid constants
ROWS = 3
COLUMNS = 8
# GAP between each cell
GAP = 5

if __name__ == '__main__':
    pygame.init()
    # Set the width and height of the screen [width, height]
    SCREEN_SIZE = (365, 140)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    # Set the title of the screen
    pygame.display.set_caption("Turtle Game")
    # Used to manage how fast the screen updates (fps)
    clock = pygame.time.Clock()
