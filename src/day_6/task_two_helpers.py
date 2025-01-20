from typing import Optional

from pandas import DataFrame

from day_6.Direction import Direction, direction_symbols
from day_6.task_one_helpers import is_next_guard_location_out_of_bounds, get_next_guard_location, \
    rotate_90_degrees_clockwise


# have missed an edge case where the guard is at the edge of the map, a blocker cannot be placed ahead of them because the blocker would be off the map
def clockwise_slice_contains_blocker(current_map: DataFrame,
                                     guard_location: tuple[int, int],
                                     direction_of_travel: Direction
                                     ) -> bool:
    clockwise_slice = get_slice_perpendicular_to_direction(current_map, guard_location, direction_of_travel)
    for index, value in enumerate(clockwise_slice):
        if index == len(clockwise_slice) - 1:
            return False
        if clockwise_slice[index + 1] == "#":
            return True


def get_slice_perpendicular_to_direction(current_map: DataFrame,
                                         guard_location: tuple[int, int],
                                         direction_of_travel: Direction
                                         ) -> list:
    row_index = guard_location[0]
    column_index = guard_location[1]

    if direction_of_travel == Direction.UP:
        whole_row = current_map.iloc[row_index].tolist()
        return whole_row[column_index:]

    elif direction_of_travel == Direction.DOWN:
        whole_row = current_map.iloc[row_index].tolist()
        # reverse so that X precedes #
        return whole_row[column_index::-1]

    elif direction_of_travel == Direction.RIGHT:
        whole_column = current_map.iloc[:, column_index].tolist()
        return whole_column[row_index:]

    elif direction_of_travel == Direction.LEFT:
        whole_column = current_map.iloc[:, column_index].tolist()
        # reverse so that X precedes #
        return whole_column[row_index::-1]


def guard_is_about_to_leave_map(current_map, current_guard_location, current_direction):
    projected_guard_location = get_next_guard_location(current_guard_location, current_direction)
    return is_next_guard_location_out_of_bounds(projected_guard_location, current_map)


def guard_is_not_about_to_leave_map(current_map, current_guard_location, current_direction):
    return not guard_is_about_to_leave_map(current_map, current_guard_location, current_direction)


# think this is unneccessary, if the next move was a blocker and it satisfies next perpendicular slice is hit blocker then it is in a loop,?
def next_move_is_blocker(current_map, guard_location, direction_of_travel):
    next_guard_location = get_next_guard_location(guard_location, direction_of_travel)
    try:
        next_value = current_map.iloc[next_guard_location]
    except IndexError:
        return False
    value_is_blocker = next_value == "#"
    return value_is_blocker


def next_move_is_not_blocker(current_map, guard_location, direction_of_travel):
    return not next_move_is_blocker(current_map, guard_location, direction_of_travel)


def is_potential_loop_location(current_map, guard_location, direction_of_travel):
    return (next_move_is_not_blocker(current_map, guard_location, direction_of_travel)
            & guard_is_not_about_to_leave_map(current_map, guard_location, direction_of_travel)
            & clockwise_slice_contains_blocker(current_map, guard_location, direction_of_travel)
            )


def next_move_is_blocker_again(current_map, guard_location, direction_of_travel):
    return not next_move_is_not_blocker(current_map, guard_location, direction_of_travel)


def move_was_a_rotation(current_direction, next_direction) -> bool:
    return current_direction != next_direction


def get_next_set_of_map_features_for_loop_checker(current_map: DataFrame,
                                                  current_guard_location: tuple[int, int],
                                                  current_direction: Direction
                                                  ) -> tuple[DataFrame, tuple[int, int], Direction, Optional[bool]]:
    projected_guard_location = get_next_guard_location(current_guard_location, current_direction)
    new_map = current_map.copy()
    is_on_map = True

    if is_next_guard_location_out_of_bounds(projected_guard_location, current_map):
        is_on_map = False
        new_map.iloc[current_guard_location] = "Y"
        direction_for_next_map = current_direction
        guard_location_for_next_map = current_guard_location

    elif new_map.iloc[projected_guard_location] == "#":
        direction_for_next_map = rotate_90_degrees_clockwise(current_direction)
        new_map.iloc[current_guard_location] = direction_symbols[direction_for_next_map]
        guard_location_for_next_map = current_guard_location

    else:
        new_map.iloc[current_guard_location] = "Y"
        new_map.iloc[projected_guard_location] = direction_symbols[current_direction]
        direction_for_next_map = current_direction
        guard_location_for_next_map = projected_guard_location

    return new_map, guard_location_for_next_map, direction_for_next_map, is_on_map
