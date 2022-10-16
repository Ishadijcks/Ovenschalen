from ovenschalen.game.OvenschaalState import OvenschaalState
from ovenschalen.strategies.AbstractStrategy import AbstractStrategy
from ovenschalen.strategies.Action import Action


class Player:
    def __init__(self, name: str, strategy: AbstractStrategy) -> None:
        self.name = name
        self.strategy = strategy
        self.dice_count = 0

    def start_game(self, dice_count):
        self.dice_count = dice_count

    def throw_die(self):
        self.dice_count -= 1

    def gain_dice(self, amount):
        self.dice_count += amount

    def __str__(self) -> str:
        return f"{self.name}({self.strategy})"

    def process_turn(self, state: OvenschaalState) -> Action:
        return self.strategy.process_turn(state)
