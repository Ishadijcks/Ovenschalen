from src.ovenschalen.game.OvenschaalState import OvenschaalState
from src.ovenschalen.strategies.AbstractStrategy import AbstractStrategy
from src.ovenschalen.strategies.Action import Action


class NeverThrowStrategy(AbstractStrategy):
    """Never throw when given the option"""

    def get_name(self) -> str:
        return "Never Throw"

    def process_turn(self, state: OvenschaalState) -> Action:
        return Action.NO_DICE
