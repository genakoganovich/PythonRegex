import util_3_7_2, re


def build_regex():
    character = r'a-zA-Z0-9'
    return rf'(?:(?<=\s)|(?<=^))[{character}-_]+@[{character}]+\.[{character}]+\b'


# list(map(lambda x: print(x), re.findall(build_regex(), input(), 0)))
util_3_7_2.test('3.7.3.input.txt', build_regex)