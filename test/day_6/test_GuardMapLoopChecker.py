from pandas import DataFrame

from day_6.Direction import Direction
from day_6.GuardMapLoopChecker import GuardMapLoopChecker, GuardLocationWhenBlockerHit


def test_loop_checker_not_mutating_passed_in_map():
    passed_in_map = DataFrame(
        [
            [".", "#", ".", "."],
            [".", ".", ".", "#"],
            ["Y", "<", ".", "."],
            [".", ".", "#", "."],
        ]
    )
    expected = DataFrame(
        [
            [".", "#", ".", "."],
            [".", ".", ".", "#"],
            ["#", "^", ".", "."],
            [".", ".", "#", "."],
        ]
    )
    loop_checker = GuardMapLoopChecker(current_map=passed_in_map,
                                       guard_location=(2, 1),
                                       direction_of_travel=Direction.LEFT,
                                       is_on_map=True
                                       )
    actual = loop_checker.get_current_map()
    assert actual.equals(expected)
    assert passed_in_map.equals(actual) is False


def test_loop_checker_adjacent_to_blocker():
    current_map = DataFrame(
        [
            [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "X", "X", "X", "X", "X", "#"],
            [".", ".", ".", ".", "X", ".", ".", ".", "X", "."],
            [".", ".", "#", ".", "X", ".", ".", ".", "X", "."],
            [".", ".", ".", ".", "X", ".", ".", "#", "v", "."],
            [".", ".", ".", ".", "X", ".", ".", ".", ".", "."],
            [".", "#", ".", ".", "X", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", ".", ".", "."]
        ]
    )
    guard_location = (4, 8)
    direction_of_travel = Direction.DOWN
    expected = False
    guard_map = GuardMapLoopChecker(current_map=current_map,
                                    guard_location=guard_location,
                                    direction_of_travel=direction_of_travel,
                                    is_on_map=True
                                    )
    actual = guard_map.gets_stuck_in_loop()
    assert actual == expected


def test_loop_checker():
    current_map = DataFrame(
        [
            [".", "#", ".", "."],
            [".", "X", "X", "#"],
            ["Y", "<", "X", "."],
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
    actual = guard_map.gets_stuck_in_loop()

    assert actual == expected


def test_loop_checker_hits_an_obstacle_and_leaves():
    current_map = DataFrame(
        [
            [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "X", "X", ">", "Y", ".", ".", ".", ".", "."],
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

    actual = guard_map.gets_stuck_in_loop()
    assert actual == expected


def test_loop_checker_hits_two_obstacles_and_leaves():
    current_map = DataFrame(
        [
            [".", ".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "X", "X", ">", "Y", ".", ".", ".", ".", "."],
            [".", ".", "X", ".", ".", ".", ".", ".", ".", ".", "."],
            ["#", ".", "X", "X", "X", "X", "X", "#", ".", ".", "."],
            [".", ".", "X", ".", "#", ".", "X", ".", ".", ".", "."],
            [".", "#", "X", "X", "X", "X", "X", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "."]
        ]
    )

    loop_checker = GuardMapLoopChecker(current_map=current_map,
                                       guard_location=(1, 4),
                                       direction_of_travel=Direction.RIGHT,
                                       is_on_map=True
                                       )
    expected = False
    actual = loop_checker.gets_stuck_in_loop()

    assert actual == expected


def test_loop_checker_not_returning_to_start_point():
    current_map = DataFrame(
        [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "#", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", ".", "."],
            [".", ".", ".", ".", "Y", ".", ".", ".", ".", "."],
            [".", "#", ".", ".", "^", ".", ".", "#", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
        ]
    )
    guard_map = GuardMapLoopChecker(current_map=current_map,
                                    guard_location=(7, 4),
                                    direction_of_travel=Direction.UP,
                                    is_on_map=True
                                    )
    expected = True

    actual = guard_map.gets_stuck_in_loop()
    assert actual == expected


def test_loop_checker_false_initial_blocker_interferes_with_path():
    current_map = DataFrame(
        [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "#", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "Y", ".", ".", "#", ".", "."],
            [".", "#", ".", ".", "^", ".", ".", "#", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
        ]
    )
    guard_map = GuardMapLoopChecker(current_map=current_map,
                                    guard_location=(6, 4),
                                    direction_of_travel=Direction.UP,
                                    is_on_map=True
                                    )
    expected = False

    actual = guard_map.gets_stuck_in_loop()
    assert actual == expected


def test_move_to_next_location_and_record_blockers_hit():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            ["#", "v", ".", "."],
            [".", "Y", ".", "."],
        ]
    )
    guard_location = (2, 1)
    direction_of_travel = Direction.DOWN
    added_initial_blocker = GuardLocationWhenBlockerHit(location=(2, 1), direction=Direction.DOWN)
    expected_blocker = GuardLocationWhenBlockerHit(location=(2, 1), direction=Direction.LEFT)
    expected = [added_initial_blocker, expected_blocker]

    guard_map = GuardMapLoopChecker(current_map=current_map,
                                    guard_location=guard_location,
                                    direction_of_travel=direction_of_travel,
                                    is_on_map=True
                                    )
    guard_map.move_to_next_location_and_record_blockers_hit()

    actual = guard_map.get_previously_hit_blockers()
    assert actual == expected


def test_gets_stuck_in_loop_false_blocker_hits_tested():
    # Y is where the blocker could be placed, and we are checking for a loop as a result
    current_map = DataFrame(
        [
            [".", "#", ".", ".", "."],
            [".", ".", ".", "#", "."],
            ["#", ".", ".", "v", "."],
            [".", ".", ".", "Y", "."]
        ]
    )
    guard_location = (2, 3)
    direction_of_travel = Direction.DOWN

    added_initial_blocker = GuardLocationWhenBlockerHit(location=(2, 3), direction=Direction.DOWN)
    first_blocker = GuardLocationWhenBlockerHit(location=(2, 1), direction=Direction.LEFT)
    second_blocker = GuardLocationWhenBlockerHit(location=(1, 1), direction=Direction.UP)
    third_blocker = GuardLocationWhenBlockerHit(location=(1, 2), direction=Direction.RIGHT)

    expected = False
    expected_hit_blockers = [added_initial_blocker, first_blocker, second_blocker, third_blocker]

    loop_checker = GuardMapLoopChecker(current_map=current_map,
                                       guard_location=guard_location,
                                       direction_of_travel=direction_of_travel,
                                       is_on_map=True
                                       )
    actual = loop_checker.gets_stuck_in_loop()
    actual_hit_blockers = loop_checker.get_previously_hit_blockers()

    assert actual == expected
    assert actual_hit_blockers == expected_hit_blockers


def test_is_back_at_previously_hit_blocker():
    current_map = DataFrame(
        [
            [".", "#", ".", ".", "."],
            [".", ".", ".", "#", "."],
            ["#", ".", ".", "v", "."],
            [".", ".", ".", "Y", "."]
        ]
    )
    loop_checker = GuardMapLoopChecker(current_map=current_map,
                                       guard_location=(2, 3),
                                       direction_of_travel=Direction.DOWN,
                                       is_on_map=True
                                       )
    loop_checker.add_to_previously_hit_blockers(guard_location=(2, 3), direction=Direction.LEFT)
    expected = True
    actual = loop_checker.is_back_at_previously_hit_blocker()
    assert actual == expected


def test_is_back_at_previously_hit_blocker_returns_false():
    current_map = DataFrame(
        [
            [".", "#", ".", ".", "."],
            [".", ".", ".", "#", "."],
            ["#", ".", ".", "v", "."],
            [".", ".", ".", "Y", "."]
        ]
    )
    loop_checker = GuardMapLoopChecker(current_map=current_map,
                                       guard_location=(2, 3),
                                       direction_of_travel=Direction.DOWN,
                                       is_on_map=True
                                       )
    expected = False
    actual = loop_checker.is_back_at_previously_hit_blocker()
    assert actual == expected



# are there any cases where you can get to a point of a previously hit blocker and not be a loop?
# I thought not because we are checking for the direction as well