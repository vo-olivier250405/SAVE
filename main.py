import pygame as pg
from os import system
from data.modules.constants import COLORS, DIMENSIONS
from data.modules.player import Player

pg.init()


test: bool = True
clock = pg.time.Clock()
update_rect = []
display = pg.display
display.set_caption("Save v.1.0.0")
surface = display.set_mode(DIMENSIONS)


player = Player()


while test:
    surface.fill(COLORS["black"])
    update_rect.append(pg.draw.rect(
        surface, COLORS["white"], ((DIMENSIONS[0] - 200) // 2, DIMENSIONS[1] - 200 - 100, 200, 150), 7))
    update_rect.append(surface.blit(player.vals["image"], player.rect))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            test = False
    print(player.rect)
    pg.display.update(update_rect)
    update_rect = []
