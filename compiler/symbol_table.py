"""Symbol table module of the compiler

Classes:
    SymbolTable
"""

from enums.variable_kind import VariableKind


class SymbolTable:
    """SymbolTable class of the Jack compiler.

    Provides services for building, populating, and using symbol tables.

    Keeps track of the symbol properties' name, type, kind, and a
    running index for each kind.

    Properties:
        symbol_table: dictionary used as the symbol table data structure
        index: dictionary with the index count of each variable kind

    Methods:
        reset() -> None
        define(str, str, VariableKind) -> None
        var_count(VariableKind) -> int
        kind_of(str) -> VariableKind
        type_of(str) -> str
        index_of(str) -> int
    """

    def __init__(self):
        self.reset()

    def reset(self):
        """Empty the symbol table, and reset the four indexes to 0.
        Should be called when starting to compile a subroutine declaration.
        """
        self.symbol_table = {}
        self.index = {
            VariableKind.STATIC: 0,
            VariableKind.FIELD: 0,
            VariableKind.ARG: 0,
            VariableKind.VAR: 0,
        }

    def define(self, name, data_type, kind):
        """Define (add to the table) a new variable of the given
        name, type, and kind. Assign to it the index value of that kind,
        and add 1 to the index.
        """
        self.symbol_table[name] = {
            "type": data_type,
            "kind": kind,
            "index": self.index[kind]
        }
        self.index[kind] += 1

    def var_count(self, kind):
        """Return the number of variables in the table of the given kind"""
        return self.index[kind]

    def kind_of(self, name):
        """Return the kind of the named identifier.
        If the identifier is not found, return None.
        """
        if name in self.symbol_table:
            return self.symbol_table[name]["kind"]
        return None

    def type_of(self, name):
        """Return the type of the named variable"""
        if name in self.symbol_table:
            return self.symbol_table[name]["type"]
        return None

    def index_of(self, name):
        """Return the index of the named variable"""
        if name in self.symbol_table:
            return self.symbol_table[name]["index"]
        return None
