import re, sys


def build_regex():
    return r'\b[a-zA-Zа-яА-ЯёЁ]{5}\b'


def test():
    sys.stdin = open('3.6.3.input.txt', 'r')
    args_buffer = []
    args_count = 0
    answers_total = 0
    answers_countdown = 0
    result = None

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 1:
            result = re.finditer(build_regex(), args_buffer.pop(0), 0)
        if args_count == 2:
            try:
                answers_total = args_buffer[0]
                answers_countdown = answers_total
                assert len(list(result)) == int(args_buffer.pop(0))
            except AssertionError:
                print(f'{len(list(result))} not equal {answers_total}')

        if args_count > 2:
            answers_countdown -= 1
            try:
                line = args_buffer[0]
                assert next(result).group() == args_buffer.pop(0)
            except AssertionError:
                print(line)

        if answers_countdown == 0:
            args_count = 0


list(map(lambda x: print(x.group()), list(re.finditer(build_regex(), input(), 0))))
