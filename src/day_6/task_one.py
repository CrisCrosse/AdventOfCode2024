from pandas import DataFrame
from day_6.Direction import Direction
from day_6.task_one_helpers import get_next_set_of_map_features


class GuardMap:
    current_map: DataFrame
    guard_location: tuple[int, int]  # (y co-ord or row index, x co-ord or column index) OPPOSITE TO conventional maths
    direction_of_travel: Direction
    is_on_map: bool

    def __init__(self,
                 current_map: DataFrame = None,
                 guard_location: tuple[int, int] = None,
                 direction_of_travel: Direction = Direction.UP,
                 is_on_map: bool = True
                 ):
        if current_map is None:
            self.set_current_map(get_starting_map_from_input())
        else:
            self.set_current_map(current_map)
        if guard_location is None:
            self.set_guard_location(self.get_starting_guard_location_from_map())
        else:
            self.set_guard_location(guard_location)
        self.direction_of_travel = direction_of_travel
        self.is_on_map = is_on_map

    def set_current_map(self, current_map: DataFrame) -> None:
        self.current_map = current_map

    def set_guard_location(self, guard_location: tuple[int, int]) -> None:
        self.guard_location = guard_location

    def set_direction_of_travel(self, direction_of_travel: Direction) -> None:
        self.direction_of_travel = direction_of_travel

    def set_is_on_map(self, is_on_map: bool) -> None:
        self.is_on_map = is_on_map

    def get_current_map(self) -> DataFrame:
        return self.current_map

    def get_guard_location(self) -> tuple[int, int]:
        return self.guard_location

    def get_direction_of_travel(self) -> Direction:
        return self.direction_of_travel

    def get_is_on_map(self) -> bool:
        return self.is_on_map

    def get_map_properties_other_than_on_map(self) -> tuple[DataFrame, tuple[int, int], Direction]:
        return (
            self.get_current_map(),
            self.get_guard_location(),
            self.get_direction_of_travel(),
        )

    def set_map_properties(self,
                           new_map: DataFrame,
                           new_guard_location: tuple[int, int],
                           new_direction_of_travel: Direction,
                           is_on_map: bool
                           ) -> None:
        self.set_current_map(new_map)
        self.set_guard_location(new_guard_location)
        self.set_direction_of_travel(new_direction_of_travel)
        self.set_is_on_map(is_on_map)

    def get_starting_guard_location_from_map(self) -> tuple[int, int]:
        starting_map = self.get_current_map()
        for row_number, row in starting_map.iterrows():
            for column_number, column in enumerate(row):
                if column == "^":
                    return row_number, int(column_number)
        raise Exception("No guard found on map")

    def move_guard_until_leaves_grid(self):
        while self.is_on_map:
            self.get_next_map_position_and_update_self()
            map_for_viewing = self.get_current_map()
        return self.get_current_map()

    def get_next_map_position_and_update_self(self) -> None:
        self.set_map_properties(
            *get_next_set_of_map_features(self.get_current_map(),
                                          self.get_guard_location(),
                                          self.get_direction_of_travel()
                                          )
        )


def get_starting_map_from_input() -> DataFrame:
    with open('/Users/chris.rossell/projects/AdventOfCode2024/AdventOfCode2024/src/day_6/input.txt') as f:
        lines = f.readlines()
    lines_split_by_char = [list(line.strip()) for line in lines]
    return DataFrame(lines_split_by_char)


def count_x_in_df(df: DataFrame) -> int:
    return df.apply(lambda x: x.str.count("X")).sum().sum()


if __name__ == "__main__":
    guard_map = GuardMap()
    guard_map.move_guard_until_leaves_grid()
    map_where_guard_left = guard_map.get_current_map()
    print(count_x_in_df(map_where_guard_left))
