import re
import util_3_10


def build_regex():
    return r'[.?!,:]'


# util_3_10.test('3.10.2.input.txt', build_regex, '')
print(re.subn(build_regex(), '', input())[1])
