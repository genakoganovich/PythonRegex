import re
import util_6_2


def make_regex():
    return r'(?i)привет'


def make_result(regex, string):
    return str(re.findall(make_regex(), string))


print(make_result(make_regex(), input()))
# util_6_2.test_hello('6.2.3.input.txt', make_result, make_regex())
