import re


def make_regex():
    return r'(?i)o'


def make_replacement(match_obj):
    return {'o': 'x', 'O': 'X'}[match_obj[0]]


def make_result(regex, string, make_replacement_func):
    return re.sub(regex, make_replacement_func, string)


print(make_result(make_regex(), input(), make_replacement))
