from day_6.Direction import Direction
from day_6.task_one_helpers import rotate_90_degrees_clockwise
from day_6.task_two_helpers import clockwise_slice_contains_blocker, guard_is_not_about_to_leave_map
from src.day_6.task_one import GuardMap

class GuardMapWithBlockerPlacement(GuardMap):
    potential_loop_count: int
    def __init__(self, current_map, guard_location, direction_of_travel, is_on_map):
        super().__init__(current_map, guard_location, direction_of_travel, is_on_map)
        self.potential_loop_count = 0

    def get_potential_loop_count(self):
        return self.potential_loop_count

    def set_potential_loop_count(self, potential_loop_count):
        self.potential_loop_count = potential_loop_count

    def move_guard_until_leaves_grid(self):
        while self.is_on_map:
            self.get_next_map_position_and_update_self()

            if clockwise_slice_contains_blocker(*self.get_map_properties_other_than_is_on_map()) \
                    and guard_is_not_about_to_leave_map(*self.get_map_properties_other_than_is_on_map()):
                # massive increase in time complexity
                print("potential loop found")
                loop_checker = GuardMapLoopChecker(*self.get_map_properties_other_than_is_on_map(), is_on_map=True)
                if loop_checker.guard_will_get_stuck_in_loop_if_blocker_placed_ahead():
                    new_loop_count = self.get_potential_loop_count() + 1
                    print(f"loop found, loop count is now: {new_loop_count}")
                    self.set_potential_loop_count(new_loop_count)
        return self.get_current_map()


class GuardMapLoopChecker(GuardMap):
    is_back_at_start_point: bool
    start_point: tuple[int, int]
    
    def __init__(self, current_map, guard_location, direction_of_travel, is_on_map):
        super().__init__(current_map, guard_location, direction_of_travel, is_on_map)
        self.is_back_at_start_point = False
        self.start_point = guard_location
        # check if a blocker was placed ahead causing a 90 degree turn
        self.direction_of_travel = rotate_90_degrees_clockwise(direction_of_travel)

    def get_is_back_at_start_point(self):
        return self.is_back_at_start_point

    def set_is_back_at_start_point(self, is_back_at_start_point):
        self.is_back_at_start_point = is_back_at_start_point

    def get_start_point(self):
        return self.start_point

    def guard_is_back_at_start(self):
        return self.get_guard_location() == self.get_start_point()


    def guard_will_get_stuck_in_loop_if_blocker_placed_ahead(self):
        while self.is_on_map:
            self.get_next_map_position_and_update_self()
            if self.guard_is_back_at_start():
                return True
        return False


def main():
    guard_map = GuardMapWithBlockerPlacement(None, None, Direction.UP, True)
    guard_map.move_guard_until_leaves_grid()
    # 2220 too high
    print(guard_map.get_potential_loop_count())

if __name__ == '__main__':
    main()