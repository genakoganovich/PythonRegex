import re
import util_7


def make_regex():
    value = r'([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
    return r'\.'.join([f'{value}' for i in range(4)])


def make_result(regex, string):
    return str(bool(re.match(regex, string)))


print(make_result(make_regex(), input()))
# util_7.test_vc('7.8.input.txt', make_result, make_regex())
