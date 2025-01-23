from day_6.Direction import Direction
from day_6.task_two import main, GuardMapWithLoopCounter
from pandas import DataFrame


def test_main_infinite_loop_debug():
    main()


def test_loop_counter_does_not_count_start_location():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", "^", ".", "#"],
            ["#", ".", ".", "."],
            [".", ".", "#", ""]
        ]
    )
    expected = 0
    expected_visited = {(0, 1)}
    loop_counter = GuardMapWithLoopCounter(current_map=current_map,
                                           guard_location=(1, 1),
                                           direction_of_travel=Direction.UP,
                                           is_on_map=True
                                           )
    loop_counter.add_all_visited_positions_at_the_start()
    actual_visited = loop_counter.visited_locations

    assert actual_visited == expected_visited

    loop_counter.try_all_visited_blocks_for_loop(loop_counter.visited_locations)
    actual = loop_counter.get_loop_count()


    assert actual == expected


def test_loop_checker_returns_false_when_leaving_map():
    current_map = DataFrame(
        [
            [".", "^", ".", "."],
            [".", ".", ".", "#"],
            ["#", ".", ".", "."],
            [".", ".", "#", ""]
        ]
    )
    expected = False
    loop_counter = GuardMapWithLoopCounter(current_map=current_map,
                                           guard_location=(0, 1),
                                           direction_of_travel=Direction.UP,
                                           is_on_map=True
                                           )
    actual = loop_counter.loop_checker()
    assert actual == expected


def test_loop_checker_returns_false_when_leaving_map_right():
    current_map = DataFrame(
        [
            [".", ".", ".", ">"],
            [".", ".", ".", "#"],
            ["#", ".", ".", "."],
            [".", ".", "#", ""]
        ]
    )
    expected = False
    loop_counter = GuardMapWithLoopCounter(current_map=current_map,
                                           guard_location=(0, 3),
                                           direction_of_travel=Direction.RIGHT,
                                           is_on_map=True
                                           )
    actual = loop_counter.loop_checker()
    assert actual == expected


def test_loop_checker_returns_false_when_leaving_map_down():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "#"],
            ["#", ".", ".", "."],
            [".", "v", "#", ""]
        ]
    )
    expected = False
    loop_counter = GuardMapWithLoopCounter(current_map=current_map,
                                           guard_location=(3, 1),
                                           direction_of_travel=Direction.DOWN,
                                           is_on_map=True
                                           )
    actual = loop_counter.loop_checker()
    assert actual == expected


def test_loop_checker_returns_false_when_leaving_map_left():
    current_map = DataFrame(
        [
            [".", ".", ".", "."],
            [".", ".", ".", "#"],
            ["#", ".", ".", "."],
            ["<", ".", "#", ""]
        ]
    )
    expected = False
    loop_counter = GuardMapWithLoopCounter(current_map=current_map,
                                           guard_location=(3, 0),
                                           direction_of_travel=Direction.LEFT,
                                           is_on_map=True
                                           )
    actual = loop_counter.loop_checker()
    assert actual == expected



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