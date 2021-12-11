import pygame
from setup.properties import GameProperties


class GameObject:

    def __init__(self, parent, image):
        self.parent = parent
        self._row = None
        self._column = None
        self.size = None
        self.sprite = pygame.image.load(image)
        self.sprite = pygame.transform.scale(self.sprite, (self.parent.width, self.parent.height))

    def place_object(self, coordinates):
        x, y = coordinates
        image_rect = self.sprite.get_rect()
        image_rect.center = (x, y)
        self.parent.screen.blit(self.sprite, image_rect)

    def unblit(self):
        self.parent.screen.unblit(self.sprite)

class Queen(GameObject):

    def __init__(self, parent):
        super().__init__(parent, "game/assets/queen.png")

