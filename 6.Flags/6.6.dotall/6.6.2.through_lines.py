import re, sys
import util_6_6


def make_regex():
    return r'(?s)(?<=start).*(?=end)'


def make_result(regex, string):
    return str(re.findall(regex, string))


print(make_result(make_regex(), ''.join(sys.stdin.readlines())))
# util_6_6.test('6.6.2.input.txt', make_result, make_regex())
