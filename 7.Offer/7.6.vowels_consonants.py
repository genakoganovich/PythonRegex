import re
import util_7


def make_regex():
    v = '[aeiouy]'
    c = '[bcdfghjklmnpqrstvwxyz]'
    return re.compile(fr'\b({v}?(?:{c}{v})+{c}?)\b', flags=re.I)


def make_result(pattern, string):
    return ' '.join(pattern.findall(string))


# print(make_result(make_regex(), input()))
util_7.test_vc('7.6.input.txt', make_result, make_regex())
