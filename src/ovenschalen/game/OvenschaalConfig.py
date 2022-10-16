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

    def __str__(self) -> str:
        to_win_string = "First to 0 wins" if self.play_to_win else "Last to 0 loses"
        dice_string = f"{self.dice_count} dice"
        starter_string = "First player start" if self.first_player_starts else "Random beginner"
        shuffled_string = "Players shuffled" if self.randomize_player_order else "Players not shuffled"

        return f"{to_win_string}, {dice_string}, {starter_string}, {shuffled_string}"
