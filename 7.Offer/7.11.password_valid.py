import re
import util_7


def make_pattern():
    return re.compile(r'\w{6,}', re.I)


def make_result(pattern, string):
    return str(bool(pattern.fullmatch(string)) and '_' not in string)


# print(make_result(make_pattern(), input()))
util_7.test_vc('7.11.input.txt', make_result, make_pattern())
