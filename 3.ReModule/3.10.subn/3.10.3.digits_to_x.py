import re
import util_3_10


def build_regex():
    return r'[0-9]'


# util_3_10.test_tuple('3.10.3.input.txt', build_regex, 'X')
print(re.subn(build_regex(), 'X', input()))
