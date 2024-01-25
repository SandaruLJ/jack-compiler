from enum import Enum


class Segment(Enum):
    CONSTANT = 'constant'
    ARGUMENT = 'argument'
    LOCAL = 'local'
    STATIC = 'static'
    THIS = 'this'
    THAT = 'that'
    POINTER = 'pointer'
    TEMP = 'temp'
