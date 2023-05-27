import re


def make_regex():
    return r'(?i)o'


def make_replacement(match_obj):
    if str(match_obj[0]).islower():
        return 'x'
    else:
        return 'X'


def make_result(regex, string, make_replacement_func):
    return re.sub(regex, make_replacement_func, string)


print(make_result(make_regex(), input(), make_replacement))
