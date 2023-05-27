import re
import util_4_6


def make_regex():
    return r'\b[a-z]+\b'


def make_result(regex, string, beg_pos, end_pos):
    found = re.compile(regex).search(string, beg_pos, end_pos)
    return found[0] if found else ''


# util_4_6.test_position('4.6.3.input.txt', make_result, make_regex())
print(make_result(make_regex(), input(), int(input()), int(input())))
