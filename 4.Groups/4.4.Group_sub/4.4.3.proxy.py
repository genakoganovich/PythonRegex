import re
import util_4_4


def make_regex():
    return r'((?:\d+\.){3}\d+:\d+)'


def make_replace():
    return r'http://\1'


def make_result(found):
    return found


def make_found(make_regex_func, make_replace_func, string):
    return re.sub(make_regex_func(), make_replace_func(), string)


print(make_result(make_found(make_regex, make_replace, input())))
# util_4_4.test('4.4.3.input.txt', make_result, make_found, make_regex, make_replace)
