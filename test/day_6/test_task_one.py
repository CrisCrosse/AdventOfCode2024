from unittest.mock import patch

import pytest
from pandas import DataFrame
from day_6.task_one import GuardMap
from day_6.Direction import Direction


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


@patch("day_6.task_one.GuardMap.set_map_properties")
@patch("day_6.task_one.get_next_set_of_map_features")
@patch("day_6.task_one.GuardMap.get_map_properties_other_than_is_on_map")
def test_get_next_map_position_and_update_self_calls_correct_functions_with_correct_args(get_map_properties_mock,
                                                                                         get_next_features_mock,
                                                                                         set_map_properties_mock
                                                                                         ):
    returned_current_map_properties = (
        DataFrame(
            [
                [".", ">", ".", "."],
                [".", ".", ".", "."],
                [".", ".", ".", "."],
                [".", ".", ".", "."]
            ]
        ),
        (0, 1),
        Direction.RIGHT
    )
    get_map_properties_mock.return_value = returned_current_map_properties

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
        True
    )
    get_next_features_mock.return_value = next_map_features

    test_map = GuardMap()
    test_map.get_next_map_position_and_update_self()

    get_next_features_mock.assert_called_once()
    get_next_features_mock.assert_called_with(*returned_current_map_properties)

    set_map_properties_mock.assert_called_once()
    set_map_properties_mock.assert_called_with(*next_map_features)


def test_move_guard_until_leaves_grid_from_example():
    current_map = DataFrame(
        [
            [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "#", ".", ".", "^", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", ".", ".", "."]
        ]
    )
    expected = DataFrame(
        [
            [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "X", "X", "X", "X", "X", "#"],
            [".", ".", ".", ".", "X", ".", ".", ".", "X", "."],
            [".", ".", "#", ".", "X", ".", ".", ".", "X", "."],
            [".", ".", "X", "X", "X", "X", "X", "#", "X", "."],
            [".", ".", "X", ".", "X", ".", "X", ".", "X", "."],
            [".", "#", "X", "X", "X", "X", "X", "X", "X", "."],
            [".", "X", "X", "X", "X", "X", "X", "X", "#", "."],
            ["#", "X", "X", "X", "X", "X", "X", "X", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", "X", ".", "."]
        ]
    )
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(6, 4),
                         direction_of_travel=Direction.UP,
                         is_on_map=True
                         )
    actual = guard_map.move_guard_until_leaves_grid()
    assert actual.equals(expected)
