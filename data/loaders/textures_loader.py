import pygame as pg

pg.display.init()

GFX = {}
GFX["player"] = pg.transform.scale(
    pg.image.load("data/gfx/heart.png"), (25, 25))
