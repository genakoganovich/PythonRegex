import re, sys
import util_6_3


def make_regex():
    return r'(?m)^[\$\^]+$'


def make_result(regex, string):
    return str(re.findall(regex, string))


# print(make_result(make_regex(), ''.join(sys.stdin.readlines())))
util_6_3.test_long_string('6.3.2.input.txt', make_result, make_regex())
