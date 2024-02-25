"""
Player class
"""
import pygame as pg
from data.loaders.textures_loader import GFX


class Player(pg.sprite.Sprite):
    """
    Player class
    """

    def __init__(self, pos) -> None:
        super().__init__()
        self.init_dict(pos)

    def init_dict(self, pos):
        self.vals = {"image": GFX["player"]}
        self.rect = self.vals["image"].get_rect()
        self.rect.x = pos["x"]
        self.rect.y = pos["y"]

    def movements(self):
        """_summary_
        """
        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_z]:
            self.rect.y -= 5
        elif pressed_key[pg.K_s]:
            self.rect.y += 5
        elif pressed_key[pg.K_q]:
            self.rect.x -= 5
        elif pressed_key[pg.K_d]:
            self.rect.x += 5

    def update(self, surface, update_rect):
        """_summary_

        Args:
            surface (_type_): _description_
            update_rect (_type_): _description_
        """
        self.movements()
        update_rect.append(surface.blit(self.vals["image"], self.rect))
