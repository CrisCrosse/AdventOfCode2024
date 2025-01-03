from pandas import DataFrame

from day_6.Direction import Direction


class GuardMap:
    current_map: DataFrame
    guard_location: tuple[int, int]
    direction_of_travel: Direction
    is_on_map: bool


    def __init__(self,
                 current_map: DataFrame = None,
                 guard_location: tuple[int, int] = None,
                 direction_of_travel: Direction = Direction.UP,
                 is_on_map: bool = True
                 ):
        if current_map:
            self.set_current_map(current_map)
        else:
            self.set_current_map(get_starting_map_from_input())
        self.guard_location = guard_location
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


    def move_guard(self) -> DataFrame:
        print(self.is_on_map)
        return self.current_map


    def get_starting_guard_location_from_map(self) -> tuple[int, int]:
        starting_map = self.get_current_map()
        for row_number, row in starting_map.iterrows():
            for column_number, column in row.iteritems():
                if column == "^":
                    return int(row.index), int(column_number)


def get_starting_map_from_input() -> DataFrame:
    with open('/Users/chris.rossell/projects/AdventOfCode2024/AdventOfCode2024/src/day_6/input.txt') as f:
        lines = f.readlines()
    lines_split_by_char = [list(line.strip()) for line in lines]
    return DataFrame(lines_split_by_char)



def move_guard(current_map: DataFrame, guard_location: tuple[int, int], direction_of_travel: Direction, is_on_map: bool) -> DataFrame:
    print(is_on_map)
    return current_map
