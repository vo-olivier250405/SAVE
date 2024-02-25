"""
Class Sprite
"""
import pygame as pg


class Custom_Sprite(pg.sprite.Sprite):
    """_summary_

    Args:
        pg (_type_): _description_
    """

    def __init__(self, img, pos) -> None:
        super().__init__()
        self.init_dict(img, pos)

    def init_dict(self, img, pos):
        """_summary_
        """
        self.vals = {}
        self.vals["image"] = img
        self.vals["pos"] = pos
        self.rect = self.vals["image"].get_rect()
        self.rect.x = pos["x"], self.rect.y = pos["y"]
