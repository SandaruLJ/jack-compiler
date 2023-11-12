"""Module for storing constants used in the Jack compiler"""

symbols = [
    '{', '}', '(', ')', '[', ']',
    '.', ',', ';',
    '+', '-', '*', '/',
    '&', '|', '<', '>', '=', '~',
]


class TokenType:
    KEYWORD = 'KEYWORD'
    SYMBOL = 'SYMBOL'
    IDENTIFIER = 'IDENTIFIER'
    INT_CONST = 'INT_CONST'
    STRING_CONST = 'STRING_CONST'


class KeywordType:
    CLASS = 'CLASS'
    METHOD = 'METHOD'
    FUNCTION = 'FUNCTION'
    CONSTRUCTOR = 'CONSTRUCTOR'
    INT = 'INT'
    BOOLEAN = 'BOOLEAN'
    CHAR = 'CHAR'
    VOID = 'VOID'
    VAR = 'VAR'
    STATIC = 'STATIC'
    FIELD = 'FIELD'
    LET = 'LET'
    DO = 'DO'
    IF = 'IF'
    ELSE = 'ELSE'
    WHILE = 'WHILE'
    RETURN = 'RETURN'
    TRUE = 'TRUE'
    FALSE = 'FALSE'
    NULL = 'NULL'
    THIS = 'THIS'


keywords = {
    'class': KeywordType.CLASS,
    'constructor': KeywordType.CONSTRUCTOR,
    'function': KeywordType.FUNCTION,
    'method': KeywordType.METHOD,
    'field': KeywordType.FIELD,
    'static': KeywordType.STATIC,
    'var': KeywordType.VAR,
    'int': KeywordType.INT,
    'char': KeywordType.CHAR,
    'boolean': KeywordType.BOOLEAN,
    'void': KeywordType.VOID,
    'true': KeywordType.TRUE,
    'false': KeywordType.FALSE,
    'null': KeywordType.NULL,
    'this': KeywordType.THIS,
    'let': KeywordType.LET,
    'do': KeywordType.DO,
    'if': KeywordType.IF,
    'else': KeywordType.ELSE,
    'while': KeywordType.WHILE,
    'return': KeywordType.RETURN,
}
