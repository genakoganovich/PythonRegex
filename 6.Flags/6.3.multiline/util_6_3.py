import sys


def test_long_string(file_name, make_result_func, regex):
    sys.stdin = open(file_name, 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    input_size = 0
    result = None

    for line in sys.stdin:
        args_buffer.append(line)
        args_count += 1

        if args_count == 1:
            input_size = int(args_buffer.pop(0).rstrip())

        if args_count == input_size:
            args_count = 0
            input_size = 0
            result = make_result_func(regex, ''.join(args_buffer[:-1]))
            del args_buffer[:-1]
            try:
                assert result == args_buffer.pop(0).rstrip()
                print(f'{result} is ok')
            except AssertionError:
                print(f'{result} is NOT ok')