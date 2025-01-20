from dataclasses import dataclass

from day_6.Direction import Direction, direction_symbols
from day_6.task_one import GuardMap
from day_6.task_one_helpers import rotate_90_degrees_clockwise, get_next_guard_location
from day_6.task_two_helpers import move_was_a_rotation, get_next_set_of_map_features_for_loop_checker


@dataclass
class GuardLocationWhenBlockerHit:
    location: tuple[int, int]
    direction: Direction

class GuardMapLoopChecker(GuardMap):
    locations_where_blockers_hit: list[GuardLocationWhenBlockerHit]

    def __init__(self, current_map, guard_location, direction_of_travel, is_on_map):
        super().__init__(current_map, guard_location, direction_of_travel, is_on_map)

        # add starting blocker to map, list of hit blockers and set direction of travel to 90 degrees
        self.account_for_starting_blocker(current_map, guard_location, direction_of_travel)


    def account_for_starting_blocker(self, current_map, guard_location, direction_of_travel):
        loop_checker_map = current_map.copy()

        simulated_hit_location = GuardLocationWhenBlockerHit(guard_location, direction_of_travel)
        self.locations_where_blockers_hit = [simulated_hit_location]

        starting_blocker_position = get_next_guard_location(guard_location, direction_of_travel)
        loop_checker_map.iloc[starting_blocker_position] = "#"

        clockwise_direction = rotate_90_degrees_clockwise(direction_of_travel)
        self.set_direction_of_travel(clockwise_direction)
        loop_checker_map.iloc[guard_location] = direction_symbols[clockwise_direction]

        self.set_current_map(loop_checker_map)


    def get_previously_hit_blockers(self):
        return self.locations_where_blockers_hit

    def add_to_previously_hit_blockers(self, guard_location: tuple[int, int], direction: Direction):
        blockers = self.get_previously_hit_blockers()
        new_blocker = GuardLocationWhenBlockerHit(guard_location, direction)
        updated_blockers = blockers.append(new_blocker)
        return updated_blockers


    def gets_stuck_in_loop(self):
        while self.is_on_map:
            self.move_to_next_location_and_record_blockers_hit()
            if self.is_back_at_previously_hit_blocker():
                return True
        return False


    def move_to_next_location_and_record_blockers_hit(self):
        current_map, current_guard_location, current_direction = self.get_map_properties_other_than_is_on_map()
        next_map, next_guard_location, next_direction, is_on_map = get_next_set_of_map_features_for_loop_checker(current_map, current_guard_location, current_direction)

        if move_was_a_rotation(current_direction, next_direction):
            self.add_to_previously_hit_blockers(current_guard_location, current_direction)

        self.set_map_properties(next_map, next_guard_location, next_direction, is_on_map)


    def is_back_at_previously_hit_blocker(self):
        current_guard_location = self.get_guard_location()
        current_direction = self.get_direction_of_travel()

        for blocker in self.get_previously_hit_blockers():
            if current_guard_location == blocker.location and current_direction == blocker.direction:
                return True
        return False
