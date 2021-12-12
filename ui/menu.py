import thorpy
import pygame
from setup.driver import GameDriver


# @desc:
class Menu:

    def __init__(self, driver: GameDriver):
        self.driver = driver
        driver.parent = self
        pass

    # @desc:
    # @params:
    # @returns:
    def display_menu(self):
        thorpy.set_theme("human")
        button = thorpy.make_button("Start Game", func=self.process_input)
        self._input_field = thorpy.Inserter(name="Enter n: ", value="")

        group_box = thorpy.make_group(elements=[self._input_field])
        box = thorpy.Box(elements=[group_box, button])
        self._box = box
        self._input_field.enter()  # set focus for typing
        # You could put your box somewhere on the screen box.set_topleft((100, 100))
        box.center()  # or center it on the screen
        box.blit()
        box.update()
        thorpy.theme.set_default_theme_as_current()
        self._background = thorpy.Background(elements=[self._box], image="ui/chess.png")

        self._menu = thorpy.Menu(self._background)

        self._menu.play()

    # @desc:
    # @params:
    # @returns:
    def react(self, event):
        self._menu.react(event)

    # @desc:
    # @params:
    # @returns:
    def process_input(self):
        if self._input_field.get_value().title().isnumeric():
            grid_size = int(self._input_field.get_value().title())
        else:

            thorpy.launch_blocking_alert(title="Value Error",
            text="Please enter a valid, positive integer to start the game (0-99)",
            parent=self._background
            ) # for auto-unblitting)
            return 
        self._box.remove_all_elements()
        self._box.unblit()
        self._box.update()
        self._menu.refresh()

        pygame.display.update()
        self.driver.start(grid_size)
        self._menu.play()


