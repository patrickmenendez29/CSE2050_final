import pygame
from setup.properties import GameProperties, GridProperties
from constants import colors


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
        pass

    def classic(self):
        pygame.init()

        while self.run:

            self.update_ui()

            self.screen = pygame.display.set_mode(self.screen_size)
            # Set the title of the screen
            # Used to manage how fast the screen updates (fps)
            clock = pygame.time.Clock()
            # Set the screen background
            self.screen.fill(colors.BLACK)
            self.draw_grid()
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
                pygame.draw.rect(self.screen, color, [self.width * column +
                                                      self.gap, (self.gap + self.height) * row + self.gap, self.width,
                                                      self.height])
                n += 1
            n += 1

    def update_ui(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                left, middle, right = pygame.mouse.get_pressed()
                if left:
                    pos = pygame.mouse.get_pos()
                    print(pos)
