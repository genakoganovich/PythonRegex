import re
import util_7


def make_regex():
    return r'([A-Z][a-z]*(?=\s|$))|([A-Z][a-z]*(?=[A-Z]|[0-9]))'


def make_replacement(match_obj):
    if match_obj[1]:
        return str(match_obj[1]).lower()
    if match_obj[2]:
        return f'{str(match_obj[2]).lower()}_'


def make_result(regex, make_replacement_func, string):
    return re.sub(regex, make_replacement_func, string)


print(make_result(make_regex(), make_replacement, input()))
# util_7.test('7.1.input.txt', util_7.make_result, make_regex(), make_replacement)
