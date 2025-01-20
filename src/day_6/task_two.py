from day_6.Direction import Direction
from day_6.GuardMapLoopChecker import GuardMapLoopChecker
from day_6.task_two_helpers import is_potential_loop_location
from src.day_6.task_one import GuardMap

class GuardMapWithLoopCounter(GuardMap):
    found_loop_count: int

    def __init__(self, current_map, guard_location, direction_of_travel, is_on_map):
        super().__init__(current_map, guard_location, direction_of_travel, is_on_map)
        self.found_loop_count = 0

    def get_loop_count(self):
        return self.found_loop_count

    def set_loop_count(self, potential_loop_count):
        self.found_loop_count = potential_loop_count

    def move_guard_until_leaves_grid(self):
        loop_count = 0
        potential_blocked_locations = []
        while self.is_on_map:
            self.get_next_map_position_and_update_self()

            if is_potential_loop_location(*self.get_map_properties_other_than_is_on_map()):
                loop_checker = self.instantiate_loop_checker()
                if loop_checker.gets_stuck_in_loop():
                    map_position_of_potential_loop = loop_checker.get_previously_hit_blockers()[0]
                    potential_blocked_locations.append(map_position_of_potential_loop)
                    loop_count += 1
                    # seem to be hitting here without gets_stuck in loop returning true
                    print(f"loop found, loop count is now: {loop_count}")

        self.set_loop_count(loop_count)
        return self.get_current_map()


    def instantiate_loop_checker(self) -> GuardMapLoopChecker:
        current_map = self.get_current_map().copy()
        guard_location = self.get_guard_location()[::]
        direction_of_travel = self.get_direction_of_travel().deep_copy()
        return GuardMapLoopChecker(current_map, guard_location, direction_of_travel, is_on_map=True)


def main():
    guard_map = GuardMapWithLoopCounter(None, None, Direction.UP, True)
    guard_map.move_guard_until_leaves_grid()
    # 2220 too high
    print(guard_map.get_loop_count())
#     1911 too high still :(
# 1748 is correct

if __name__ == '__main__':
    main()