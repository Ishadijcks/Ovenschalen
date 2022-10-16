from ovenschalen.benchmarks.AbstractBenchmark import AbstractBenchmark
from ovenschalen.game.Player import Player
from ovenschalen.strategies.NeverThrowStrategy import NeverThrowStrategy


class NeverThrowBenchmark(AbstractBenchmark):
    """Play games against n players who never throw when given the option"""

    def __init__(self, player: Player, rounds: int = 1000, opponent_count: int = 1) -> None:
        opponents = []
        for i in range(opponent_count):
            opponents.append(Player(f"Never-{i}", NeverThrowStrategy()))
        super().__init__(player, opponents, rounds)
