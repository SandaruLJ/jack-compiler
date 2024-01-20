from enum import Enum


class VariableKind(Enum):
    STATIC = 0
    FIELD = 1
    ARG = 2
    VAR = 3
