import re, sys


def test(file_name, build_regex_func, replace):
    sys.stdin = open(file_name, 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    result = None

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 1:
            result = re.sub(build_regex_func(), replace, args_buffer.pop(0))

        if args_count == 2:
            args_count = 0
            try:
                line = args_buffer[0]
                assert result == args_buffer.pop(0)
                print(f"{line} replace ok")
            except AssertionError:
                print(f"{line} replace NOT ok")


def test_name(file_name, build_regex_func, replace):
    sys.stdin = open(file_name, 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    result = None

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 2:
            result = re.sub(build_regex_func(args_buffer.pop(0)), replace, args_buffer.pop(0))

        if args_count == 3:
            args_count = 0
            try:
                line = args_buffer[0]
                assert result == args_buffer.pop(0)
                print(f"{line} replace ok")
            except AssertionError:
                print(result)
                print(f"{line} replace NOT ok")

