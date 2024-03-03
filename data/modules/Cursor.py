import pygame
from data.loaders.textures_loader import GFX


class Cursor:
    def __init__(self, x, y) -> None:
        self.image = GFX["player"]
        self.rect = self.image.get_rect()
        self.rect = [x, y]

    def render(self, display):
        """_summary_
        """
        display.blit(self.image, self.rect)

    def update(self, x, y):
        """_summary_
        """
        self.rect = [x, y]
