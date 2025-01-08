from pandas import DataFrame
from day_6.Direction import Direction


class GuardMap:
    current_map: DataFrame
    guard_location: tuple[int, int]
    # guard_location: (y co-ord or row index, x co-ord or column index) OPPOSITE TO conventional maths
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


    def get_starting_guard_location_from_map(self) -> tuple[int, int]:
        starting_map = self.get_current_map()
        for row_number, row in starting_map.iterrows():
            for column_number, column in enumerate(row):
                    if column == "^":
                        return row_number, int(column_number)
        raise Exception("No guard found on map")


    def move_guard_until_leaves_grid(self):
        while self.is_on_map:
            self.set_current_map(self.move_or_rotate_guard())
            map_for_viewing = self.get_current_map()
        return self.get_current_map()


    def move_or_rotate_guard(self) -> DataFrame:
        if self.direction_of_travel == Direction.UP:
            return self.go_up_or_rotate()
        if self.direction_of_travel == Direction.RIGHT:
            return self.go_right_or_rotate()
        if self.direction_of_travel == Direction.LEFT:
            return self.go_left_or_rotate()
        if self.direction_of_travel == Direction.DOWN:
            return self.go_down_or_rotate()

    def go_up_or_rotate(self) -> DataFrame:
        new_map = self.get_current_map()
        guard_location = self.get_guard_location()
        next_guard_location = (guard_location[0] - 1, guard_location[1])

        if next_guard_location[0] < 0:
            new_map.iloc[guard_location] = "X"
            self.set_is_on_map(False)
            return new_map

        if new_map.iloc[next_guard_location] == "#":
            new_map.iloc[guard_location] = ">"
            self.set_direction_of_travel(Direction.RIGHT)
            return new_map

        new_map.iloc[guard_location] = "X"
        new_map.iloc[next_guard_location] = "^"
        self.set_guard_location(next_guard_location)
        return new_map


    def go_right_or_rotate(self) -> DataFrame:
        new_map = self.get_current_map()
        guard_location = self.get_guard_location()
        next_guard_location = (guard_location[0], guard_location[1] + 1)
        max_x_index = new_map.shape[1]

        if next_guard_location[1] >= max_x_index:
            new_map.iloc[guard_location] = "X"
            self.set_is_on_map(False)
            return new_map

        if new_map.iloc[next_guard_location] == "#":
            new_map.iloc[guard_location] = "v"
            self.set_direction_of_travel(Direction.DOWN)
            return new_map

        new_map.iloc[guard_location] = "X"
        new_map.iloc[next_guard_location] = ">"
        self.set_guard_location(next_guard_location)
        return new_map


    def go_down_or_rotate(self) -> DataFrame:
        new_map = self.get_current_map()
        guard_location = self.get_guard_location()
        next_guard_location = (guard_location[0] + 1, guard_location[1])
        max_y_index = new_map.shape[0]

        if next_guard_location[0] >= max_y_index:
            new_map.iloc[guard_location] = "X"
            self.set_is_on_map(False)
            return new_map

        if new_map.iloc[next_guard_location] == "#":
            new_map.iloc[guard_location] = "<"
            self.set_direction_of_travel(Direction.LEFT)
            return new_map

        new_map.iloc[guard_location] = "X"
        new_map.iloc[next_guard_location] = "v"
        self.set_guard_location(next_guard_location)
        return new_map

    def go_left_or_rotate(self) -> DataFrame:
        new_map = self.get_current_map()
        guard_location = self.get_guard_location()
        next_guard_location = (guard_location[0] , guard_location[1] - 1)

        if next_guard_location[1] < 0:
            new_map.iloc[guard_location] = "X"
            self.set_is_on_map(False)
            return new_map

        if new_map.iloc[next_guard_location] == "#":
            new_map.iloc[guard_location] = "^"
            self.set_direction_of_travel(Direction.UP)
            return new_map

        new_map.iloc[guard_location] = "X"
        new_map.iloc[next_guard_location] = "<"
        self.set_guard_location(next_guard_location)
        return new_map


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


