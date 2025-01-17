from day_6.Direction import Direction
from day_6.GuardMapLoopChecker import GuardMapLoopChecker
from day_6.task_two_helpers import is_potential_loop_location
from src.day_6.task_one import GuardMap

# need to test I do not include start location as a potential block check
class GuardMapWithLoopCounter(GuardMap):
    found_loop_count: int
    def __init__(self, current_map, guard_location, direction_of_travel, is_on_map):
        super().__init__(current_map, guard_location, direction_of_travel, is_on_map)
        self.found_loop_count = 0

    def get_loop_count(self):
        return self.found_loop_count

    def set_loop_count(self, potential_loop_count):
        self.found_loop_count = potential_loop_count


    # this method moves the guard and checks each location for a potential loop if a blocker was placed ahead
    # is potential loop is intended to stop the looper being instantiated for each one --> reduce computational complexity
    def move_guard_until_leaves_grid(self):
        while self.is_on_map:
            self.get_next_map_position_and_update_self()

            if is_potential_loop_location(*self.get_map_properties_other_than_is_on_map()):

                loop_checker = GuardMapLoopChecker(*self.get_map_properties_other_than_is_on_map(), is_on_map=True)
                if loop_checker.gets_stuck_in_loop():
                    # could introduce threading and make the set method thread safe
                    new_loop_count = self.get_loop_count() + 1
                    self.set_loop_count(new_loop_count)
                    print(f"loop found, loop count is now: {new_loop_count}")
        return self.get_current_map()


def main():
    guard_map = GuardMapWithLoopCounter(None, None, Direction.UP, True)
    guard_map.move_guard_until_leaves_grid()
    # 2220 too high
    print(guard_map.get_loop_count())
#     1911 too high still :(

if __name__ == '__main__':
    main()