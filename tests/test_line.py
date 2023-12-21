import pytest

from game.board import EMPTY, Line


def test_get_line_values(line: Line):
    assert line.get_line_values() == [EMPTY, EMPTY, EMPTY]


def test_add_value_base(line: Line):
    assert line.add_value(1)
    assert line.get_line_values() == [1, EMPTY, EMPTY]


@pytest.mark.parametrize(
    "values, add_value_results, line_result",
    [
        ([1], [True], [1, EMPTY, EMPTY]),
        ([1, 2, 3], [True, True, True], [1, 2, 3]),
        ([1, 7, 3], [True, False, True], [1, 3, EMPTY]),
        ([1, 2, 3, 4], [True, True, True, False], [1, 2, 3]),
    ],
)
def test_add_value(
    line: Line, values: list[int], add_value_results: list[bool], line_result: list[int]
):
    for v, r in zip(values, add_value_results):
        assert line.add_value(v) == r
    assert line.get_line_values() == line_result


@pytest.mark.parametrize(
    "values, result",
    [
        ([], 0),
        ([1], 1),
        ([1, 1], 4),
        ([1, 1, 2], 6),
        ([1, 2, 1], 6),
        ([1, 2, 2], 9),
        ([2, 2, 2], 18),
    ],
)
def test_get_score(line: Line, values: list[int], result: int):
    for v in values:
        line.add_value(v)
    assert line.get_score() == result


@pytest.mark.parametrize(
    "values, result",
    [
        ([], False),
        ([1, 1, 1], True),
    ],
)
def test_is_full(line: Line, values: list[int], result: bool):
    for v in values:
        line.add_value(v)
    assert line.is_full() == result


@pytest.mark.parametrize(
    "values, remove_value, line_result",
    [
        ([], 1, [EMPTY, EMPTY, EMPTY]),
        ([1], 1, [EMPTY, EMPTY, EMPTY]),
        ([2], 1, [2, EMPTY, EMPTY]),
        ([1, 2, 3], 1, [2, 3, EMPTY]),
        ([1, 2, 3], 2, [1, 3, EMPTY]),
        ([1, 2, 3], 3, [1, 2, EMPTY]),
        ([1, 1, 2], 1, [2, EMPTY, EMPTY]),
        ([1, 1, 1], 1, [EMPTY, EMPTY, EMPTY]),
    ],
)
def test_remove_value(
    line: Line, values: list[int], remove_value: int, line_result: list[int]
):
    for v in values:
        line.add_value(v)
    line.remove_value(remove_value)
    assert line.get_line_values() == line_result
