import matplotlib.pyplot as plt


def wins_barchart(winning_dict):
    """Take a dictionary of the form name --> wins and plot it as a bar chart"""
    plt.bar(range(len(winning_dict)), list(winning_dict.values()), align='center')
    plt.xticks(range(len(winning_dict)), list(winning_dict.keys()))
    plt.ylabel("Wins")
    plt.show()
