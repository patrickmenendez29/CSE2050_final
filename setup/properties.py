import pygame


class GameProperties:

    def __init__(self, cell_width=40, cell_height=40, rows=3, columns=8, gap=5, screen_size=(600, 600), caption=""):
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.rows = rows
        self.columns = columns
        self.gap = gap
        self.screen_size = screen_size
        self.caption = caption
        self.clock = pygame.time.Clock()

        pygame.display.set_caption(self.caption)
        self.screen = pygame.display.set_mode(self.screen_size)


class GridProperties:

    def __init__(self, game_properties: GameProperties):
        self.rows = game_properties.rows
        self.columns = game_properties.columns
        self.gap = game_properties.gap
        self.width = game_properties.cell_width
        self.height = game_properties.cell_height
