import re

regex = r'П.+?т'
text = 'Привет, как тебя зовут?'

# Не обращайте внимание на эту функцию, мы её разберём уже на следующем уроке
# Всё, что нужно о ней знать это то, что в результате своей работы она возвращает Match-объект
# В данном случае мы записываем Match-объект в переменную match

match = re.match(regex, text)
print(f'match = {match}')
print(f'match.group() = {match.group()}')
print(f'match.group(0) = {match.group(0)}')
print(f'match[0] = {match[0]}')
print(f'match.span() = {match.span()}')
print(f'match.span(0) = {match.span(0)}')
print(f'match.pos = {match.pos}')
print(f'match.endpos = {match.endpos}')
print(f'match.re = {match.re}')
print(f'match.string = {match.string}')
