from day_6.Direction import Direction
from day_6.task_one_helpers import rotate_90_degrees_clockwise
from day_6.task_two_helpers import clockwise_slice_contains_previously_hit_blocker, guard_is_not_about_to_leave_map
# the smallest part of the problem is:
# finding places along the guard path
# , where one can turn right 90 degrees, and you hit an obstacle on the same face as in the normal path
# ie an X then an obstacle

# guard move
# at each square, check the 90 degree offshoot clockwise
# for index in row (or column) check if current index is an X and next is an #
# if so current square is a potential blocker position, add 1 to count

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
            if clockwise_slice_contains_previously_hit_blocker(
                    *self.get_map_properties_other_than_is_on_map())\
                    and guard_is_not_about_to_leave_map(*self.get_map_properties_other_than_is_on_map()) & not_before_existing_blocker:
                new_loop_count = self.get_potential_loop_count() + 1
                map_to_view = self.get_current_map()
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


    def guard_will_return_to_start_point(self):
        while self.is_on_map:
            self.get_next_map_position_and_update_self()
            if self.guard_is_back_at_start() & guard_is_not_about_to_leave_map(*self.get_map_properties_other_than_is_on_map()):
                return True
        return False


def main():
    guard_map = GuardMapWithBlockerPlacement(None, None, Direction.UP, True)
    guard_map.move_guard_until_leaves_grid()
    # 2220 too high
    print(guard_map.get_potential_loop_count())

if __name__ == '__main__':
    main()