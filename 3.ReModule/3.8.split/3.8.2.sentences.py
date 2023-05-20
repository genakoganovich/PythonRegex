import re
import util_3_8


def build_regex():
    return r'[.?!]'


# util_3_8.test('3.8.2.input.txt', build_regex)
print(re.split(build_regex(), input()))