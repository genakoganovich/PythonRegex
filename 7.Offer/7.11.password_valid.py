import re
import util_7


def make_result(string):
    return bool(re.search(r'(?=.*\d)', string)) \
        and bool(re.search(r'(?=.*\w)', string)) \
        and any(str(char).islower() for char in string) \
        and any(str(char).isupper() for char in string) \
        and bool(re.search(r'.{6,}', string)) and '_' not in string


print(make_result(input()))


# util_7.test_find_repeated('7.11.input.txt', make_result)


def print_short_solution():
    import regex

    pattern = r'''
    (?x)^(?=[^\W_]{6,})  # длина пароля более 6 символов
    (?=.*?\d)  # определяю наличие цифры
    (?=.*?[[:upper:]])  # определяю наличие заглавной буквы
    (?=.*?[[:lower:]])  # определяю наличие маленькой буквы
    [^\W_]+$  # записываю пароль правильными символами
    '''.strip()
    pattern = regex.compile(pattern)

    print(bool(pattern.fullmatch(input())))


print_short_solution()
