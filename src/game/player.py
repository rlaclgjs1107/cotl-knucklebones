from game.board import Board


class Player:
    def __init__(self):
        self.__my_board = Board()

    def get_line_score(self, line_no: int) -> int:
        return self.__my_board.get_line_score(line_no)

    def get_total_score(self) -> int:
        return self.__my_board.get_total_score()

    def get_board_values(self) -> list[list[int]]:
        return self.__my_board.get_board_values()

    def get_available_lines(self) -> list[int]:
        return self.__my_board.get_available_lines()

    def play(self, line_no: int, value: int) -> bool:
        return self.__my_board.add_value_in_line(line_no, value)
