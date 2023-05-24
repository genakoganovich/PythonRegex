import re
import util_4_3


def make_regex():
    return r'[^0-9]*([+:=*/-])[^0-9]*'


def make_result(found):
    return list(found).__repr__()


def make_found(make_regex_func, line):
    return re.split(make_regex_func(), line)


print(make_result(make_found(make_regex, input())))
# util_4_3.test('4.3.1.input.txt', make_result, make_found, make_regex)
