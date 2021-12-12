import pygame
from setup.properties import GameProperties, GridProperties
from constants import colors
from ui.grid import Grid, Cell

from game.gameobjects import Queen
from algorithms.nqueens import is_cell_valid, get_solution
import thorpy
import webbrowser


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

    # @desc: reset the instance and game status (game is no longer won)
    # @params: None
    # @returns: None
    def de_init(self):
        self.game_is_won = False
        self.grid.reset()

    # @desc: load the scene of the game (this code is only run once)
    # @params:
    #   n: size of the grid
    # @returns: None
    def _load_game(self, n):
        pygame.init()
        self.grid_size = n
        self.grid = Grid(self.grid_size)
        # Set the width and height of the screen [width, height]
        self.width = self.screen_size[0] / self.grid_size - self.gap
        self.height = (self.screen_size[1] - self.offset) / self.grid_size - self.gap
        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen.fill(colors.BLACK)

        self.background = pygame.draw.rect(self.screen, colors.BLACK, [0, 0, self.screen_size[0],
                                                                       self.offset])
        fill_start = (0, 0), (1, 0)
        fill_end = (0, 1), (1, 1)
        self.gradient_rect(self.screen, colors.WHITE, colors.BLACK, self.background, fill_start, fill_end)
        self.draw_grid()
        self.display_status_bar()

        # self.game_menu.display_menu()

    # @desc: main code for the driver class
    # @params:
    #   n: grid size (int)
    # @returns: None
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

    # @desc: function that draws the board
    # @params: None
    # @returns: None
    def draw_grid(self):
        # n alternates cell color (white or black)
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

            # alternate current color each row if the board is even
            if self.grid_size % 2 == 0:
                n *= -1

    # @desc: updates the UI (runs every frame)
    # @params: None
    # @returns: None
    def update_ui(self):
        # check if the game has been won yet
        if self.game_is_won:
            self.label_text.set_text("Congratulations, you win!")
        # check if any even has happened
        for event in pygame.event.get():
            # close the game if pygame is closed
            if event.type == pygame.QUIT:
                exit(0)
            # user made a left click
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_click()
            # update the status bar and add it to the game (so that it checks for updates)
            self.status_bar_menu.blit_and_update()
            self.status_bar_menu.react(event)

    # @desc: play a sound
    # @params:
    #   path: String that points to a .wav file
    # @returns: None
    def _play_sound(self, path):
        sound = pygame.mixer.Sound(path)
        pygame.mixer.Sound.play(sound)

    # @desc: handle when a user makes a left click
    # @params: None
    # @returns: None
    def _handle_click(self):
        # get the pressed instance
        left, middle, right = pygame.mouse.get_pressed()
        # if the click was indeed a left click and the game has not been won yet:
        if left and not self.game_is_won:
            # get the x,y clicked position
            pos = pygame.mouse.get_pos()
            if pos[1] < self.offset:
                return
            x, y = self.grid.get_cell_position(pos[0], pos[1])
            # check if the cell is valid and play the respective sound
            if is_cell_valid(self.board, x, y):
                self.handle_successful_queen(x, y)
                self._play_sound("game/assets/bell.wav")
            else:
                self._play_sound("game/assets/wrong.wav")
            if self.queen_count == self.grid_size:
                self.game_is_won = True
                self._play_sound("game/assets/victory.wav")


    # @desc: function that runs if a queen can be sucessfully placed
    # @params:
    #   x: row for the queen to be placed
    #   y: column for the queen to be placed
    # @returns: None
    def handle_successful_queen(self, x, y):
        queen = Queen(self)
        queen.place_object(self.grid.cells[x][y].get_center())
        self.game_objects.append(queen)
        self.grid.cells[x][y].toggle()
        self.board[x][y] = 1
        self.queen_count += 1

    # @desc: draw a gradient in the top side of the screen (black and white)
    # @params:
    #   screen: screen in which the drawn rectangle is to be placed
    #   color1: start color (white)
    #   color2: end color (black)
    #   target_rect: rectangle in which the gradient is to be drawn
    #   fill_start: location in which the gradient starts
    #   fill_end: location in which the gradient ends
    # @returns: None
    def gradient_rect(self, screen, color1, color2, target_rect, fill_start, fill_end):
        """ Draw a gradient filled rectangle covering target_rect """

        bitmap = pygame.Surface((2, 2))  # a 2x2 bitmap
        # a line requires x1, y1, x2, y2
        pygame.draw.line(bitmap, color1, *fill_start)  # start color line.
        pygame.draw.line(bitmap, color2, *fill_end)  # end color line
        color_rect = pygame.transform.smoothscale(bitmap, (target_rect.width, target_rect.height))  # stretch!
        screen.blit(color_rect, target_rect)

    # @desc: display a status bar in game
    # @params: None
    # @returns: None
    def display_status_bar(self):

        thorpy.set_theme("human")
        # declaration of some ThorPy elements ...
        self.restart_button = thorpy.make_button("Restart", func=self._restart)
        self.quit_button = thorpy.make_button("Quit", func=self._quit)
        self.solve_button = thorpy.make_button("Solve", func=self._solve)
        self.help_button = thorpy.make_button("Help", func=self._help)
        self.label_text = thorpy.make_text("Welcome to N Queens by Patrick", 22, (0, 0, 0))
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

    # @desc: quit the game
    # @params: None
    # @returns: None
    def _quit(self):
        thorpy.functions.quit_func()
        pass

    # @desc: restart the game
    # @params: None
    # @returns: None
    def _restart(self):
        self.queen_count = 0
        self.game_is_won = False
        self.parent.display_menu()

    # @desc: Display the current board (after being solved)
    # @params: None
    # @returns: None
    def print_board(self):
        board = []
        # create an empty board the size of the current one
        for row in range(self.grid_size):
            board.append([])
            for col in range(self.grid_size):
                board[row].append(0)
        # try to get a solution
        board = get_solution(board, 0)
        # if the game cannot be solved, alert the user
        if not board:
            self.label_text.set_text("There is no solution to this game!")
            return
        # if the game can be solved, alert the user and display the solution
        self.label_text.set_text("Game solved!")
        # place a queen every time there is a 1 in the solved board
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == 1:

                    self.handle_successful_queen(x, y)

    # @desc: solve the current board for the user
    # @params: None
    # @returns: None
    def _solve(self):
        self.queen_count = 0
        self.draw_grid()
        self.display_status_bar()
        self.print_board()

    # @desc: open a link that describes how the game works
    # @params: None
    # @returns: None
    def _help(self):
        webbrowser.open("https://thimbleby.gitlab.io/algorithm-wiki-site/wiki/n-queens/")
        pass
