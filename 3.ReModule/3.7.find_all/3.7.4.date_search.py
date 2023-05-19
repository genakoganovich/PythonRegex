import re, sys


def build_regex():
    return r'(?:[0-9]{2}/[0-9]{2}/[0-9]{4})|(?:[0-9]{2}\.[0-9]{2}\.[0-9]{4})|(?:[0-9]{4}/[0-9]{2}/[0-9]{2})|(?:[0-9]{' \
           r'4}\.[0-9]{2}\.[0-9]{2})'


def test():
    sys.stdin = open('3.7.4.input.txt', 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    answers_total = 0
    answers_countdown = -1
    result = None

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 1:
            result = re.findall(build_regex(), args_buffer.pop(0), 0)
        if args_count == 2:
            try:
                answers_total = int(args_buffer[0])
                answers_countdown = answers_total
                assert len(result) == int(args_buffer.pop(0))
            except AssertionError:
                print(f'{len(list(result))} not equal {answers_total}')

        if args_count > 2:
            answers_countdown -= 1
            try:
                line = args_buffer[0]
                assert result.pop(0) == args_buffer.pop(0)
            except AssertionError:
                print(line)

        if answers_countdown == 0:
            args_count = 0
            answers_countdown = -1


list(map(lambda x: print(x), re.findall(build_regex(), input(), 0)))
# test()
