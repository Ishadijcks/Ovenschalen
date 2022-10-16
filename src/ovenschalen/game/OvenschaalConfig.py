from dataclasses import dataclass


@dataclass
class OvenschaalConfig:
    # The amount of dice each player starts with
    dice_count: int = 5

    # Perform a stoelendans before the game begins
    randomize_player_order: bool = True

    # Does the first player start, or a random player
    first_player_starts: bool = False

    # Is the first player to lose their dice the winner, or do we play until there is one player left
    play_to_win: bool = False
