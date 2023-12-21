from collections import Counter

from game.dice import is_dice_value

EMPTY = 0
LINE_N = 3
LINE_DEPTH = 3


class Line:
    def __init__(self):
        self.__line: list[int] = [EMPTY for _ in range(LINE_DEPTH)]
        self.__count: int = 0

    def get_line_values(self):
        return self.__line

    def get_score(self) -> int:
        value_counts = Counter(self.__line)

        score = 0
        for value in self.__line:
            score += value * value_counts[value]

        return score

    def is_full(self) -> bool:
        return self.__count == LINE_DEPTH

    def add_value(self, value: int) -> bool:
        if self.is_full():
            return False

        if not is_dice_value(value):
            return False

        self.__line[self.__count] = value
        self.__count += 1

        return True

    def remove_value(self, value: int):
        new_line: list[int] = []
        new_count: int = 0
        for _value in self.__line:
            if _value != value:
                new_line.append(_value)
                new_count += 1
        new_line = new_line + [EMPTY] * (LINE_DEPTH - new_count)
        self.__line = new_line
        self.__count = new_count


class Board:
    def __init__(self):
        self.__board: list[Line] = [Line() for _ in range(LINE_N)]

    @staticmethod
    def is_valid_line_n(n) -> bool:
        return 0 <= n < LINE_N

    def get_board_values(self) -> list[list[int]]:
        board_values: list[list[int]] = []

        for line in self.__board:
            board_values.append(line.get_line_values())

        return board_values

    def get_total_score(self) -> int:
        return sum(line.get_score() for line in self.__board)

    def get_line_score(self, line_no: int) -> int:
        if not Board.is_valid_line_n(line_no):
            return -1
        return self.__board[line_no].get_score()

    def get_available_lines(self) -> list[int]:
        available_lines: list[int] = []
        for line_n, line in enumerate(self.__board):
            if not line.is_full():
                available_lines.append(line_n)
        return available_lines

    def add_value_in_line(self, line_n: int, value: int) -> bool:
        if not is_dice_value(value) or not Board.is_valid_line_n(line_n):
            return False

        return self.__board[line_n].add_value(value)

    def remove_value_in_line(self, line_n: int, value: int) -> bool:
        if not is_dice_value(value) or not Board.is_valid_line_n(line_n):
            return False

        self.__board[line_n].remove_value(value)
        return True
