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
        self.is_first_round = True
        self.turns = 0
        self.rolls = 0
        self.schaal = Ovenschaal()

    def start(self) -> Player:
        """Start a game of ovenschalen and return the winner or loser depending on the config"""
        self.schaal = Ovenschaal()

        print("Simulating game between", ' and '.join(map(lambda p: str(p), self.players)))
        # Configure the players so the game can start
        for player in self.players:
            player.start_game(self.config.dice_count)

        # Set starting player
        if self.config.first_player_starts:
            self.current_player = 0
        else:
            self.current_player = random.randint(0, len(self.players) - 1)

        if self.config.randomize_player_order:
            random.shuffle(self.players)

        while not self.is_game_over():
            # Skip already finished players
            current_player: Player = self.players[self.current_player]
            if current_player.dice_count == 0:
                self.next_turn()
                continue

            self.process_turn()
            self.turns += 1
            if self.turns == len(self.players):
                self.is_first_round = False

            self.print_state()
            self.next_turn()

        for player in self.players:
            if player.dice_count == 0:
                return player
        raise NoWinnerException()

    def is_game_over(self) -> bool:
        # Sanity check
        players_below_zero = len(list(filter(lambda player: player.dice_count < 0, self.players)))
        if players_below_zero > 0:
            self.print_state()
            exit(1)

        players_with_zero = len(list(filter(lambda player: player.dice_count == 0, self.players)))
        if self.config.play_to_win:
            return players_with_zero > 0
        else:
            return players_with_zero == len(self.players) - 1

    def get_state(self) -> OvenschaalState:
        return OvenschaalState(
            player_dice_counts=list(map(lambda player: player.dice_count, self.players)),
            schaal_dice_count=self.schaal.dice,
            current_player=self.current_player,
        )

    def print_state(self):
        print(self.get_state())

    def roll(self) -> int:
        self.rolls += 1
        # TODO make dice customizable as well
        return random.randint(1, 6)

    def process_turn(self):
        current_player: Player = self.players[self.current_player]

        # First toss is forced
        die = self.roll()
        print(f"{current_player.name} rolled a {die}", end=' / ')

        current_player.throw_die()
        self.schaal.add(die)

        duplicates = self.schaal.process_state()
        if duplicates > 0:
            # We got duplicates, turn is over
            current_player.gain_dice(duplicates)
            return
        if self.is_first_round or current_player.dice_count == 0:
            return

        if die == 6 and not self.is_game_over():
            self.process_turn()
            return

        if self.is_game_over():
            return

        action = current_player.process_turn(self.get_state())
        if action == Action.THROW:
            self.process_turn()
        elif action == Action.NO_DICE:
            return

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)
