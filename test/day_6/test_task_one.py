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


def test_go_up():
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
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(3,2),
                         direction_of_travel=Direction.UP,
                         is_on_map=True
                         )
    actual = guard_map.go_up_or_rotate()
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
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(1, 2),
                         direction_of_travel=Direction.UP,
                         is_on_map=True
                         )
    actual = guard_map.go_up_or_rotate()
    assert actual.equals(expected_map)


def test_move_guard_leaves_grid_to_top():
    current_map = DataFrame(
        [
            [".", ".", "^", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    expected_map = DataFrame(
        [
            [".", ".", "X", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(0, 2),
                         direction_of_travel=Direction.UP,
                         is_on_map=True
                         )
    actual = guard_map.go_up_or_rotate()
    assert actual.equals(expected_map)
    assert guard_map.is_on_map == False


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
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(1, 2),
                         direction_of_travel=Direction.RIGHT,
                         is_on_map=True
                         )
    actual = guard_map.go_right_or_rotate()
    assert actual.equals(expected_map)


def test_move_guard_leaves_grid_to_right():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", ">"],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    expected_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "X"],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(1, 3),
                         direction_of_travel=Direction.RIGHT,
                         is_on_map=True
                         )
    actual = guard_map.go_right_or_rotate()
    assert actual.equals(expected_map)
    assert guard_map.is_on_map == False


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
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(1, 2),
                         direction_of_travel=Direction.RIGHT,
                         is_on_map=True
                         )
    actual = guard_map.go_right_or_rotate()
    assert actual.equals(expected_map)


def test_move_guard_down():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", "v", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    expected_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", "X", "."],
            [".", ".", "v", "."],
            [".", ".", ".", "."]
        ]
    )
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(1, 2),
                         direction_of_travel=Direction.DOWN,
                         is_on_map=True
                         )
    actual = guard_map.go_down_or_rotate()
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
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(1, 2),
                         direction_of_travel=Direction.DOWN,
                         is_on_map=True
                         )
    actual = guard_map.go_down_or_rotate()
    assert actual.equals(expected_map)
    assert guard_map.get_direction_of_travel() == Direction.LEFT


def test_move_guard_leaves_grid_to_bottom():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", "v", "."]
        ]
    )
    expected_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", "X", "."]
        ]
    )
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(3, 2),
                         direction_of_travel=Direction.DOWN,
                         is_on_map=True
                         )
    actual = guard_map.go_down_or_rotate()
    assert actual.equals(expected_map)
    assert guard_map.is_on_map == False


def test_move_guard_left():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", "<", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    expected_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", "<", "X", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(1, 2),
                         direction_of_travel=Direction.LEFT,
                         is_on_map=True
                         )
    actual = guard_map.go_left_or_rotate()
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
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(1, 2),
                         direction_of_travel=Direction.LEFT,
                         is_on_map=True
                         )
    actual = guard_map.go_left_or_rotate()
    assert actual.equals(expected_map)
    assert guard_map.get_direction_of_travel() == Direction.UP


def test_move_guard_leaves_grid_to_left():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            ["<", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    expected_map = DataFrame(
        [
            [".", ".", ".", "."],
            ["X", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )
    guard_map = GuardMap(current_map=current_map,
                         guard_location=(1, 0),
                         direction_of_travel=Direction.LEFT,
                         is_on_map=True
                         )
    actual = guard_map.go_left_or_rotate()
    assert actual.equals(expected_map)
    assert guard_map.is_on_map == False

