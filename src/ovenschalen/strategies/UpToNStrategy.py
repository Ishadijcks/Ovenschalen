from src.ovenschalen.game.OvenschaalState import OvenschaalState
from src.ovenschalen.strategies.AbstractStrategy import AbstractStrategy
from src.ovenschalen.strategies.Action import Action


class UpToNStrategy(AbstractStrategy):
    """Throw until there are n dice in the schaal"""

    def __init__(self, n: int) -> None:
        super().__init__()
        self.n = n

    def get_name(self) -> str:
        return f"Up to {self.n}"

    def process_turn(self, state: OvenschaalState) -> Action:
        if len(state.schaal_dice_count) < self.n:
            return Action.THROW
        else:
            return Action.NO_DICE
