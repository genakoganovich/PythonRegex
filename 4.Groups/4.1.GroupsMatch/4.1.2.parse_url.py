import re
import util_4_1


def build_regex():
    return r'\b(https?)://([a-z.]+)([a-z0-9-_/]+)(\?[a-z=&0-9]+)?(#[a-z]+)?\b'


# util_4_1.test('4.1.1.input.txt', build_regex)
list(map(lambda x: print(x), re.findall(build_regex(), input())))

