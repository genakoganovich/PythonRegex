import re
import util_4_4


def make_regex():
    return r'([еЕ]гонны[йея])|([еЕ]ённы[йея])|([иИ]хни[йея])'


def make_replacement(match_obj):
    if match_obj.group(1):
        return fr'{match_obj.group(1)[0:3]}'
    if match_obj.group(2):
        return fr'{match_obj.group(2)[0:2]}'
    if match_obj.group(3):
        return fr'{match_obj.group(3)[0:2]}'


def make_result(regex, make_replacement_func, string):
    return re.sub(regex, make_replacement_func, string)


print(make_result(make_regex(), make_replacement, input()))
# util_4_4.test('4.4.5.input.txt', util_4_4.make_result, make_regex(), make_replacement)

