import re
import util_4_1


def make_regex():
    return r'</?([a-z0-9]+).*?>'


def make_result(found):
    return list(found).__repr__()


def make_found(make_regex_func, line):
    return re.findall(make_regex_func(), line)


print(make_result(make_found(make_regex, input())))
# util_4_1.test_413('4.1.3.input.txt', make_result, make_found, make_regex)
