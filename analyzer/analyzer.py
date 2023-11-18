"""Main module of the syntax analyzer"""

import os
import sys

from tokenizer import Tokenizer
from compilation_engine import CompilationEngine
from constants import TerminalElement


SOURCE_EXT = 'jack'
TARGET_EXT = 'xml'


def main():
    """Entrypoint of the syntax analyzer"""
    if len(sys.argv) != 2:
        print('Usage: program <Source>.jack || program <source_dir>')
        sys.exit(1)

    source = sys.argv[1]
    is_dir = os.path.isdir(source)

    # determine source and target files according to user input
    if is_dir:
        # get all files with the extension '.vm' in the specified source directory
        source_files = [file.path for file in os.scandir(source)
                        if file.path.split('.')[-1] == SOURCE_EXT]
        absolute_path = os.path.abspath(source)
        target_file = f'{absolute_path}/{os.path.basename(absolute_path)}.{TARGET_EXT}'
    else:
        source_files = [source]
        target_file = _parse_filename(source)[0] + f'.{TARGET_EXT}'

    # TODO: Replace with actual code
    for source_file in source_files:
        filename, ext = _parse_filename(source_file)

        # check if filename and extension is valid
        if not (filename or filename[0].isupper() or ext != SOURCE_EXT):
            print(f'Invalid filename format: {filename}.{ext}')
            sys.exit(1)

        # create tokenizer instance for each source file
        tokenizer = Tokenizer(source_file)

        # write tokenized output
        with open(f'{filename}T.{TARGET_EXT}', 'w') as output:
            output.write('<tokens>\n')
            
            while tokenizer.advance():
                token_type = getattr(TerminalElement, tokenizer.token_type())
                token = tokenizer.current_token
                
                if token == '<':
                    token = '&lt;'
                elif token == '>':
                    token = '&gt;'
                elif token == '&':
                    token = '&amp;'
                
                output.write(f'<{token_type}> {token} </{token_type}>\n')
            
            output.write('</tokens>\n')
            output.close()


def _parse_filename(file):
    split_filename = file.split('.')

    filename = ''.join(split_filename[0:-1])
    ext = split_filename[-1]

    return filename, ext


if __name__ == '__main__':
    main()
