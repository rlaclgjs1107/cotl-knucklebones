import pytest

from game.board import Board, Line


@pytest.fixture
def line():
    _line = Line()
    return _line


@pytest.fixture
def board():
    _board = Board()
    return _board
