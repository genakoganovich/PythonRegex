import re
import util_7


def make_regex():
    return r'[1-9][0-9]*'


def SPQR(m):
    num = int(m[0])
    result = ''
    lst = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
           (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    for arabic, roman in lst:
        result += num // arabic * roman
        num %= arabic
    return result


make_replacement = SPQR


def make_result(regex, make_replacement_func, string):
    return re.sub(regex, make_replacement_func, string)


print(make_result(make_regex(), make_replacement, input()))
# util_7.test('7.3.input.txt', util_7.make_result, make_regex(), make_replacement)
