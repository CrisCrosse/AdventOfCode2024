from unittest.mock import patch

import pytest
from pandas import DataFrame
from day_6.task_one import get_starting_map_from_input, GuardMap, count_x_in_df
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


def test_move_guard_until_leaves_grid():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", "^", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    expected = DataFrame(
        [
            [".", ".", "X", "."],
            [".", ".", "X", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(1, 2),
                         direction_of_travel=Direction.UP,
                         is_on_map=True
                         )
    actual = guard_map.move_guard_until_leaves_grid()
    assert actual.equals(expected)


def test_move_guard_until_leaves_grid_with_turns():
    current_map = DataFrame(
        [
            [">", ".", "#", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", "#", ".", "."]
        ]
    )
    expected = DataFrame(
        [
            ["X", "X", "#", "."],
            [".", "X", ".", "."],
            ["X", "X", ".", "."],
            [".", "#", ".", "."]
        ]
    )
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(0, 0),
                         direction_of_travel=Direction.RIGHT,
                         is_on_map=True
                         )
    actual = guard_map.move_guard_until_leaves_grid()
    assert actual.equals(expected)


def test_count_x_in_df():
    finished_map = DataFrame(
        [
            ["X", "X", "#", "."],
            [".", "X", ".", "."],
            ["X", "X", ".", "."],
            [".", "#", ".", "."]
        ]
    )
    expected = 5
    actual = count_x_in_df(finished_map)
    assert actual == expected


@patch("day_6.task_one.GuardMap.set_map_properties")
@patch("day_6.task_one.GuardMap.get_next_set_of_map_features")
def test_get_next_map_position_and_update_self(get_next_features_mock,
                                               set_map_properties_mock
                                               ):
    current_map_features = (
        DataFrame(
            [
                [".", ">", ".", "."],
                [".", ".", ".", "."],
                [".", ".", ".", "."],
                [".", ".", ".", "."]
            ]
        ),
        (0, 1),
        Direction.RIGHT,
        False
    )

    next_map_features = (
        DataFrame(
            [
                [".", "X", ">", "."],
                [".", ".", ".", "."],
                [".", ".", ".", "."],
                [".", ".", ".", "."]
            ]
        ),
        (0, 2),
        Direction.RIGHT,
        False
    )
    get_next_features_mock.return_value = next_map_features

    GuardMap.get_next_map_position_and_update_self()
    pass


