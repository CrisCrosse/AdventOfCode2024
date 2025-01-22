from day_6.Direction import Direction
from day_6.GuardMapLoopChecker import GuardMapLoopChecker
from day_6.task_one_helpers import get_starting_map_from_input
from src.day_6.task_one import GuardMap

class GuardMapWithLoopCounter(GuardMap):
    visited_locations: set[tuple[int, int]]
    found_loop_count: int

    def __init__(self, current_map, guard_location, direction_of_travel, is_on_map):
        super().__init__(current_map, guard_location, direction_of_travel, is_on_map)
        self.found_loop_count = 0
        self.visited_locations = set()

    def get_loop_count(self):
        return self.found_loop_count

    def set_loop_count(self, potential_loop_count):
        self.found_loop_count = potential_loop_count

    def add_to_visited_locations(self, location: tuple[int, int]):
        self.visited_locations.add(location)


    def add_all_visited_positions_at_the_start(self):
        while self.is_on_map:
            self.get_next_map_position_and_update_self()
            self.add_to_visited_locations(self.get_guard_location())


    def loop_checker(self):
        # this currently matches every single visited block
        visited_on_this_loop_check = {(self.get_guard_location(), self.get_direction_of_travel())}
        while self.is_on_map:
            self.get_next_map_position_and_update_self()
            current_state = (self.get_guard_location(), self.get_direction_of_travel())
            if current_state in visited_on_this_loop_check:
                return True
            visited_on_this_loop_check.add(current_state)
        return False

    def try_all_visited_blocks_for_loop(self, visited_blocks: set[tuple[int, int]]):
        loop_count = 0
        starting_map = get_starting_map_from_input()
        self.set_current_map(starting_map)
        starting_location =  self.get_starting_guard_location_from_map()
        starting_direction = Direction.UP
        starting_on_map = True

        for block in visited_blocks:
            self.set_current_map(starting_map)
            self.current_map.iloc[block] = "#"
            self.set_guard_location(starting_location)
            self.set_direction_of_travel(starting_direction)
            self.set_is_on_map(starting_on_map)
            if self.loop_checker():
                loop_count += 1
                print(f"loop found, loop count is now: {loop_count}")
        self.set_loop_count(loop_count)



    def instantiate_loop_checker(self) -> GuardMapLoopChecker:
        current_map = self.get_current_map().copy()
        guard_location = self.get_guard_location()[::]
        direction_of_travel = self.get_direction_of_travel().deep_copy()
        return GuardMapLoopChecker(current_map, guard_location, direction_of_travel, is_on_map=True)


def main():
    guard_map = GuardMapWithLoopCounter(None, None, Direction.UP, True)
    guard_map.add_all_visited_positions_at_the_start()
    guard_map.try_all_visited_blocks_for_loop(guard_map.visited_locations)
    print(guard_map.get_loop_count())
# 1748 is correct

if __name__ == '__main__':
    main()