from enum import Enum
from copy import deepcopy


class Direction(str, Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"

    def deep_copy(self):
        return deepcopy(self)


direction_symbols = {
    Direction.UP: "^",
    Direction.DOWN: "v",
    Direction.RIGHT: ">",
    Direction.LEFT: "<"
}
