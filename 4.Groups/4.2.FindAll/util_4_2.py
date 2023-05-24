import sys


def test(file_name, make_result_func, make_found_func, make_regex_func):
    sys.stdin = open(file_name, 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    result = None

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 1:
            result = make_result_func(make_found_func(make_regex_func, args_buffer.pop(0)))

        if args_count == 2:
            args_count = 0

            try:
                assert result == args_buffer.pop(0)
                print('ok')
            except AssertionError:
                print(f'{result} is NOT ok')
