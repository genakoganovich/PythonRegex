import re
import util_7


def make_regex():
    return r'.{5}$'


def make_regex_out():
    return r'^.{5}'


def make_replacement(match_obj):
    if match_obj[0]:
        return re.search(make_regex_out(), match_obj.string)[0]


def make_result(regex, make_replacement_func, string):
    return re.sub(regex, make_replacement_func, string)


def print_lazy_solution(input_string):
    print(re.sub(input_string[-5:], input_string[0:5], input_string))


print(make_result(make_regex(), make_replacement, input()))
# util_7.test('7.5.input.txt', util_7.make_result, make_regex(), make_replacement)
