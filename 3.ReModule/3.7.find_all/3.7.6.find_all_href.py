import re, sys


def build_regex_tag():
    return r'<a.*?href=[\'\"].+?[\'\"]'


def build_regex_href():
    return r'(?<=href=[\'\"]).+?(?=[\'\"])'


def test(file_name, build_regex_tag_func, build_regex_href_func):
    sys.stdin = open(file_name, 'r', encoding='utf8')
    args_buffer = []
    args_count = 0
    answers_total = 0
    answers_countdown = -1
    result = None

    for line in sys.stdin:
        args_buffer.append(line.rstrip())
        args_count += 1

        if args_count == 1:
            result_tag = re.findall(build_regex_tag_func(), args_buffer.pop(0), 0)
            result = [re.search(build_regex_href_func(), tag).group() for tag in result_tag]
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
                print(line, 'ok')
            except AssertionError:
                print(line, 'not ok')

        if answers_countdown == 0:
            args_count = 0
            answers_countdown = -1


# list(map(lambda tag: print(re.search(build_regex_href(), tag).group()), re.findall(build_regex_tag(), input())))
test('3.7.6.input.txt', build_regex_tag, build_regex_href)
