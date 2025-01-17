from day_6.Direction import Direction
from day_6.task_two import main, GuardMapWithLoopCounter
from pandas import DataFrame


def test_main_infinite_loop_debug():
    main()



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
    guard_map = GuardMapWithLoopCounter(current_map=current_map,
                                        guard_location=(6, 4),
                                        direction_of_travel=Direction.UP,
                                        is_on_map=True
                                        )
    actual = guard_map.move_guard_until_leaves_grid()
    actual_loop_count = guard_map.get_loop_count()

    assert actual.equals(expected)
    assert actual_loop_count == 6