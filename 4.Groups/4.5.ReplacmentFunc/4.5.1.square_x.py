import re
import util_4_5


def make_regex():
    return r'\d+'


def make_replacement(match_obj):
    return int(match_obj[0]) ** 2


def make_result(regex, make_replacement_func, string):
    return re.subn(regex, make_replacement_func, string)


print(make_result(make_regex(), make_replacement, input()))
# util_4_5.test('4.5.1.input.txt', util_4_5.make_result, make_regex(), make_replacement)
