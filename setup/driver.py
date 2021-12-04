import pygame
from setup.properties import GameProperties, GridProperties
from constants import colors


class GameDriver:

    def __init__(self, properties: GameProperties):
        self.properties = properties
        self.grid_properties = GridProperties(self.properties)
        pass

    def launch_game(self):
        pygame.init()
        self.draw_grid()

    def draw_grid(self):

        # Set the screen background
        self.properties.screen.fill(colors.BLACK)

        for row in range(self.properties.rows):
            for column in range(self.properties.columns):
                color = colors.WHITE
                # Draw a rectangle as [start_x, start_y, width, height]
                # or [surface, color, [start_x, start_y, width, height]]
                pygame.draw.rect(self.properties.screen, color,
                                 [
                                     (
                                                 self.properties.gap + self.properties.cell_width) * column + self.properties.gap,
                                     (
                                                 self.properties.gap + self.properties.cell_height) * row + self.properties.gap,
                                     self.properties.cell_width,
                                     self.properties.cell_height
                                 ]
                                 )
