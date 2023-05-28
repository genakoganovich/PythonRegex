import re, sys
import util_6_3

text = ''.join(sys.stdin.readlines())


def make_regex():
    return r'(?m)^[\$\^]+$'


def make_result(regex, string):
    return str(re.findall(regex, string))


print(make_result(make_regex(), text))
# util_6_3.test('6.3.2.input.txt', make_result, make_regex())
