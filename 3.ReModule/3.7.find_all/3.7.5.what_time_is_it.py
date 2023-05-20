import util_3_7, re


def build_regex():
    return r'(?:[0-1][0-9]|2[0-3]):[0-5][0-9]'


list(map(lambda x: print(x), re.findall(build_regex(), input(), 0)))
# util_3_7.test('3.7.5.input.txt', build_regex)

