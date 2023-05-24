import re
import util_4_1


def make_regex():
    return r'(https?)://([a-z.]+)[a-z0-9-_/]+(\?[a-z=&0-9]+)*(#[a-z]+)*'


def make_result(found):
    headers = ['Полная ссылка', 'Протокол', 'Домен', 'Параметры', 'Якорь']
    result = list()
    for i in range(len(found)):
        result.append(f'{headers[0]}: {found[i].group(0)}')
        result.append(' | '.join([f'{headers[j]}: {found[i].group(j)}' for j in range(1, len(headers))]))
        if i < len(found) - 1:
            result.append('')
    return result


def make_found(build_regex_func, line):
    return list(re.finditer(build_regex_func(), line, 0))


list(map(lambda x: print(x), make_result(make_found(make_regex, input()))))
# util_4_1.test('4.1.2.input.txt', make_result, make_found)
