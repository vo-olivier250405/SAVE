import pygame as pg

from data.loaders.textures_loader import GFX


class Case():
    def __init__(self, pos) -> None:
        self.init_dict(pos)

    def init_dict(self, pos):
        self.vals = {"image": GFX["case"]}
        self.rect = self.vals["image"].get_rect()
        self.rect = pos

    def log_utility(self, utility):
        print(utility)
