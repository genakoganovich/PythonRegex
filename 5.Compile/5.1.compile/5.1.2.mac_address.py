import re
import util_5_1


def make_regex():
    return ':'.join([r'[0-9A-F]{2}' for i in range(6)])


def make_result(regex, string):
    return str(re.compile(regex).findall(string))


# print(make_result(make_regex(), input()))
# pattern = re.compile(':'.join([r'[0-9A-F]{2}' for i in range(6)]))
util_5_1.test('5.1.2.input.txt', make_result, make_regex())

