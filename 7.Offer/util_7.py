import sys, re


def make_result(regex, make_replacement_func, string):
    return re.sub(regex, make_replacement_func, string)


def test(file_name, make_result_func, regex, make_replace_func):
    sys.stdin = open(file_name, 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    result = None

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 1:
            result = make_result_func(regex, make_replace_func, args_buffer.pop(0))

        if args_count == 2:
            args_count = 0

            try:
                assert result == args_buffer.pop(0)
                print(f'{result} is ok')
            except AssertionError:
                print(f'{result} is NOT ok')


def test_vc(file_name, make_result_func, regex):
    sys.stdin = open(file_name, 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    result = None
    string = None

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 1:
            string = args_buffer[0]
            result = make_result_func(regex, args_buffer.pop(0))

        if args_count == 2:
            args_count = 0

            try:
                assert result == args_buffer.pop(0)
                print(f'{string} is ok')
            except AssertionError:
                print(f'{string} is NOT ok')
