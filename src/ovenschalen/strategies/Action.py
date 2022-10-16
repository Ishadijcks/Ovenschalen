from enum import Enum


class Action(Enum):
    NO_DICE = "A"
    THROW = "B"

    def __eq__(self, other):
        return other.value == self.value
