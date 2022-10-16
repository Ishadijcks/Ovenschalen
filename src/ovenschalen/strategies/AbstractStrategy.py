from abc import ABC, abstractmethod

from src.ovenschalen.game.OvenschaalState import OvenschaalState
from src.ovenschalen.strategies.Action import Action


class AbstractStrategy(ABC):
    name: str

    @abstractmethod
    def process_turn(self, state: OvenschaalState) -> Action:
        raise NotImplementedError("Strategy does not implement process_turn)")

    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError("Strategy does not implement get_name)")

    def __str__(self) -> str:
        return self.get_name()

