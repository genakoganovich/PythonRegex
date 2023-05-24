import re, sys


def test(file_name, make_result_func, make_found_func, make_regex_func):
    sys.stdin = open(file_name, 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    answers_countdown = -1
    result = None

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 1:
            result = make_result_func(make_found_func(make_regex_func, args_buffer.pop(0)))

        if args_count == 2:
            answers_total = int(args_buffer[0])
            answers_countdown = answers_total

            try:
                assert len(result) == int(args_buffer.pop(0))
            except AssertionError:
                print(f'{len(list(result))} not equal {answers_total}')

        if args_count > 2:
            answers_countdown -= 1
            line = args_buffer[0]

            try:

                assert result.pop(0) == args_buffer.pop(0)
                print(line, 'ok')
            except AssertionError:
                print(line, 'not ok')

        if answers_countdown == 0:
            args_count = 0
            answers_countdown = -1
