import re, sys


def build_regex():
    term = r'(?:[0-9]+|[0-9]*x|[0-9]*x\^[0-9])'
    return rf'[+-]?{term}(?:[+-]{term})*'


def test():
    sys.stdin = open('3.5.5.input.txt', 'r')
    args_buffer = []
    args_count = 0
    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1
        if args_count == 2:
            args_count = 0
            try:
                line = args_buffer[0]
                assert str(bool(re.fullmatch(build_regex(), args_buffer.pop(0)))) == args_buffer.pop(0)
            except AssertionError:
                print(line)


def run():
    print(bool(re.fullmatch(build_regex(), input())))


test()
