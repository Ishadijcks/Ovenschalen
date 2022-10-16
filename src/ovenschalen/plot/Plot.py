import matplotlib.pyplot as plt

from ovenschalen.game.OvenschaalConfig import OvenschaalConfig


def results_barchart(winning_dict, config: OvenschaalConfig):
    """Take a dictionary of the form name --> wins and plot it as a bar chart"""
    plt.bar(range(len(winning_dict)), list(winning_dict.values()), align='center')
    plt.xticks(range(len(winning_dict)), list(winning_dict.keys()))
    if config.play_to_win:
        plt.ylabel("Wins")
    else:
        plt.ylabel("Losses")

    total_games = sum(winning_dict.values())
    plt.xlabel(f"{total_games} games, {config}")
    plt.show()
