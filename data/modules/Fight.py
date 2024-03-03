import pygame
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

    def run(self, _actions=None):

        self.display.fill("yellow")
