from typing import Optional

from pandas import DataFrame

from day_6.Direction import Direction


def get_next_set_of_map_features(current_map: DataFrame,
                                 current_guard_location: tuple[int, int],
                                 current_direction: Direction
                                 ) -> tuple[DataFrame, tuple[int, int], Direction, Optional[bool]]:
    projected_guard_location = get_next_guard_location(current_guard_location, current_direction)
    new_map = current_map.copy()
    direction_symbols = {
        Direction.UP: "^",
        Direction.DOWN: "v",
        Direction.RIGHT: ">",
        Direction.LEFT: "<"
    }
    is_on_map = True

    if is_next_guard_location_out_of_bounds(projected_guard_location, current_map):
        is_on_map = False
        new_map.iloc[current_guard_location] = "X"
        direction_for_next_map = current_direction
        guard_location_for_next_map = current_guard_location

    elif new_map.iloc[projected_guard_location] == "#":
        direction_for_next_map = rotate_90_degrees_clockwise(current_direction)
        new_map.iloc[current_guard_location] = direction_symbols[direction_for_next_map]
        guard_location_for_next_map = current_guard_location

    else:
        new_map.iloc[current_guard_location] = "X"
        new_map.iloc[projected_guard_location] = direction_symbols[current_direction]
        direction_for_next_map = current_direction
        guard_location_for_next_map = projected_guard_location

    return new_map, guard_location_for_next_map, direction_for_next_map, is_on_map


def rotate_90_degrees_clockwise(current_direction: Direction) -> Direction:
    rotation_directions = {
        Direction.UP: Direction.RIGHT,
        Direction.RIGHT: Direction.DOWN,
        Direction.DOWN: Direction.LEFT,
        Direction.LEFT: Direction.UP
    }
    return rotation_directions[current_direction]


def get_next_guard_location(guard_location: tuple[int, int], current_direction: Direction) -> tuple[int, int]:
    next_guard_location = {
        Direction.UP: (guard_location[0] - 1, guard_location[1]),
        Direction.DOWN: (guard_location[0] + 1, guard_location[1]),
        Direction.RIGHT: (guard_location[0], guard_location[1] + 1),
        Direction.LEFT: (guard_location[0], guard_location[1] - 1)
    }
    return next_guard_location[current_direction]


def is_next_guard_location_out_of_bounds(next_guard_location: tuple[int, int], current_map: DataFrame) -> bool:
    out_of_bounds_to_top = next_guard_location[0] < 0
    out_of_bounds_to_right = next_guard_location[1] >= current_map.shape[1]
    out_of_bounds_to_bottom = next_guard_location[0] >= current_map.shape[0]
    out_of_bounds_to_left = next_guard_location[1] < 0
    return  out_of_bounds_to_top or out_of_bounds_to_right or out_of_bounds_to_bottom or out_of_bounds_to_left


def get_starting_map_from_input() -> DataFrame:
    with open('/Users/chris.rossell/projects/AdventOfCode2024/AdventOfCode2024/src/day_6/input.txt') as f:
        lines = f.readlines()
    lines_split_by_char = [list(line.strip()) for line in lines]
    return DataFrame(lines_split_by_char)


def count_x_in_df(df: DataFrame) -> int:
    return df.apply(lambda x: x.str.count("X")).sum().sum()
