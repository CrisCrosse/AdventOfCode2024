from pandas import DataFrame
from day_6.task_two import GuardMapWithBlockerPlacement
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
    assert actual_loop_count == 6


# there is another edge case where you pass by an obstacle on the right, but you never hit it, so you never

def test_move_guard_until_leaves_grid_bypass_an_obstacle_on_the_right():
    current_map = DataFrame(
        [
            ["#", ".", ".", ".", ".", ".", ".", "v", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", ".", ".", "."]
        ]
    )
    expected = DataFrame(
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
    guard_map = GuardMapWithBlockerPlacement(current_map=current_map,
                                             guard_location=(0, 7),
                                             direction_of_travel=Direction.DOWN,
                                             is_on_map=True
                                             )
    actual = guard_map.move_guard_until_leaves_grid()
    actual_loop_count = guard_map.get_potential_loop_count()

    assert actual.equals(expected)
    assert actual_loop_count == 0
