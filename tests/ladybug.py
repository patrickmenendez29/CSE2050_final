import pygame
from random import randint


class LadyBugGame:
    def __init__(self, w=365, h=140, cell_w=40, cell_h=40, rows=3, cols=8):
        self._screen = None
        self._lady_bug = None
        self._clock = pygame.time.Clock()
        self._background_color = (0, 0, 0)  # black rgb
        self._cell_background_color = (255, 255, 255)  # white rgb
        self._gap = 5
        self._window_width = w
        self._window_height = h
        self._cell_width = cell_w
        self._cell_height = cell_h
        self._grid_rows = rows
        self._grid_columns = cols
        rand_x = randint(1, self._grid_columns)
        rand_y = randint(1, self._grid_rows)
        self._bug_x = ((rand_x * self._cell_width) + (rand_x * self._gap)) - (self._cell_width / 2)
        self._bug_y = ((rand_y * self._cell_height) + (rand_y * self._gap)) - (self._cell_height / 2)

    def setup(self):
        pygame.init()

        # Set window size using a tuple
        self._screen = pygame.display.set_mode((self._window_width, self._window_height))
        # Set the window title
        pygame.display.set_caption("Lady Bug")
        # Load the bug image
        self._lady_bug = pygame.image.load('assets/lady_bug.png')
        self.draw_grid()

    def draw_grid(self):
        self._screen.fill(self._background_color)

        for row in range(self._grid_rows):
            for column in range(self._grid_columns):
                color = self._cell_background_color
                # Make rectangle as [start_x, start_y, width, height]
                # or [surface, color, [start_x, start_y, width, height]]
                pygame.draw.rect(self._screen, color, [(self._gap + self._cell_width) * column +
                                                       self._gap, (self._gap + self._cell_height) * row + self._gap,
                                           self._cell_width, self._cell_height])

    def place_bug(self):
        image_rect = self._lady_bug.get_rect()

        image_rect.center = (self._bug_x, self._bug_y)
        self._screen.blit(self._lady_bug, image_rect)

    def update_ui(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.draw_grid()
            self._clock.tick(60)  # set to 60 FPS
            self.place_bug()
            # flip allows only a portion of the screen to be updated instead of the entire area
            pygame.display.flip()

    def quit(self):
        pygame.quit()


if __name__ == '__main__':

    lady_bug_game = LadyBugGame()

    lady_bug_game.setup()
    lady_bug_game.update_ui()
    lady_bug_game.quit()