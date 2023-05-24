import re
import util_4_2


def make_regex():
    return r'([0-9]+):([a-zA-Z0-9]+):([a-z0-9]+)'


def make_result(found):
    return list(found).__repr__()


def make_found(make_regex_func, line):
    return re.findall(make_regex_func(), line)


print(make_result(make_found(make_regex, input())))
# util_4_2.test('4.2.2.input.txt', make_result, make_found, make_regex)
