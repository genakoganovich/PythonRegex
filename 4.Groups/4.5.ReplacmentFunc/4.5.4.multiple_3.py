import re
import util_4_5


def make_regex():
    return r'\d*'


def make_replacement(match_obj):
    if match_obj[0]:
        if int(match_obj[0]) % 3 == 0:
            return str(int(match_obj[0]) // 3)
        else:
            return match_obj[0]


def make_result(regex, make_replacement_func, string):
    return re.sub(regex, make_replacement_func, string)


# print(make_result(make_regex(), make_replacement, input()))
util_4_5.test('4.5.4.input.txt', util_4_5.make_result, make_regex(), make_replacement)
