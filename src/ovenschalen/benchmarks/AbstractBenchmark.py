from abc import ABC
from typing import List

from ovenschalen.game.OvenschaalConfig import OvenschaalConfig
from ovenschalen.game.OverschaalGame import OvenschaalGame
from ovenschalen.game.Player import Player
from ovenschalen.plot.Plot import wins_barchart


class AbstractBenchmark(ABC):
    """Play games against a number of players and see how you do"""

    def __init__(self, player: Player, opponents: List[Player], rounds: int = 1000) -> None:
        self.players = [player] + opponents
        self.rounds = rounds

    def simulate(self, config: OvenschaalConfig):
        win_counts = {}
        for player in self.players:
            win_counts[player.name] = 0

        for i in range(self.rounds):
            game = OvenschaalGame(self.players, config)
            winner = game.start()
            win_counts[winner.name] += 1

        wins_barchart(win_counts)
        print(win_counts)
