from setup.driver import GameDriver, GameProperties

if __name__ == '__main__':
    properties = GameProperties()
    driver = GameDriver(properties)
    driver.launch_game()