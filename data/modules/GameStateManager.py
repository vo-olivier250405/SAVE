class GameStateManager:
    def __init__(self, current_state) -> None:
        self.current_state = current_state

    def get_current_state(self):
        return self.current_state

    def set_current_state(self, state):
        self.current_state = state
