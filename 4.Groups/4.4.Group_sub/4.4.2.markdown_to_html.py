import re
import util_4_4


def make_regex():
    return r'(?<!\*)\*([a-zA-Zа-яА-ЯёЁ ]+)\*(?!\*)|(?:\*\*([a-zA-Zа-яА-ЯёЁ ]+)\*\*)'


def make_replacement(match_obj):
    if match_obj.group(1):
        return fr'<em>{match_obj.group(1)}</em>'
    if match_obj.group(2):
        return fr'<strong>{match_obj.group(2)}</strong>'


def make_result(regex, make_replacement_func, sting):
    return re.sub(regex, make_replacement_func, sting)


# print(make_result(make_regex(),make_replacement, input()))
util_4_4.test('4.4.2.input.txt', make_result, make_regex(), make_replacement)
