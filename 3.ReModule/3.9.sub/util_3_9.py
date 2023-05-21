import re, sys, json, functools


def test(file_name, build_regex_func):
    sys.stdin = open(file_name, 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    result = None

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 1:
            result = re.sub(build_regex_func(), args_buffer.pop(0))

        if args_count == 2:
            args_count = 0
            try:
                line = args_buffer[0]
                sentences = json.loads(args_buffer.pop(0))
                assert functools.reduce(lambda x, y: x and y,
                                        map(lambda p, q: p == q, result, sentences), True)
                print(f"{line} split ok")
            except AssertionError:
                print(f"CAN'T split {line}")


def test_full_name(file_name, build_regex_func):
    sys.stdin = open(file_name, 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    result = None

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 1:
            result = re.sub(build_regex_func(), args_buffer.pop(0))

        if args_count == 2:
            args_count = 0
            try:
                line = args_buffer[0]
                sentences = json.loads(args_buffer.pop(0))
                assert functools.reduce(lambda x, y: x and y,
                                        map(lambda p, q: p == q, result, sentences), True)
                print(f"{line} split ok")
            except AssertionError:
                print(f"CAN'T split {line}")
