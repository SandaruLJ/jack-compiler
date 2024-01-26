"""VM code writer module of the compiler

Classes:
    VmWriter
"""

class VmWriter:
    """VmWriter class of the jack compiler.

    Features a set of simple routines for writing
    VM commands into the output file.

    Properties:
        output: file object representing the output

    Methods:
        write_push(Segment, int) -> None
        write_pop(Segment, int) -> None
        write_arithmetic(ArithmeticCommand) -> None
        write_label(str) -> None
        write_goto(str) -> None
        write_if(str) -> None
        write_call(str, int) -> None
        write_call(str, int) -> None
        write_return() -> None
        close() -> None
    """

    def __init__(self, filename):
        self.output = open(filename, 'w')

    def write_push(self, segment, index):
        """Write a VM push command"""
        self.output.write(f'push {segment.value} {index}\n')

    def write_pop(self, segment, index):
        """Write a VM pop command"""
        self.output.write(f'pop {segment.value} {index}\n')

    def write_arithmetic(self, command):
        """Write a VM arithmetic-logical command"""
        self.output.write(f'{command.value}\n')

    def write_label(self, label):
        """Write a VM label command"""
        self.output.write(f'label {label}\n')

    def write_goto(self, label):
        """Write a VM goto command"""
        self.output.write(f'goto {label}\n')

    def write_if(self, label):
        """Write a VM if-goto command"""
        self.output.write(f'if-goto {label}\n')

    def write_call(self, name, num_args):
        """Write a VM call command"""
        self.output.write(f'call {name} {num_args}\n')

    def write_function(self, name, num_vars):
        """Write a VM function command"""
        self.output.write(f'function {name} {num_vars}\n')

    def write_return(self):
        """Write a VM return command"""
        self.output.write('return\n')

    def close(self):
        """Close the output file"""
        self.output.close()
