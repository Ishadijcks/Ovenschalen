import random
from typing import List

from ovenschalen.exceptions.NoWinnerException import NoWinnerException
from ovenschalen.game.Ovenschaal import Ovenschaal
from ovenschalen.game.OvenschaalState import OvenschaalState
from ovenschalen.strategies.Action import Action
from src.ovenschalen.game.OvenschaalConfig import OvenschaalConfig
from src.ovenschalen.game.Player import Player


class OvenschaalGame:

    def __init__(self, players: List[Player], config: OvenschaalConfig) -> None:
        self.players = players
        self.config = config
        self.current_player = 0
        self.schaal = Ovenschaal()

    def start(self) -> Player:
        """Start a game of ovenschalen and return the winner"""
        self.schaal = Ovenschaal()

        print("Simulating game between", ' and '.join(map(lambda p: str(p), self.players)))
        # Configure the players so the game can start
        for player in self.players:
            player.start_game(self.config.dice_count)
        self.current_player = random.randint(0, len(self.players) - 1)

        while not self.is_game_won():
            self.process_turn()
            self.next_turn()
            self.print_state()

        for player in self.players:
            if player.dice_count == 0:
                return player
        raise NoWinnerException()

    def is_game_won(self) -> bool:
        for player in self.players:
            if player.dice_count == 0:
                return True
        return False

    def get_state(self) -> OvenschaalState:
        return OvenschaalState(
            player_dice_counts=list(map(lambda player: player.dice_count, self.players)),
            schaal_dice_count=self.schaal.dice,
            current_player=self.current_player,
        )

    def print_state(self):
        print(self.get_state())

    def throw_die(self) -> int:
        # TODO make dice customizable as well
        return random.randint(1, 6)

    def process_turn(self):
        current_player: Player = self.players[self.current_player]

        # First toss is forced
        die = self.throw_die()
        print(f"{current_player.name} rolled a {die}", end=' / ')

        current_player.throw_die()
        self.schaal.add(die)

        # TODO check if you need to rethrow after every 6
        if die == 6 and not self.is_game_won():
            self.process_turn()
            return

        duplicates = self.schaal.process_state()
        if duplicates > 0:
            # We got duplicates, turn is over
            current_player.gain_dice(duplicates)
            return
        if self.is_game_won():
            return

        action = current_player.process_turn(self.get_state())
        if action == Action.THROW:
            self.process_turn()
        elif action == Action.NO_DICE:
            return

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)
