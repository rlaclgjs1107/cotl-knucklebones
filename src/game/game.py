from secrets import randbelow

from game.dice import roll_dice
from game.player import Player

GAME_STATE_INIT = 0
GAME_STATE_START = 1
GAME_STATE_PLAY = 2
GAME_STATE_END = 3


class Observer:
    def update(self, game: "Game"):
        pass


class Game:
    def __init__(self):
        self.__players: tuple[Player, Player]
        self.__turn: int
        self.__first_player: int
        self.__dice_value: int
        self.__state: int = GAME_STATE_INIT
        self.__observers: list[Observer] = []

    def notify(self):
        for observer in self.__observers:
            observer.update(self)

    def register(self, observer: Observer):
        self.__observers.append(observer)

    @staticmethod
    def is_valid_player_no(n: int) -> bool:
        return 0 <= n < 2

    def get_player_line_score(self, player_no: int, line_no: int) -> int:
        assert self.is_valid_player_no(player_no)
        return self.__players[player_no].get_line_score(line_no)

    def get_player_total_score(self, player_no: int) -> int:
        assert self.is_valid_player_no(player_no)
        return self.__players[player_no].get_total_score()

    def get_player_board_values(self, player_no: int) -> list[list[int]]:
        assert self.is_valid_player_no(player_no)
        return self.__players[player_no].get_board_values()

    def get_player_available_lines(self, player_no: int) -> list[int]:
        assert self.is_valid_player_no(player_no)
        return self.__players[player_no].get_available_lines()

    def get_turn(self) -> int:
        return self.__turn

    def get_current_player_no(self) -> int:
        return (self.__turn + self.__first_player) % 2

    def get_dice_value(self) -> int:
        return self.__dice_value

    def get_state(self) -> int:
        return self.__state

    def get_winner(self) -> int:
        assert self.__state == GAME_STATE_END
        return self.__winner

    def start_game(self):
        assert self.__state == GAME_STATE_INIT or self.__state == GAME_STATE_END
        self.__turn = 0
        self.__players = (Player(), Player())
        self.__first_player = randbelow(2)
        self.__state = GAME_STATE_START
        self.notify()

    def play_game(self):
        assert self.__state == GAME_STATE_START or self.__state == GAME_STATE_PLAY
        self.__turn += 1
        self.__dice_value = roll_dice()
        self.__state = GAME_STATE_PLAY
        self.notify()

    def end_game(self):
        assert self.__state == GAME_STATE_PLAY
        self.__state = GAME_STATE_END
        self.__winner = (
            0 if self.get_player_total_score(0) > self.get_player_total_score(1) else 1
        )
        self.notify()

    def player_move(self, player_no: int, line_no: int):
        assert self.__state == GAME_STATE_PLAY
        assert self.is_valid_player_no(player_no)
        assert line_no in self.get_player_available_lines(player_no)

        other_no = (player_no + 1) % 2
        self.__players[player_no].place_dice(line_no, self.__dice_value)
        self.__players[other_no].remove_dice(line_no, self.__dice_value)

        if self.check_end():
            self.end_game()
        else:
            self.play_game()

    def check_end(self) -> bool:
        return (
            len(self.__players[0].get_available_lines()) == 0
            or len(self.__players[1].get_available_lines()) == 0
        )
