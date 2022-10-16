from ovenschalen.benchmarks.AbstractBenchmark import AbstractBenchmark
from ovenschalen.game.Player import Player
from ovenschalen.strategies.UpToNStrategy import UpToNStrategy


class UpToNBenchmark(AbstractBenchmark):
    """Play games against n players who always throw when there are less than {index} dice"""

    def __init__(self, player: Player, rounds: int = 1000, opponent_count: int = 1) -> None:
        opponents = []
        for i in range(opponent_count):
            opponents.append(Player(f"UpTo-{i+1}", UpToNStrategy(i+1)))
        super().__init__(player, opponents, rounds)
