import re
import util_7


def make_regex():
    return r'(?:\b(?:01)+\b)|(?:\b(?:10)+\b)|(?:\b(?:0(?:10)+)\b)|(?:\b(?:1(?:01)+)\b)'


def make_result(regex, string):
    return ' '.join(re.findall(regex, string))


# print(make_result(make_regex(), input()))
# util_7.test('7.6.input.txt', util_7.make_result, make_regex(), make_replacement)

print(re.findall(make_regex(), input()))
