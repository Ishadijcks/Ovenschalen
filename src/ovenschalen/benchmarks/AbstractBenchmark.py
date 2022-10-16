from abc import ABC
from typing import List

from ovenschalen.game.OvenschaalConfig import OvenschaalConfig
from ovenschalen.game.OverschaalGame import OvenschaalGame
from ovenschalen.game.Player import Player
from ovenschalen.plot.Plot import results_barchart


class AbstractBenchmark(ABC):
    """Play games against a number of players and see how you do"""

    def __init__(self, player: Player, opponents: List[Player], rounds: int = 1000) -> None:
        self.players = [player] + opponents
        self.rounds = rounds

    def simulate(self, config: OvenschaalConfig):
        result_counts = {}
        for player in self.players:
            result_counts[player.name] = 0

        for i in range(self.rounds):
            game = OvenschaalGame(self.players, config)
            player = game.start()
            result_counts[player.name] += 1

        results_barchart(result_counts, config)
