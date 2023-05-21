import re
import util_3_9


def build_regex(full_name):
    last, first, middle = full_name.split()
    full = f'{last}' + r'[а-яё]{0,3} ' + f'{first[:-1]}' + r'[а-яё]{0,3} ' + f'{middle}' + r'[а-яё]{0,3}'
    initials = f'{last}' + r'[а-яё]{0,3} ' + f'{first[0]}' + r'\. ' + f'{middle[0]}' + r'\.'
    return fr'(?:{full})|(?:{initials})'


# util_3_9.test_name('3.9.4.input.txt', build_regex, 'ФИО')
# print(build_regex('Калашников Дмитрий Митрофанович'))
# list(map(lambda x: print(x), re.findall(build_regex('Калашников Дмитрий Митрофанович'), input())))
print(re.sub(build_regex(input()), 'ФИО', input()))
