from dataclasses import dataclass

from day_6.Direction import Direction
from day_6.task_one import GuardMap
from day_6.task_one_helpers import rotate_90_degrees_clockwise, get_next_set_of_map_features, get_next_guard_location
from day_6.task_two_helpers import move_was_a_rotation

@dataclass
class MapPositionWhenBlockerHit:
    location: tuple[int, int]
    direction: Direction

class GuardMapLoopChecker(GuardMap):
    is_back_at_start_point: bool
    start_point: tuple[int, int]
    previously_hit_blockers: list[MapPositionWhenBlockerHit]

    def __init__(self, current_map, guard_location, direction_of_travel, is_on_map):
        super().__init__(current_map, guard_location, direction_of_travel, is_on_map)
        # remove once new implementation done
        self.is_back_at_start_point = False
        self.start_point = guard_location
        # add starting blocker to map, list of hit blockers and set direction of travel to 90 degrees
        self.account_for_starting_blocker(current_map, guard_location, direction_of_travel)


    def account_for_starting_blocker(self, current_map, guard_location, direction_of_travel):
        hit_location = MapPositionWhenBlockerHit(guard_location, direction_of_travel)
        self.previously_hit_blockers = [hit_location]
        self.set_direction_of_travel(rotate_90_degrees_clockwise(direction_of_travel))
        starting_blocker_position = get_next_guard_location(guard_location, direction_of_travel)
        current_map.iloc[starting_blocker_position] = "#"
        self.set_current_map(current_map)


    def get_is_back_at_start_point(self):
        return self.is_back_at_start_point

    def set_is_back_at_start_point(self, is_back_at_start_point):
        self.is_back_at_start_point = is_back_at_start_point

    def get_start_point(self):
        return self.start_point

    def get_previously_hit_blockers(self):
        return self.previously_hit_blockers

    def add_to_previously_hit_blockers(self, guard_location: tuple[int, int], direction: Direction):
        blockers = self.get_previously_hit_blockers()
        new_blocker = MapPositionWhenBlockerHit(guard_location, direction)
        updated_blockers = blockers.append(new_blocker)
        return updated_blockers


    def guard_is_back_at_start(self):
        return self.get_guard_location() == self.get_start_point()


    def gets_stuck_in_loop(self):
        while self.is_on_map:
            self.move_to_next_location_and_record_blockers_hit()
            if self.is_back_at_previously_hit_blocker():
                return True
        return False


    def move_to_next_location_and_record_blockers_hit(self):
        current_map, current_guard_location, current_direction = self.get_map_properties_other_than_is_on_map()
        next_map, next_guard_location, next_direction, is_on_map = get_next_set_of_map_features(current_map, current_guard_location, current_direction)

        if move_was_a_rotation(current_direction, next_direction):
            self.add_to_previously_hit_blockers(current_guard_location, current_direction)

        self.set_map_properties(next_map, next_guard_location, next_direction, is_on_map)


    def is_back_at_previously_hit_blocker(self):
        current_guard_location = self.get_guard_location()
        current_direction = self.get_direction_of_travel()

        for blocker in self.get_previously_hit_blockers():
            if current_guard_location == blocker.location and current_direction == blocker.direction:
                return True



