import re

regex = r'П(?P<name>.+?)т' # Захватим весь текст между П и т в группу с именем name
text = 'Привет, как тебя зовут?'

match = re.match(regex, text)
print(match)
print(match.group())
print(match.group(0)) # Можно передать номер нужной группы в метод
print(match[0])
print(match.group(1)) # Получаем то, что захватила первая группа
print(match[1])


# Ошибка: IndexError: no such group
print(match.group(2))
print(match[2])

# Выведет строку "риве":
print(match.group("name")) # Получаем то, что захватила группа с именем name
print(match["name"])       # Получаем то, что захватила группа с именем name через квадратные скобки

# Выведет кортеж ('Привет', 'риве', 'риве'):
print(match.group(0, "name", 1))