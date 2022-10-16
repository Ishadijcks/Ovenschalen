from ovenschalen.benchmarks.AlwaysThrowBenchmark import AlwaysThrowBenchmark
from ovenschalen.benchmarks.UpToNBenchmark import UpToNBenchmark
from ovenschalen.strategies.NeverThrowStrategy import NeverThrowStrategy
from ovenschalen.strategies.UpToNStrategy import UpToNStrategy
from src.ovenschalen.game.Player import Player
from src.ovenschalen.strategies.AlwaysThrowStrategy import AlwaysThrowStrategy


def main():
    benchmark = UpToNBenchmark(
        player=Player("Always", AlwaysThrowStrategy()),
        rounds=10000,
        opponent_count=8,
    )
    benchmark.simulate()


if __name__ == '__main__':
    main()
