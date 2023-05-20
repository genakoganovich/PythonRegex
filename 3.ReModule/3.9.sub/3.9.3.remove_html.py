import re


def build_regex():
    return r'<.*?>'


print(re.sub(build_regex(), '', input()))