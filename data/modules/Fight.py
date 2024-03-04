import pygame
from data.loaders.textures_loader import GFX
from data.modules.Case import Case
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
        self.menu_options = {0: "fight", 1: "action", 2: "items", 3: "mercy"}
        self.cursor = Cursor(0, self.props["height"] - 150)
        self.init_cases()

    def init_cases(self):
        """_summary_
        """
        self.cases = []
        for i in range(4):
            self.cases.append(
                Case(pos=[i * self.props["width"] // 4 + 50, self.props["height"] - 150], name=self.menu_options[i].upper()))

    def run(self, _actions=None):
        self.update_events(actions=_actions)
        self.update()
        self.render()

    def render(self):
        """_summary_
        """
        self.display.fill("black")
        [case.render(self.display) for case in self.cases]
        self.cases[self.props["index"]].is_current = True
        for i in range(len(self.cases)):
            if i != self.props["index"]:
                self.cases[i].is_current = False
        self.cursor.render(self.display)

    def update(self):
        """_summary_
        """
        x = self.cases[self.props["index"]].x + 20
        y = self.cases[self.props["index"]].y + \
            50 - self.cursor.image.get_height() // 2
        self.cursor.update(x, y)

    def update_events(self, actions):
        """_summary_

        Args:
            actions (_type_): _description_
        """
        for event in actions:
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                    self.props["index"] = (
                        self.props["index"] + {pygame.K_RIGHT: 1, pygame.K_LEFT: -1}[event.key]) % len(self.menu_options)
                elif event.key == pygame.K_RETURN:
                    print(self.menu_options[self.props["index"]])
