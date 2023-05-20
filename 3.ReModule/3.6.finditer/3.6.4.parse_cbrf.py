import re, sys
import util_3_6


def build_regex():
    return r'[0-9,]+ ₽'


# list(map(lambda x: print(x.group()), list(re.finditer(build_regex(), input(), 0))))
util_3_6.test('3.6.4.input.txt', build_regex)