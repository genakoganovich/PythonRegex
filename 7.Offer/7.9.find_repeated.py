import re
import util_7


def find_repeated(text):
    words = str(text).split()
    for w in words:
        length = len(re.findall(rf'(?:(?<=\s)|(?<=^)){w}(?=\s|$)', text))
        if length > 1:
            return w

    return None


print(find_repeated(input()))
# util_7.test_find_repeated('7.9.input.txt', find_repeated)


