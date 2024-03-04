import pygame

from data.loaders.textures_loader import FONTS, GFX


class Case:
    def __init__(self, pos, name) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.is_current = False
        self.name = name

    def render(self, display):
        """_summary_
        """
        #  pygame.draw.rect(display, "white", (self.x, self.y, 200, 100))

        color = "red" if self.is_current else "white"
        pygame.draw.rect(display, color, (self.x, self.y, 200, 75), 5)

        text_color = (255, 0, 0) if self.is_current else (255, 255, 255)
        display.blit(FONTS["menu"].render(
            self.name, True, text_color), (self.x + 50, self.y + 45 - FONTS["menu"].get_height() // 2))

    def update(self):
        """_summary_
        """
        pass
