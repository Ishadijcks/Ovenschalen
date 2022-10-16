from typing import List


class Ovenschaal:

    def __init__(self) -> None:
        self.dice: List[int] = []

    def add(self, number: int):
        self.dice.append(number)

    def process_state(self) -> int:
        """Removes duplicate dice from the schaal and returns how many duplicates were found"""
        duplicates = 0
        new_dice = []

        # TODO be able to handle larger sized dice
        for die in range(6):
            if die == 6:
                continue

            count = self.dice.count(die)
            if count > 1:
                duplicates += count
            elif count == 1:
                new_dice.append(die)

        assert duplicates + len(new_dice) + self.dice.count(6) == len(self.dice)
        self.dice = new_dice
        return duplicates
