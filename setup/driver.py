import pygame
from setup.properties import GameProperties, GridProperties
from constants import colors
from ui.grid import Grid, Cell
from game.gameobjects import Queen
from algorithms.nqueens import is_cell_valid, get_solution


class GameDriver:

    def __init__(self, properties: GameProperties, grid_size, gap):
        pygame.display.set_caption("N Queens")

        self.properties = properties
        self.grid_properties = GridProperties(self.properties)
        self.run = True
        self.screen_size = (500, 500)
        self.grid_size = grid_size
        self.gap = gap

        # Set the width and height of the screen [width, height]
        self.width = self.screen_size[0] / grid_size - gap
        self.height = self.screen_size[1] / grid_size - gap
        self.screen = None
        self.grid = Grid(self.grid_size)
        self.game_objects = []
        self.queen_count = 0
        self.game_is_won = False
        pass

    def _load_game(self):
        pygame.init()

        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen.fill(colors.BLACK)
        self.draw_grid()

    def classic(self):
        self._load_game()

        while self.run:
            self.update_ui()

            # Set the title of the screen
            # Used to manage how fast the screen updates (fps)
            clock = pygame.time.Clock()
            # Set the screen background

            # Limit to 60 frames per second
            clock.tick(60)
            pygame.display.flip()
            pygame.display.update()

        pygame.quit()

    def draw_grid(self):
        n = 0
        for row in range(self.grid_size):

            for column in range(self.grid_size):

                if n % 2 == 0:
                    color = colors.WHITE
                else:
                    color = colors.BLACK

                # Draw a rectangle as [start_x, start_y, width, height]
                # or [surface, color, [start_x, start_y, width, height]]
                start_x = self.width * column + self.gap
                start_y = (self.gap + self.height) * row + self.gap
                pygame.draw.rect(self.screen, color, [start_x, start_y, self.width,
                                                      self.height])
                new_cell = Cell(start_x, start_y, self.width, self.height)
                self.grid.insert_cell(new_cell, row, column)

                n += 1
            n += 1

    def update_ui(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_click()

    def _handle_click(self):
        left, middle, right = pygame.mouse.get_pressed()
        if left:
            pos = pygame.mouse.get_pos()
            x, y = self.grid.get_cell_position(pos[0], pos[1])
            board = self.grid.get_board()
            for row in board:
                print(row)
            print()
            if is_cell_valid(board, x, y):
                self._handle_successful_queen(x, y)
            if self.queen_count == self.grid_size:
                self.game_is_won = True

    def _handle_successful_queen(self, x, y):
        queen = Queen(self)
        queen.place_object(self.grid.cells[x][y].get_center())
        self.grid.cells[x][y].toggle()
        self.queen_count += 1
