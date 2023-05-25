import re
import util_4_5


def make_regex():
    return r'\b[аА][а-яА-ЯёЁ]*\b'


def make_replacement(match_obj):
    return f'удалено({str(len(match_obj[0]))})'


def make_result(regex, make_replacement_func, string):
    return re.sub(regex, make_replacement_func, string)


print(make_result(make_regex(), make_replacement, input()))
# util_4_5.test('4.5.2.input.txt', util_4_5.make_result, make_regex(), make_replacement)
