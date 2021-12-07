import pygame
from pygame.locals import *
from sys import exit
import pygame
import sys
import random
import subprocess

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Set the width and height of each cell

# Grid constants
N = 5
# GAP between each cell
GAP = 5

if __name__ == '__main__':
    pygame.init()

    run = True
    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                command = "python AhjaiyGame.py"
                subprocess.call(command)

        # Set the width and height of the screen [width, height]
        SCREEN_SIZE = (500, 500)
        WIDTH = SCREEN_SIZE[0] / N - GAP
        HEIGHT = SCREEN_SIZE[1] / N - GAP
        screen = pygame.display.set_mode(SCREEN_SIZE)
        # Set the title of the screen
        pygame.display.set_caption("Turtle Game")
        # Used to manage how fast the screen updates (fps)
        clock = pygame.time.Clock()
        # Set the screen background
        screen.fill(BLACK)
        n = 0
        for row in range(N):

            for column in range(N):

                if n % 2 == 0:
                    color = WHITE
                else:
                    color = BLACK
        # Draw a rectangle as [start_x, start_y, width, height]
        # or [surface, color, [start_x, start_y, width, height]]
                pygame.draw.rect(screen, color, [(WIDTH) * column +
                                         GAP, (GAP + HEIGHT) * row + GAP, WIDTH, HEIGHT])
                n += 1


        # Limit to 60 frames per second
        clock.tick(60)
        pygame.display.flip()
        pygame.display.update()

    pygame.quit()

