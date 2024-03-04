import pygame as pg

pg.display.init()
pg.font.init()

GFX = {}
GFX["player"] = pg.transform.scale(
    pg.image.load("data/gfx/heart.png"), (25, 25))
GFX["case"] = pg.transform.scale(
    pg.image.load("data/gfx/temmieCar.jpg"), (100, 50))


FONTS = {}
FONTS["menu"] = pg.font.Font("data/gfx/fonts/save/save.ttf", 30)
