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
        index_counts: dictionary with the index count of each variable kind

    Methods:
        reset() -> None
    """

    def __init__(self):
        self.symbol_table = {}
        self.index_counts = {}

    def reset(self):
        """Empty the symbol table, and reset the four indexes to 0.
        Should be called when starting to compile a subroutine declaration.
        """
        self.symbol_table = {}
        self.index_counts = {
            VariableKind.STATIC: 0,
            VariableKind.FIELD: 0,
            VariableKind.ARG: 0,
            VariableKind.VAR: 0,
        }
