from ovenschalen.benchmarks.UpToNBenchmark import UpToNBenchmark
from ovenschalen.game.OvenschaalConfig import OvenschaalConfig
from src.ovenschalen.game.Player import Player
from src.ovenschalen.strategies.AlwaysThrowStrategy import AlwaysThrowStrategy


def main():
    benchmark = UpToNBenchmark(
        player=Player("Isha", AlwaysThrowStrategy()),
        rounds=1,
        opponent_count=2,
    )
    benchmark.simulate(config=OvenschaalConfig(
        dice_count=5,
        randomize_player_order=True,
        first_player_starts=False,
        play_to_win=False
    ))


if __name__ == '__main__':
    main()
