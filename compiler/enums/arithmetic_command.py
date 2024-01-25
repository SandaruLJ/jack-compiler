from enum import Enum


class ArithmeticCommand(Enum):
    ADD = 'add'
    SUB = 'sub'
    NEG = 'neg'
    EQ = 'eq'
    GT = 'gt'
    LT = 'lt'
    AND = 'and'
    OR = 'or'
    NOT = 'not'
