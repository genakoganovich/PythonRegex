import re
import util_3_9


def build_regex():
    return r'[aeioyuAEIOUауоыиэяюёеАУОЫИЭЯЮЁЕ]'


# util_3_8.test('3.9.2.input.txt', build_regex)
print(re.sub(build_regex(), '!', input()))