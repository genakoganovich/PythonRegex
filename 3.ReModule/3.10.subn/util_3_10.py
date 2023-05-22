import re, sys


def test(file_name, build_regex_func, replace):
    sys.stdin = open(file_name, 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    result = None
    replacements_count = 0

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 1:
            result, replacements_count = re.subn(build_regex_func(), replace, args_buffer.pop(0))

        if args_count == 2:
            args_count = 0
            try:
                line = args_buffer[0]
                assert replacements_count == int(args_buffer.pop(0))
                print(f"{line} replace ok")
            except AssertionError:
                print(f"{line} replace NOT ok")


def test_tuple(file_name, build_regex_func, replace):
    sys.stdin = open(file_name, 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    result = None

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 1:
            result = re.subn(build_regex_func(), replace, args_buffer.pop(0))

        if args_count == 2:
            args_count = 0
            try:
                line = args_buffer[0]
                assert str(result) == args_buffer.pop(0)
                print(f"{str(result)} replace ok")
            except AssertionError:
                print(f"{str(result)} replace NOT ok. Expected: {line}")

