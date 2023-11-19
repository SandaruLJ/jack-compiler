"""Compilation engine module of the compiler

Classes:
    CompilationEngine
"""

import sys

from constants import TerminalElement


class CompilationEngine:
    """CompilationEngine class of the Jack compiler.

    Emits a structured representation of the input source code
    wrapped in XML tags.

    Gets input from a Tokenizer and emits output to a file.
    Output is generated by a series of compile_xxx functions, each designed to
    handle the compilation of a specific Jack langugage construct xxx.
    Each compile_xxx function should get from the input, and handle,
    all the tokens that make up xxx, advance the Tokenizer exactly beyond these
    tokens, and output the parsing of xxx.

    Properties:
        input: input stream of tokens
        output: file object of the output

    Methods:
        compile_class() -> None
        compile_class_var_dec() -> None
        compile_subroutine() -> None
        compile_parameter_list() -> None
        compile_subroutine_body() -> None
        compile_var_dec() -> None
    """

    def __init__(self, tokenizer, filename):
        self.input = tokenizer
        self.output = open(filename, 'w')

    def __del__(self):
        self.output.close()

    def _eat(self, token):
        token_type = getattr(TerminalElement, self.input.token_type())

        if self.input.current_token != token:
            print('Invalid token.')
            sys.exit(1)
        else:
            if token == '<':
                token = '&lt;'
            elif token == '>':
                token = '&gt;'
            elif token == '&':
                token = '&amp;'

            self.output.write(f'<{token_type}> {token} </{token_type}>\n')
            self.input.advance()

    def compile_class(self):
        """Compile a complete class"""
        self.output.write('<class>\n')

        self._eat('class')
        self._eat(self.input.current_token)  # className
        self._eat('{')

        while self.input.current_token in ('static', 'field'):
            self.compile_class_var_dec()
        while self.input.current_token in ('constructor', 'function', 'method'):
            self.compile_subroutine()

        self._eat('}')

        self.output.write('</class>\n')

    def compile_class_var_dec(self):
        """Compile a static or field variable declaration"""
        self.output.write('<classVarDec>\n')

        self._eat(self.input.current_token)  # 'static'|'field'
        self._eat(self.input.current_token)  # type
        self._eat(self.input.current_token)  # varName

        # if a comma is present, that means there are more variables
        while self.input.current_token == ',':
            self._eat(',')
            self._eat(self.input.current_token)  # varName

        self._eat(';')

        self.output.write('</classVarDec>\n')

    def compile_subroutine(self):
        """Compile a complete method, function, or constructor"""
        self.output.write('<subroutineDec>\n')

        self._eat(self.input.current_token)  # 'constructor'|'function'|'method'
        self._eat(self.input.current_token)  # 'void'|type
        self._eat(self.input.current_token)  # subroutineName
        self._eat('(')
        self.compile_parameter_list()
        self._eat(')')
        self.compile_subroutine_body()

        self.output.write('</subroutineDec>\n')

    def compile_parameter_list(self):
        """Compile a (possibly empty) parameter list"""
        self.output.write('<parameterList>\n')

        if self.input.current_token != ')':
            self._eat(self.input.current_token)  # type
            self._eat(self.input.current_token)  # varName

            # the presence of a comma means that there are more parameters
            while self.input.current_token == ',':
                self._eat(',')
                self._eat(self.input.current_token)  # type
                self._eat(self.input.current_token)  # varName

        self.output.write('</parameterList>\n')

    def compile_subroutine_body(self):
        """Compile a subroutine's body"""
        self.output.write('<subroutineBody>\n')

        self._eat('{')
        while self.input.current_token == 'var':
            self.compile_var_dec()
        self.compile_statements()
        self._eat('}')

        self.output.write('</subroutineBody>\n')

    def compile_var_dec(self):
        """Compile a variable declaration"""
        self.output.write('<varDec>\n')

        self._eat('var')
        self._eat(self.input.current_token)  # type
        self._eat(self.input.current_token)  # varName

        # check for and compile more variable names
        while self.input.current_token == ',':
            self._eat(',')
            self._eat(self.input.current_token)  # varName

        self._eat(';')

        self.output.write('</varDec>\n')

    def compile_statements(self):
        pass
