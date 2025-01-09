import pytest
from pandas import DataFrame
from day_6.Direction import Direction
from day_6.task_one_helpers import rotate_90_degrees_clockwise, get_next_guard_location, \
    is_next_guard_location_out_of_bounds, get_next_set_of_map_features


def test_rotate_90_degrees_clockwise_up():
    expected = Direction.RIGHT
    actual = rotate_90_degrees_clockwise(Direction.UP)
    assert actual == expected


def test_rotate_90_degrees_clockwise_right():
    expected = Direction.DOWN
    actual = rotate_90_degrees_clockwise(Direction.RIGHT)
    assert actual == expected


def test_rotate_90_degrees_clockwise_down():
    expected = Direction.LEFT
    actual = rotate_90_degrees_clockwise(Direction.DOWN)
    assert actual == expected


def test_rotate_90_degrees_clockwise_left():
    expected = Direction.UP
    actual = rotate_90_degrees_clockwise(Direction.LEFT)
    assert actual == expected


def test_get_next_guard_location_up():
    expected = (0, 1)
    actual = get_next_guard_location((1, 1), Direction.UP)
    assert actual == expected


def test_get_next_guard_location_down():
    expected = (2, 1)
    actual = get_next_guard_location((1, 1), Direction.DOWN)
    assert actual == expected


def test_get_next_guard_location_right():
    expected = (1, 2)
    actual = get_next_guard_location((1, 1), Direction.RIGHT)
    assert actual == expected


def test_get_next_guard_location_left():
    expected = (1, 0)
    actual = get_next_guard_location((1, 1), Direction.LEFT)
    assert actual == expected


@pytest.fixture
def current_map() -> DataFrame:
    return DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
    )

def test_is_next_guard_location_out_of_bounds_returns_false_at_upper_left_limit(current_map):
    expected = False
    next_guard_location = (0,0)
    actual = is_next_guard_location_out_of_bounds(next_guard_location, current_map)
    assert actual == expected


def test_is_next_guard_location_out_of_bounds_returns_false_at_lower_right_limit(current_map):
    expected = False
    next_guard_location = (3, 3)
    actual = is_next_guard_location_out_of_bounds(next_guard_location, current_map)
    assert actual == expected


def test_is_next_guard_location_out_of_bounds_to_top(current_map):
    expected = True
    next_guard_location = (-1, 0)
    actual = is_next_guard_location_out_of_bounds(next_guard_location, current_map)
    assert actual == expected


def test_is_next_guard_location_out_of_bounds_to_bottom(current_map):
    expected = True
    next_guard_location = (4, 0)
    actual = is_next_guard_location_out_of_bounds(next_guard_location, current_map)
    assert actual == expected


def test_is_next_guard_location_out_of_bounds_to_left(current_map):
    expected = True
    next_guard_location = (0, -1)
    actual = is_next_guard_location_out_of_bounds(next_guard_location, current_map)
    assert actual == expected


def test_is_next_guard_location_out_of_bounds_to_right(current_map):
    expected = True
    next_guard_location = (0, 4)
    actual = is_next_guard_location_out_of_bounds(next_guard_location, current_map)
    assert actual == expected


# test_get_next_guard_location

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
    actual = get_next_set_of_map_features(current_map,
                                          (3,2),
                                          Direction.UP)
    assert actual[0].equals(expected_map)
    assert actual[1:] == ((2,2), Direction.UP, True)


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
    actual = get_next_set_of_map_features(current_map,
                                          (1, 2),
                                          Direction.UP)
    assert actual[0].equals(expected_map)
    assert actual[1:] == ((1, 2), Direction.RIGHT, True)


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
    actual = get_next_set_of_map_features(current_map,
                                          (0, 2),
                                          Direction.UP)
    assert actual[0].equals(expected_map)
    assert actual[1:] == ((0, 2), Direction.UP, False)


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
    actual = get_next_set_of_map_features(current_map,
                                          (1, 2),
                                          Direction.RIGHT)
    assert actual[0].equals(expected_map)
    assert actual[1:] == ((1, 3), Direction.RIGHT, True)


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
    actual = get_next_set_of_map_features(current_map,
                                          (1, 3),
                                          Direction.RIGHT)
    assert actual[0].equals(expected_map)
    assert actual[1:] == ((1, 3), Direction.RIGHT, False)


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
    actual = get_next_set_of_map_features(current_map,
                                          (1, 2),
                                          Direction.RIGHT)
    assert actual[0].equals(expected_map)
    assert actual[1:] == ((1, 2), Direction.DOWN, True)


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
    actual = get_next_set_of_map_features(current_map,
                                          (1, 2),
                                          Direction.DOWN)
    assert actual[0].equals(expected_map)
    assert actual[1:] == ((2, 2), Direction.DOWN, True)



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
    actual = get_next_set_of_map_features(current_map,
                                          (1, 2),
                                          Direction.DOWN)
    assert actual[0].equals(expected_map)
    assert actual[1:] == ((1, 2), Direction.LEFT, True)


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
    actual = get_next_set_of_map_features(current_map,
                                          (3, 2),
                                          Direction.DOWN)
    assert actual[0].equals(expected_map)
    assert actual[1:] == ((3, 2), Direction.DOWN, False)


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
    actual = get_next_set_of_map_features(current_map,
                                          (1, 2),
                                          Direction.LEFT)
    assert actual[0].equals(expected_map)
    assert actual[1:] == ((1, 1), Direction.LEFT, True)


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
    actual = get_next_set_of_map_features(current_map,
                                          (1, 2),
                                          Direction.LEFT)
    assert actual[0].equals(expected_map)
    assert actual[1:] == ((1, 2), Direction.UP, True)


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
    actual = get_next_set_of_map_features(current_map,
                                          (1, 0),
                                          Direction.LEFT)
    assert actual[0].equals(expected_map)
    assert actual[1:] == ((1, 0), Direction.LEFT, False)

# could test different sizes of grid


