import pytest
from pandas import DataFrame
from day_6.task_one import move_guard, get_starting_map_from_input, GuardMap
from day_6.Direction import Direction


def test_get_starting_map_from_input() -> None:
    actual = get_starting_map_from_input()

    assert isinstance(actual, DataFrame)
    assert actual.shape == (130, 130)

    first_row = actual.iloc[0]
    first_nine_items_from_first_row = list(first_row[:9])
    assert first_nine_items_from_first_row == [".", ".", ".", ".", ".", "#", ".", ".", "#"]

    for row_number, row in actual.iterrows():
        for column_number, value in enumerate(row):
            if value == "X":
                raise Exception("Should be No X present in start map")


def test_get_starting_guard_location_from_map() -> None:
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", "^", "."]
        ]
    )
    guard_map = GuardMap(current_map)
    actual = guard_map.get_guard_location()
    assert actual == (3, 2)


def test_get_starting_guard_location_raises_error_when_no_carat() -> None:
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    with pytest.raises(Exception):
        GuardMap(current_map)


def test_move_guard_up_one_space():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", "^", "."]
        ]
    )
    expected_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", "^", "."],
            [".", ".", "X", "."]
        ]
    )
    actual = move_guard(current_map, (3, 2), Direction.UP, True)
    assert actual.equals(expected_map)

def test_move_guard_turn_to_right():
    current_map = DataFrame(
        [
            [".", ".", "#", "."],
            [".", ".", "^", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    expected_map = DataFrame(
        [
            [".", ".", "#", "."],
            [".", ".", ">", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    actual = move_guard(current_map, (1, 2), Direction.UP, True)
    assert actual.equals(expected_map)


def test_move_guard_move_to_right():
    current_map = DataFrame(
        [
            [".", ".", "#", "."],
            [".", ".", ">", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    expected_map = DataFrame(
        [
            [".", ".", "#", "."],
            [".", ".", "X", ">"],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    actual = move_guard(current_map, (1, 2), Direction.RIGHT, True)
    assert actual.equals(expected_map)

def test_move_guard_turn_to_down():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ">", "#"],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    expected_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", "v", "#"],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    actual = move_guard(current_map, (1, 2), Direction.RIGHT, True)
    assert actual.equals(expected_map)


def test_move_guard_turn_to_left():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", "v", "."],
            [".", ".", "#", "."],
            [".", ".", ".", "."]
        ]
    )
    expected_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", "<", "."],
            [".", ".", "#", "."],
            [".", ".", ".", "."]
        ]
    )
    actual = move_guard(current_map, (1, 2), Direction.DOWN, True)
    assert actual.equals(expected_map)


def test_move_guard_turn_to_up():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", "#", "<", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    expected_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", "#", "^", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    actual = move_guard(current_map, (1, 2), Direction.LEFT, True)
    assert actual.equals(expected_map)


def test_move_guard_leaves_grid_to_right():
    current_map = DataFrame(
        [
            [".", ".", "#", "."],
            [".", ".", "X", ">"],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    expected_map = DataFrame(
        [
            [".", ".", "#", "."],
            [".", ".", "X", "X"],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    is_on_map = True
    actual = move_guard(current_map, (1, 2), Direction.RIGHT, is_on_map)
    assert actual.equals(expected_map)
    assert is_on_map == False

# do for all directions

