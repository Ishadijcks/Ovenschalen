from src.ovenschalen.game.OvenschaalState import OvenschaalState
from src.ovenschalen.strategies.AbstractStrategy import AbstractStrategy
from src.ovenschalen.strategies.Action import Action


class AlwaysThrowStrategy(AbstractStrategy):
    """Always throw when given the option"""

    def get_name(self) -> str:
        return "Always Throw"

    def process_turn(self, state: OvenschaalState) -> Action:
        return Action.THROW
