from typing import List


class OvenschaalState:
    def __init__(self, player_dice_counts: List[int], schaal_dice_count: List[int], current_player: int) -> None:
        self.player_dice_counts = player_dice_counts
        self.schaal_dice_count = schaal_dice_count
        self.current_player = current_player

    def __str__(self) -> str:
        """Ugly string formatting to print the state"""

        players_str = ""
        for i in range(len(self.player_dice_counts)):
            # Wrap current player in parentheses for clarity
            if i == self.current_player:
                players_str += f"({self.player_dice_counts[i]})"
            else:
                players_str += str(self.player_dice_counts[i])

            # Add space between entries
            if i != len(self.player_dice_counts) - 1:
                players_str += " "

        return f"{self.schaal_dice_count} - {players_str}"
