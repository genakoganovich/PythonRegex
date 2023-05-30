import re
import util_7


def make_regex():
    vowel = '[AEIOUYaeiouy]'
    consonant = '[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz]'
    return fr'({vowel}{consonant})|({consonant}{vowel})|(?:\1)+|(?:\2)+|(?:{vowel}(?:\2)+)|(?:{consonant}(?:\1)+)'


def make_result(regex, string):
    return ' '.join(re.findall(regex, string))


# print(make_result(make_regex(), input()))
# util_7.test('7.6.input.txt', util_7.make_result, make_regex(), make_replacement)

print(re.findall(make_regex(), input()))