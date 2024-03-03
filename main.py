import pygame
from data.modules.Fight import Fight

from data.modules.GameStateManager import GameStateManager

SCREEN_PROPS = [1280, 720]
FPS = 60


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_PROPS)
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager("start")
        self.start = Start(self.screen, self.gameStateManager)
        self.fight = Fight(self.screen, self.gameStateManager)

        self.states = {"start": self.start, "fight": self.fight}

    def run(self):
        test = True
        while test:
            actions = pygame.event.get()
            # get the key returned by the gameStateManager
            self.states[self.gameStateManager.get_current_state()].run(actions)
            pygame.display.update()
            self.clock.tick(FPS)
            for event in actions:
                if event.type == pygame.QUIT:
                    test = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    self.gameStateManager.set_current_state("fight")
                    if event.key == pygame.K_ESCAPE:
                        self.gameStateManager.set_current_state("start")


class Start:
    def __init__(self, display, gameStateManager) -> None:
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self, _actions):
        self.display.fill("red")


if __name__ == "__main__":
    Game().run()
