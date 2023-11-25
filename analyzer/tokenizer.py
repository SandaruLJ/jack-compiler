"""Tokenizer module of the compiler

Classes:
    Tokenizer
"""

from constants import keywords, symbols, TokenType


class Tokenizer:
    """Tokenizer class of Jack compiler.
    
    Handles the parsing of input stream/file into tokens:

    Ignores all comments and white space in the input steam
    and enables accessing the input one token at a time.
    Also parses and provides the type of each token.

    Properties:
        file: file object containing the Jack source code
        current_token: the Jack token currenly being processed

    Methods:
        advance() -> bool
        token_type() -> strz
        get_token() -> str
    """

    def __init__(self, filename):
        self.file = open(filename, encoding='utf-8')
        self.current_token = ''

    def __del__(self):
        self.file.close()

    def advance(self):
        """Get the next token from the input, and make it the current token.
        Return True if a token was found, False otherwise.
        """
        self.current_token = ''

        while char := self.file.read(1):
            # handle string constants
            if self.current_token and self.current_token.startswith('"'):
                self.current_token += char
                if char == '"':
                    return True
                continue

            # ignore whitespace
            if char in (' ', '\n', '\t'):
                if self.current_token:
                    return True
                continue

            # look ahead next character
            next_char = self.file.read(1)
            self.file.seek(self.file.tell() - 1)  # restore to current position

            # ignore comments
            if f'{char}{next_char}'  in ('//', '/*'):
                if self.current_token:
                    return True
                if f'{char}{next_char}' == '/*':
                    while char:= self.file.read(1):
                        if char == '*':
                            if self.file.read(1) == '/':
                                break;
                else:
                    self.file.readline()
                continue

            # check for symbols
            if char in symbols:
                self.current_token = char
                return True
            elif next_char in symbols:
                self.current_token += char
                return True

            self.current_token += char

        return False

    def token_type(self):
        """Return the type of the current token."""
        if self.current_token.startswith('"'):
            return TokenType.STRING_CONST
        if self.current_token in keywords:
            return TokenType.KEYWORD
        if self.current_token in symbols:
            return TokenType.SYMBOL
        if self.current_token[0].isdigit():
            return TokenType.INT_CONST
        return TokenType.IDENTIFIER

    def get_token(self):
        """Return the current token."""
        if self.token_type() == TokenType.STRING_CONST:
            return self.current_token.strip('"')
        if self.token_type() == TokenType.KEYWORD:
            return keywords[self.current_token]
        return self.current_token
