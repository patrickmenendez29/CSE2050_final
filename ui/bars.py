import thorpy
import pygame


class StatusBar:

    def __init__(self):
        self.restart_button = None
        self.quit_button = None
        self.solve_button = None
        self.help_button = None

    def display_menu(self):
        self.restart_button = thorpy.make_button("Restart", func=self._restart)
        self.quit_button = thorpy.make_button("Quit", func=self._quit)
        self.solve_button = thorpy.make_button("Solve", func=self._solve)
        self.help_button = thorpy.make_button("Help", func=self._help)
        group_box = thorpy.make_group(elements=[
            self.restart_button,
            self.quit_button,
            self.solve_button,
            self.help_button
        ])

    def _quit(self):
        pass

    def _restart(self):
        pass

    def _solve(self):
        pass

    def _help(self):
        pass