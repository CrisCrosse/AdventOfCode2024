from pandas import DataFrame

from day_6.Direction import Direction
from day_6.task_two_helpers import clockwise_slice_contains_blocker, \
    get_slice_perpendicular_to_direction, guard_is_not_about_to_leave_map, next_move_is_not_blocker, \
    current_guard_location_could_be_blocked_to_create_loop, is_potential_loop_location, move_was_a_rotation


def test_for_previously_hit_blocker_going_up():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            ["X", "^", "X", "#"],
            ["#", "X", "X", "."],
            [".", ".", "#", ""]
        ]
    )
    guard_location = (1, 1)
    direction_of_travel = Direction.UP
    expected = True
    actual = clockwise_slice_contains_blocker(current_map,
                                                                                     guard_location,
                                                                                     direction_of_travel
                                                                                     )
    assert actual == expected


def test_for_previously_hit_blocker_edge_case():
    current_map = DataFrame(
        [
            [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "X", "X", "X", "X", "X", "#"],
            [".", ".", ".", ".", "X", ".", ".", ".", "X", "."],
            [".", ".", "#", ".", "X", ".", ".", ".", "X", "."],
            [".", ".", "X", "X", "X", "X", "X", "#", "X", "."],
            [".", ".", "X", ".", "X", ".", "X", ".", "X", "."],
            [".", "#", "X", "X", "X", "X", "X", "X", "X", "."],
            [".", ".", ".", ".", "X", ".", "X", ".", "#", "."],
            ["#", ".", ".", ".", "<", "X", "X", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", ".", ".", "."]
        ]
    )
    guard_location = (8, 4)
    direction_of_travel = Direction.LEFT
    expected = True
    actual = clockwise_slice_contains_blocker(current_map,
                                                                                     guard_location,
                                                                                     direction_of_travel
                                                                                     )
    assert actual == expected


def test_for_previously_hit_blocker_false():
    current_map = DataFrame(
        [
            [".", "^", ".", "."],
            ["X", "X", "X", "#"],
            ["#", "X", "X", "."],
            [".", ".", "#", ""]
        ]
    )
    guard_location = (0, 1)
    direction_of_travel = Direction.UP
    expected = False
    actual = clockwise_slice_contains_blocker(current_map,
                                                                                     guard_location,
                                                                                     direction_of_travel
                                                                                     )
    assert actual == expected


def test_get_slice_perpendicular_to_up():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            ["X", "^", "X", "#"],
            ["#", "X", "X", "."],
            [".", ".", "#", ""]
        ]
    )
    guard_location = (1, 1)
    direction_of_travel = Direction.UP

    expected = ["^", "X", "#"]
    actual = get_slice_perpendicular_to_direction(current_map,
                                                  guard_location,
                                                  direction_of_travel
                                                  )
    assert actual == expected


def test_get_slice_perpendicular_to_up_on_edge():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "^"],
            [".", ".", ".", "X"],
            [".", ".", ".", "."],
        ]
    )
    guard_location = (1, 3)
    direction_of_travel = Direction.UP
    expected = ["^"]

    actual = get_slice_perpendicular_to_direction(current_map,
                                                  guard_location,
                                                  direction_of_travel
                                                  )
    assert actual == expected


def test_get_slice_perpendicular_to_down():
    current_map = DataFrame(
        [
            [".", "#", ".", "."],
            [".", "X", "X", "#"],
            ["#", "X", "v", "."],
            [".", ".", ".", "."],
        ]
    )
    guard_location = (2, 2)
    direction_of_travel = Direction.DOWN
    expected = ["v", "X", "#"]

    actual = get_slice_perpendicular_to_direction(current_map,
                                                  guard_location,
                                                  direction_of_travel
                                                  )
    assert actual == expected


def test_get_slice_perpendicular_to_down_on_edge():
    current_map = DataFrame(
        [
            [".", "#", ".", "."],
            [".", ".", ".", "."],
            ["v", ".", ".", "."],
            [".", ".", ".", "."],
        ]
    )
    guard_location = (2, 0)
    direction_of_travel = Direction.DOWN
    expected = ["v"]

    actual = get_slice_perpendicular_to_direction(current_map,
                                                  guard_location,
                                                  direction_of_travel
                                                  )
    assert actual == expected


def test_get_slice_perpendicular_to_right():
    current_map = DataFrame(
        [
            [".", "#", ".", "."],
            [".", "X", ">", "."],
            ["#", "X", "X", "."],
            [".", ".", "#", "."],
        ]
    )
    guard_location = (1, 2)
    direction_of_travel = Direction.RIGHT
    expected = [">", "X", "#"]

    actual = get_slice_perpendicular_to_direction(current_map,
                                                  guard_location,
                                                  direction_of_travel
                                                  )
    assert actual == expected


def test_get_slice_perpendicular_to_right_on_edge():
    current_map = DataFrame(
        [
            [".", "#", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", "X", ">", "."],
        ]
    )
    guard_location = (3, 2)
    direction_of_travel = Direction.RIGHT
    expected = [">"]

    actual = get_slice_perpendicular_to_direction(current_map,
                                                  guard_location,
                                                  direction_of_travel
                                                  )
    assert actual == expected


def test_get_slice_perpendicular_to_left():
    current_map = DataFrame(
        [
            [".", "#", ".", "."],
            [".", "X", "X", "#"],
            ["#", "<", "X", "."],
            [".", ".", "#", "."],
        ]
    )
    guard_location = (2, 1)
    direction_of_travel = Direction.LEFT
    expected = ["<", "X", "#"]

    actual = get_slice_perpendicular_to_direction(current_map,
                                                  guard_location,
                                                  direction_of_travel
                                                  )
    assert actual == expected


def test_get_slice_perpendicular_to_left_on_edge():
    current_map = DataFrame(
        [
            [".", "<", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
        ]
    )
    guard_location = (0, 1)
    direction_of_travel = Direction.LEFT
    expected = ["<"]

    actual = get_slice_perpendicular_to_direction(current_map,
                                                  guard_location,
                                                  direction_of_travel
                                                  )
    assert actual == expected


def test_guard_is_not_about_to_leave_map_returns_false():
    current_map = DataFrame(
        [
            [".", "^", ".", "."],
            [".", "X", "X", "#"],
            ["#", "X", "X", "."],
            [".", ".", "#", "."],
        ]
    )
    guard_location = (0, 1)
    direction_of_travel = Direction.UP
    expected = False
    actual = guard_is_not_about_to_leave_map(current_map, guard_location, direction_of_travel)
    assert actual == expected


def test_guard_is_not_about_to_leave_map_returns_true():
    current_map = DataFrame(
        [
            [".", "^", ".", "."],
            [".", "X", "X", "#"],
            ["#", "X", "X", "."],
            [".", ".", "#", "."],
        ]
    )
    guard_location = (0, 1)
    direction_of_travel = Direction.RIGHT
    expected = True
    actual = guard_is_not_about_to_leave_map(current_map, guard_location, direction_of_travel)
    assert actual == expected



def test_guard_is_not_about_to_leave_map_returns_false_lower_left_corner():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            ["<", ".", ".", "."],
        ]
    )
    guard_location = (3, 0)
    direction_of_travel = Direction.LEFT
    expected = False
    actual = guard_is_not_about_to_leave_map(current_map, guard_location, direction_of_travel)
    assert actual == expected


def test_guard_is_not_about_to_leave_map_returns_true_lower_left_corner():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            ["^", ".", ".", "."],
        ]
    )
    guard_location = (3, 0)
    direction_of_travel = Direction.UP
    expected = True
    actual = guard_is_not_about_to_leave_map(current_map, guard_location, direction_of_travel)
    assert actual == expected


def test_next_move_is_not_blocker_returns_false():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "#"],
            [".", ".", ".", "."],
            [".", ">", "#", "."],
        ]
    )
    guard_location = (3, 1)
    direction_of_travel = Direction.RIGHT
    expected = False
    actual = next_move_is_not_blocker(current_map, guard_location, direction_of_travel)
    assert actual == expected


def test_next_move_is_not_blocker_returns_true():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "#"],
            [".", ".", ".", "."],
            [".", "^", "#", "."],
        ]
    )
    guard_location = (3, 1)
    direction_of_travel = Direction.UP
    expected = True
    actual = next_move_is_not_blocker(current_map, guard_location, direction_of_travel)
    assert actual == expected


def test_current_location_valid_loop():
    current_map = DataFrame(
        [
            [".", "#", ".", "."],
            [".", "X", "X", "#"],
            [".", "<", "X", "."],
            [".", ".", "#", "."],
        ]
    )
    guard_location = (2, 1)
    direction_of_travel = Direction.LEFT
    expected = True
    actual = current_guard_location_could_be_blocked_to_create_loop(current_map, guard_location, direction_of_travel)

    assert actual == expected



def test_current_location_invalid_loop_next_to_existing_blocker():
    current_map = DataFrame(
        [
            [".", "#", "X", "."],
            [".", "^", "X", "#"],
            ["#", "X", "X", "."],
            [".", ".", "#", "."],
        ]
    )
    guard_location = (1, 1)
    direction_of_travel = Direction.UP
    expected = False
    actual = current_guard_location_could_be_blocked_to_create_loop(current_map, guard_location, direction_of_travel)

    assert actual == expected

# move to test_task_two.py once method refactored
def test_current_location_invalid_loop_would_leave():
    current_map = DataFrame(
        [
            [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "X", "X", ">", ".", ".", ".", ".", ".", "."],
            [".", "X", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "X", "X", "X", "X", "X", "#", ".", ".", "."],
            [".", "X", ".", "#", ".", "X", ".", ".", ".", "."],
            ["#", "X", "X", "X", "X", "X", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "#", ".", ".", ".", "."]
        ]
    )
    guard_location = (1, 3)
    direction_of_travel = Direction.RIGHT
    expected = False
    actual = current_guard_location_could_be_blocked_to_create_loop(current_map, guard_location, direction_of_travel)

    assert actual == expected


def test_current_location_invalid_loop_would_leave_after_two_turns():
    current_map = DataFrame(
        [
            [".",".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
            [".",".", "X", "X", ">", ".", ".", ".", ".", ".", "."],
            [".",".", "X", ".", ".", ".", ".", ".", ".", ".", "."],
            ["#",".", "X", "X", "X", "X", "X", "#", ".", ".", "."],
            [".",".", "X", ".", "#", ".", "X", ".", ".", ".", "."],
            [".","#", "X", "X", "X", "X", "X", ".", ".", ".", "."],
            [".",".", ".", ".", ".", ".", "#", ".", ".", ".", "."]
        ]
    )
    guard_location = (1, 4)
    direction_of_travel = Direction.RIGHT
    expected = False
    actual = current_guard_location_could_be_blocked_to_create_loop(current_map, guard_location, direction_of_travel)

    assert actual == expected


def test_loop_checker_no_space_before_leaves_grid():
    current_map = DataFrame(
        [
            ["#", ".", "."],
            ["X", "X", "#"],
            ["<", "X", "."],
            [".", "#", "."],
        ]
    )
    guard_location = (2, 0)
    direction_of_travel = Direction.LEFT
    expected = False
    actual = is_potential_loop_location(current_map, guard_location, direction_of_travel)

    assert actual == expected

def test_move_was_a_rotation_true():
    current_direction = Direction.UP
    next_direction = Direction.RIGHT
    expected = True
    actual = move_was_a_rotation(current_direction, next_direction)

    assert actual == expected


def test_move_was_a_rotation_false():
    current_direction = Direction.UP
    next_direction = Direction.UP
    expected = False
    actual = move_was_a_rotation(current_direction, next_direction)

    assert actual == expected