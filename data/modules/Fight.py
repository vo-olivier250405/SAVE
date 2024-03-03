import pygame
from data.loaders.textures_loader import GFX
from data.modules.Cursor import Cursor
from data.modules.FightStateManager import FightStateManager


class Fight:
    def __init__(self, display, gameStateManager) -> None:
        self.display = display
        self.gameStateManager = gameStateManager
        self.fightStateManager = FightStateManager("fightMenu")
        self.states = {"fightMenu": FightMenu(
            self.display, self.fightStateManager), "battle": Battle(self.display, self.fightStateManager)}

    def run(self, _actions=None):
        self.display.fill("blue")
        self.states[self.fightStateManager.get_current_state()].run(_actions)
        for event in _actions:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                print("here")
                self.fightStateManager.set_new_state("battle")


class Battle:
    def __init__(self, display, fightStateManager: FightStateManager) -> None:
        print("We are in battle phase")
        self.display = display
        self.fightStateManager = fightStateManager

    def run(self, _actions):
        self.display.fill("green")

        # self.fightStateManager.set_new_state("fightMenu")


class FightMenu:
    def __init__(self, display, fightStateManager: FightStateManager) -> None:
        print("We are in battle menu")
        self.display = display
        self.fightStateManager = fightStateManager
        self.props = {
            "width": self.display.get_width(),
            "height": self.display.get_height(),
            "index": 0,
        }
        self.menu_options = {0: "fight", 1: "act", 2: "items", 3: "mercy"}
        self.cursor = Cursor(self.props["index"], self.props["height"] - 150)

    def run(self, _actions=None):

        self.display.fill("black")
        self.render()
        self.update()
        for event in _actions:
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                    self.props["index"] = (
                        self.props["index"] + {pygame.K_RIGHT: 1, pygame.K_LEFT: -1}[event.key]) % len(self.menu_options)
                elif event.key == pygame.K_RETURN:
                    print(self.menu_options[self.props["index"]])

    def render(self):
        """_summary_
        """
        for i in range(4):
            pygame.draw.rect(self.display, "white",
                             (i * self.props["width"] // 4 + 50, self.props["height"] - 150, 200, 100))
        self.cursor.render(self.display)

    def update(self):
        """_summary_
        """
        x = self.props["index"] * self.props["width"] // 4
        self.cursor.update(x, self.props["height"] - 150)
