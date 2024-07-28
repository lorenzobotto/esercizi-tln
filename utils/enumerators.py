from enum import Enum


class Turn(Enum):
    INTRO = 0
    QUESTION = 1
    OUTRO = 2


class Sex(Enum):
    MALE = 0
    FEMALE = 1


class Response(Enum):
    CORRECT = 0  # [True, False]
    INCORRECT = 1  # [False, True]
    UNCERTAIN = 2  # [True, True] or [False, False]
    INCOMPLETE = 3  # [True, False] but some frames are incomplete
