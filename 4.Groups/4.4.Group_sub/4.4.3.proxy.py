import re
import util_4_4


def make_regex():
    return r'((?:\d+\.){3}\d+:\d+)'


def make_replacement(match_obj):
    if match_obj.group(1):
        return fr'http://{match_obj.group(1)}'


# print(util_4_4.make_result(make_regex(), make_replacement, input()))
util_4_4.test('4.4.3.input.txt', util_4_4.make_result, make_regex(), make_replacement)
