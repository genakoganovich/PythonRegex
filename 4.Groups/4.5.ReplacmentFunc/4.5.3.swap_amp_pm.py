import re
import util_4_5


def make_regex():
    return r'(am)|(pm)'


def make_replacement(match_obj):
    if match_obj[1]:
        return 'pm'
    if match_obj[2]:
        return 'am'


def make_result(regex, make_replacement_func, string):
    return re.sub(regex, make_replacement_func, string)


print(make_result(make_regex(), make_replacement, input()))
# util_4_5.test('4.5.3.input.txt', util_4_5.make_result, make_regex(), make_replacement)
