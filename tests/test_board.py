import pytest

from game.board import EMPTY, Board


@pytest.mark.parametrize(
    "value, result",
    [
        (0, True),
        (1, True),
        (2, True),
        (3, False),
    ],
)
def test_is_valid_line(value: int, result: bool):
    assert Board.is_valid_line_n(value) == result


def test_get_board_values(board: Board):
    assert board.get_board_values() == [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]


def test_add_value_in_line_base(board: Board):
    assert board.add_value_in_line(0, 1)
    assert board.add_value_in_line(1, 2)
    assert board.add_value_in_line(2, 3)
    assert board.get_board_values() == [
        [1, EMPTY, EMPTY],
        [2, EMPTY, EMPTY],
        [3, EMPTY, EMPTY],
    ]


def test_add_value_in_line_base_invalid(board: Board):
    assert not board.add_value_in_line(3, 1)
    assert not board.add_value_in_line(1, 9)


def test_get_available_lines(board: Board):
    for i in range(1, 4):
        assert board.get_available_lines() == [0, 1, 2]
        board.add_value_in_line(0, i)
    assert board.get_available_lines() == [1, 2]


def test_get_line_score(board: Board):
    assert board.get_line_score(0) == 0
    assert board.get_line_score(3) == -1


def test_get_total_score(board: Board):
    assert board.get_total_score() == 0
    for i in range(1, 4):
        assert board.add_value_in_line(i - 1, i)
    assert board.get_total_score() == 6
    for i in range(1, 4):
        assert board.add_value_in_line(i - 1, i)
    assert board.get_total_score() == 24
    for i in range(1, 4):
        assert board.add_value_in_line(i - 1, i)
    assert board.get_total_score() == 54


def test_remove_value_in_line(board: Board):
    assert not board.remove_value_in_line(0, 0)
    assert not board.remove_value_in_line(3, 1)
