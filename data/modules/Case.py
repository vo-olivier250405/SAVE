import pygame

from data.loaders.textures_loader import GFX


class Case:
    def __init__(self, pos) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.is_current = False

    def render(self, display):
        """_summary_
        """
        #  pygame.draw.rect(display, "white", (self.x, self.y, 200, 100))

        color = "red" if self.is_current else "white"
        pygame.draw.rect(display, color, (self.x, self.y, 200, 100), 5)

    def update(self):
        """_summary_
        """
        pass
