import re
import util_4_4


def make_regex():
    return r'([0-9]+[₽$])'


def make_replacement():
    return r'Цена данного товара \1'


def make_result(regex, replacement, string):
    match = re.search(regex, string)
    return match.expand(replacement) if match else ''


util_4_4.test_446('4.4.6.input.txt', make_regex(), make_replacement())
# print(make_result(make_regex(), make_replacement(), input()))
