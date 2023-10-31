from enum import Enum


class Direction(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4


class State(Enum):
    SUCCESS = 1
    LOSS = 2
    IN_PROGRESS = 3
