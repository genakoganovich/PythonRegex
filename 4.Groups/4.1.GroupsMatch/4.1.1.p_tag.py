import re
import util_4_1


def build_regex():
    return r'<p[^<]*?>(.+?)</p>'


# util_4_1.test('4.1.1.input.txt', build_regex)
list(map(lambda x: print(x), re.findall(build_regex(), input())))

