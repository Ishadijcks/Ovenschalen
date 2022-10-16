from dataclasses import dataclass


@dataclass
class OvenschaalConfig:
    dice_count: int = 5
    randomize_player_order: bool = True
    first_player_starts: bool = False
