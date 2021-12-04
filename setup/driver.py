import pygame
from setup.properties import GameProperties, GridProperties
from constants import colors


class GameDriver:

    def __init__(self, properties: GameProperties):
        self.properties = properties
        self.grid_properties = GridProperties(self.properties)
        self.run = True
        pass

    def launch_game(self):
        pygame.init()
        self.game_did_launch()

        while self.run:
            self.update_game()
        pygame.quit()

    def update_game(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.run = False

    def game_did_launch(self):
        self.draw_grid()

    def draw_grid(self):
        print("Drawing grid")
        # Set the screen background
        self.properties.screen.fill(colors.WHITE)

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
