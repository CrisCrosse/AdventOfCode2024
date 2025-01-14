from pandas import DataFrame
from day_6.task_two import GuardMapWithBlockerPlacement, GuardMapLoopChecker
from day_6.Direction import Direction


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
    guard_map = GuardMapWithBlockerPlacement(current_map=current_map,
                                             guard_location=(6, 4),
                                             direction_of_travel=Direction.UP,
                                             is_on_map=True
                                             )
    actual = guard_map.move_guard_until_leaves_grid()
    actual_loop_count = guard_map.get_potential_loop_count()

    assert actual.equals(expected)
    # this was working because every time the guard hit a blocker the blocker to the right had not been hit yet
    assert actual_loop_count == 6


def test_loop_checker():
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
    guard_map = GuardMapLoopChecker(current_map=current_map,
                                    guard_location=guard_location,
                                    direction_of_travel=direction_of_travel,
                                    is_on_map=True
                                    )
    actual = guard_map.guard_will_return_to_start_point()

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
    guard_map = GuardMapLoopChecker(current_map=current_map,
                                    guard_location=guard_location,
                                    direction_of_travel=direction_of_travel,
                                    is_on_map=True
                                    )
    actual = guard_map.guard_will_return_to_start_point()

    assert actual == expected


def test_move_guard_until_leaves_grid_bypass_an_obstacle_on_the_right():
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
    guard_map = GuardMapLoopChecker(current_map=current_map,
                                    guard_location=(1, 3),
                                    direction_of_travel=Direction.RIGHT,
                                    is_on_map=True
                                    )
    expected = False

    actual = guard_map.guard_will_return_to_start_point()
    assert actual == expected


def test_move_guard_until_leaves_grid_bypass_an_obstacle_on_the_right_but_rejoin_path():
    current_map = DataFrame(
        [
            [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "X", "X", ">", ".", ".", ".", ".", ".", "."],
            [".", "X", ".", ".", ".", ".", ".", ".", ".", "."],
            ["#", "X", "X", "X", "X", "X", "#", ".", ".", "."],
            [".", "X", ".", "#", ".", "X", ".", ".", ".", "."],
            ["#", "X", "X", "X", "X", "X", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "#", ".", ".", ".", "."]
        ]
    )
    guard_map = GuardMapLoopChecker(current_map=current_map,
                                    guard_location=(1, 3),
                                    direction_of_travel=Direction.RIGHT,
                                    is_on_map=True
                                    )
    expected = True

    actual = guard_map.guard_will_return_to_start_point()
    assert actual == expected
