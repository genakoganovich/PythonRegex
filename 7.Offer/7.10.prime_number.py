import re, math
import util_7


def make_regex():
    return r'(?:(?<=\s)|(?<=^))x+(?=\s|$)'


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def has_prime_len(string):
    return is_prime(len(string))


def make_result(regex, string):
    return ' '.join(list(filter(has_prime_len, re.findall(regex, string))))


# print(make_result(make_regex(), input()))
util_7.test_vc('7.10.input.txt', make_result, make_regex())
