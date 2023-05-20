import re, sys
import util_3_6_0


def build_regex():
    return r'\b[a-zA-Zа-яА-ЯёЁ]{5}\b'


# list(map(lambda x: print(x.group()), list(re.finditer(build_regex(), input(), 0))))

util_3_6_0.test('3.6.3.input.txt', build_regex)
