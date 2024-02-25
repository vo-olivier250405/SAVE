import pygame as pg
from os import system
from data.modules.constants import COLORS, DIMENSIONS
from data.modules.player import Player

pg.init()


def collision(sprite1, sprite2) -> bool:
    """_summary_

    Args:
        sprite1 (_type_): _description_
        sprite2 (_type_): _description_

    Returns:
        bool: _description_
    """
    return pg.sprite.collide_mask(sprite1, sprite2)


test: bool = True
clock = pg.time.Clock()
update_rect = []
display = pg.display
display.set_caption("Save v.1.0.0")
surface = display.set_mode(DIMENSIONS)

rectangle_props = {"x": 400, "y": 200}
turn_is_ended = False

player = Player(
    pos={"x": rectangle_props["x"] * 1.25, "y": rectangle_props["y"] * 2.5})


while test:
    update_rect.append(pg.draw.rect(surface, COLORS["black"],
                                    (0, 0, DIMENSIONS[0], DIMENSIONS[1])))
    update_rect.append(pg.draw.rect(
        surface, COLORS["white"], ((DIMENSIONS[0] - rectangle_props["x"]) // 2, DIMENSIONS[1] - rectangle_props["y"] - 100, rectangle_props["x"], rectangle_props["y"]), 7))
    dt = clock.tick(60) / 1000.0
    player.update(surface=surface, update_rect=update_rect)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            test = False
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            turn_is_ended = True

    if rectangle_props["x"] <= 600 and turn_is_ended:
        rectangle_props["x"] += 10
    if rectangle_props["x"] > 400 and not turn_is_ended:
        rectangle_props["x"] -= 10
    pg.display.update(update_rect)
    update_rect = []
