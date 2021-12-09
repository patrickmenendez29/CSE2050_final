import thorpy
import pygame

class Menu:
    def __init__(self):
        pass

    def display_menu(self):
        thorpy.set_theme("human")
        button = thorpy.make_button("Quit", func=thorpy.functions.quit_func)
        self._input_field = thorpy.Inserter(name="Enter your name: ", value="")
        submit_button = thorpy.make_button("Submit", func=self.process_input)
        group_box = thorpy.make_group(elements=[self._input_field, submit_button])
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

    def react(self, event):
        self._menu.react(event)

    def process_input(self):
        player_name = self._input_field.get_value().title()
        if len(player_name) > 0:
            thorpy.launch_blocking_alert(title=f"Welcome {player_name}!",
            text="This is the land of The Champions!\n"
            "Are you ready to take on the lord of Omicron,\n"
            "defeat him and save Planet Earth?",
            parent=self._background
            ) # for auto-unblitting)
        self._box.remove_all_elements()
        self._box.unblit()
        self._box.update()
        self._menu.refresh()

        pygame.display.update()


