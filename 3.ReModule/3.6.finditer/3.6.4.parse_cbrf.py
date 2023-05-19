import re, sys


def build_regex():
    return r'[0-9,]+ ₽'


def test():
    sys.stdin = open('3.6.4.input.txt', 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    answers_total = 0
    answers_countdown = -1
    result = None

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 1:
            print(args_buffer[0])
            result = re.finditer(build_regex(), args_buffer.pop(0), 0)
        if args_count == 2:
            try:
                answers_total = int(args_buffer[0])
                answers_countdown = answers_total
                print(f'answers_total = {answers_total}')
                print(f'len(list(result)) = {len(list(result))}')
                assert len(list(result)) == int(args_buffer.pop(0))
            except AssertionError:
                print(f'{len(list(result))} not equal {answers_total}')

        if args_count > 2:
            answers_countdown -= 1
            try:
                line = args_buffer[0]
                assert next(result).group() == args_buffer.pop(0)
                print(line, 'ok')
            except AssertionError:
                print(line)

        if answers_countdown == 0:
            answers_countdown = -1
            args_count = 0
            result = None


# list(map(lambda x: print(x.group()), list(re.finditer(build_regex(), input(), 0))))
test()