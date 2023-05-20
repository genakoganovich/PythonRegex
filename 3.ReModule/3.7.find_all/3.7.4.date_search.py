import util_3_7, re


def build_regex():
    return r'(?:[0-9]{2}/[0-9]{2}/[0-9]{4})|(?:[0-9]{2}\.[0-9]{2}\.[0-9]{4})|(?:[0-9]{4}/[0-9]{2}/[0-9]{2})|(?:[0-9]{' \
           r'4}\.[0-9]{2}\.[0-9]{2})'


# list(map(lambda x: print(x), re.findall(build_regex(), input(), 0)))
util_3_7.test('3.7.4.input.txt', build_regex)
