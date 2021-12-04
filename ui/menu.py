import thorpy


class Menu:
    def __init__(self):
        pass

    def display_menu(self):
        thorpy.set_theme("human")
        self.start_button = thorpy.make_button("Submit")
        self.input_field = thorpy.launch_inserter("Enter grid size")
        self.group_box = thorpy.make_group(elements=[self.input_field, self.start_button])
        self.box = thorpy.Box(elements=[self.group_box])
        self.input_field.enter()
        self.box.center()
        self.box.blit()
        self.box.update()

    def process_input(self):
        pass

    def update_ui(self):
        playing_game = True
        while playing_game:
            self.clock.tick(45)
