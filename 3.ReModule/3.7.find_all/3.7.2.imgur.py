import util_3_7, re


def build_regex():
    return r'https://imgur.com/[a-zA-Z0-9]{7}'


# list(map(lambda x: print(x), re.findall(build_regex(), input(), 0)))
util_3_7.test('3.7.2.input.txt', build_regex)
