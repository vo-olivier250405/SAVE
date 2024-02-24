"""
Player class
"""
import pygame as pg
from data.loaders.textures_loader import GFX


class Player(pg.sprite.Sprite):
    """
    Player class
    """

    def __init__(self) -> None:
        super().__init__()
        self.init_dict()

    def init_dict(self):
        self.vals = {"image": GFX["player"]}
        self.rect = self.vals["image"].get_rect()
        self.rect.x = 100
        self.rect.y = 100
