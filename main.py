from setup.driver import GameDriver, GameProperties
from ui.menu import Menu\


if __name__ == '__main__':
    properties = GameProperties()
    driver = GameDriver(properties, 6, 0)
    game_menu = Menu(driver)
    game_menu.display_menu()
