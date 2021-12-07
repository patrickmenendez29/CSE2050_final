import pygame
from setup.properties import GameProperties


class Bug:

    def __init__(self, image, size, properties: GameProperties):
        self._row = None
        self._column = None
        self.properties = properties
        self.size = size
        self.sprite = pygame.image.load(image)

    def place_bug(self, x, y):
        image_rect = self.sprite.get_rect()
        image_rect.center = (x, y)
        self.properties.screen.blit(self.sprite, image_rect)

