import pygame
from setup.properties import GameProperties, GridProperties
from constants import colors
from ui.grid import Grid, Cell

from game.gameobjects import Queen
from algorithms.nqueens import is_cell_valid, get_solution
import thorpy


class GameDriver:

    def __init__(self, properties: GameProperties, grid_size, gap):
        pygame.display.set_caption("N Queens")

        self.properties = properties
        self.grid_properties = GridProperties(self.properties)
        self.run = True
        self.offset = 100
        self.screen_size = (500, 500 + self.offset)
        self.grid_size = grid_size
        self.gap = gap
        self.parent = None

        self.screen = None
        self.grid = None
        self.game_objects = []
        self.queen_count = 0
        self.game_is_won = False
        self._load_game(self.grid_size)
        self.board = None
        pass

    def de_init(self):
        self.game_is_won = False
        self.grid.reset()

    def _load_game(self, n):
        pygame.init()
        self.grid_size = n
        self.grid = Grid(self.grid_size)
        # Set the width and height of the screen [width, height]
        self.width = self.screen_size[0] / self.grid_size - self.gap
        self.height = (self.screen_size[1] - self.offset) / self.grid_size - self.gap
        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen.fill(colors.BLACK)

        fill_start = (0, 0), (1, 0)
        fill_end = (0, 1), (1, 1)
        self.background = pygame.draw.rect(self.screen, colors.BLACK, [0, 0, self.screen_size[0],
                                                      self.offset])
        self.gradient_rect(self.screen, colors.WHITE, colors.BLACK, self.background, fill_start, fill_end)
        self.draw_grid()
        self.display_status_bar()

        #self.game_menu.display_menu()

    def start(self, n):
        self.grid_size = n
        self._load_game(n)
        self.board = self.grid.get_board()
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
        n = 1
        for row in range(self.grid_size):

            for column in range(self.grid_size):

                if n == 1:
                    color = colors.WHITE
                else:
                    color = colors.BLACK

                # Draw a rectangle as [start_x, start_y, width, height]
                # or [surface, color, [start_x, start_y, width, height]]
                start_x = self.width * column + self.gap
                start_y = ((self.gap + self.height) * row + self.gap) + self.offset
                pygame.draw.rect(self.screen, color, [start_x, start_y, self.width,
                                                      self.height])
                new_cell = Cell(start_x, start_y, self.width, self.height)
                self.grid.insert_cell(new_cell, row, column)

                n *= -1
            if self.grid_size % 2 == 0:
                n *= -1

    def update_ui(self):
        if self.game_is_won:
            self.label_text.set_text("Congratulations, you win!")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_click()
            self.status_bar_menu.blit_and_update()
            self.status_bar_menu.react(event)


    def _play_sound(self, path):
        sound = pygame.mixer.Sound(path)
        pygame.mixer.Sound.play(sound)

    def _handle_click(self):
        left, middle, right = pygame.mouse.get_pressed()
        if left and not self.game_is_won:
            pos = pygame.mouse.get_pos()
            if pos[1] < self.offset:
                return
            x, y = self.grid.get_cell_position(pos[0], pos[1])

            if is_cell_valid(self.board, x, y):
                self.handle_successful_queen(x, y)
                self._play_sound("game/assets/bell.wav")
            else:
                self._play_sound("game/assets/wrong.wav")
            if self.queen_count == self.grid_size:
                self.game_is_won = True
                self._play_sound("game/assets/victory.wav")

            print(self.board)

    def handle_successful_queen(self, x, y):
        queen = Queen(self)
        queen.place_object(self.grid.cells[x][y].get_center())
        self.game_objects.append(queen)
        print("cell (%s, %s) now has a queen" % (x, y))
        self.grid.cells[x][y].toggle()
        print(self.grid.cells[x][y].get_value())
        self.board[x][y] = 1
        self.queen_count += 1

    def gradient_rect(self, screen, color1, color2, target_rect, fill_start, fill_end):
        """ Draw a gradient filled rectangle covering target_rect """

        bitmap = pygame.Surface((2, 2))  # a 2x2 bitmap
        # a line requires x1, y1, x2, y2
        pygame.draw.line(bitmap, color1, *fill_start)  # start color line.
        pygame.draw.line(bitmap, color2, *fill_end)  # end color line
        color_rect = pygame.transform.smoothscale(bitmap, (target_rect.width, target_rect.height))  # stretch!
        screen.blit(color_rect, target_rect)

    def display_status_bar(self):
        thorpy.set_theme("human")
        # declaration of some ThorPy elements ...
        self.restart_button = thorpy.make_button("Restart", func=self._restart)
        self.quit_button = thorpy.make_button("Quit", func=self._quit)
        self.solve_button = thorpy.make_button("Solve", func=self._solve)
        self.help_button = thorpy.make_button("Help", func=self._help)
        self.label_text = thorpy.make_text("Welcome to N Queens by Patrick", 22,  (0,0,0))
        group_box = thorpy.make_group(elements=[
            self.restart_button,
            self.quit_button,
            self.solve_button,
            self.help_button,

        ])

        self.status_bar = group_box
        box = thorpy.Box(elements=[self.status_bar, self.label_text])
        # we regroup all elements on a menu, even if we do not launch the menu
        self.status_bar_menu = thorpy.Menu(box)
        # important : set the screen as surface for all elements
        for element in self.status_bar_menu.get_population():
            element.surface = self.screen
        # use the elements normally...
        box.set_topleft((0, 0))
        box.blit()
        box.update()
        thorpy.theme.set_default_theme_as_current()

    def _quit(self):
        thorpy.functions.quit_func()
        pass

    def _restart(self):
        self.queen_count = 0
        self.game_is_won = False
        self.parent.display_menu()

    def print_board(self):
        board = []
        for row in range(self.grid_size):
            board.append([])
            for col in range(self.grid_size):
                board[row].append(0)
        print(board)
        board = get_solution(board, 0)
        if not board:
            self.label_text.set_text("There is no solution to this game!")
            return
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == 1:
                    self.handle_successful_queen(x, y)


    def _solve(self):
        self.queen_count = 0
        self.draw_grid()
        self.display_status_bar()
        self.print_board()


    def _help(self):
        pass
