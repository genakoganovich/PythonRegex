import re
import util_7


def make_regex():
    return r'(\$[0-9]+)|([0-9]+(?:,[0-9]+)?дюйм(?:а|ов))'


def make_replacement(match_obj):
    if match_obj[1]:
        return f'{str(match_obj[1][0]).upper()}{str(match_obj[1][1:]).lower()}'
    if match_obj[2]:
        return f'{str(match_obj[2][0]).upper()}{str(match_obj[2][1:-1]).lower()}'


def make_result(regex, make_replacement_func, string):
    return re.sub(regex, make_replacement_func, string)


print(make_result(make_regex(), make_replacement, input()))
util_7.test('7.4.input.txt', util_7.make_result, make_regex(), make_replacement)
