import re

regex = re.compile(r'[a-zA-Z]{1,}')
# Регулярное выражение скомпилировано

print(regex)  # re.compile('[a-zA-Z]{1,}')

# Теперь можно использовать методы:

print(regex.findall('Some words.'))  # ['Some', 'words']
print(regex.sub('deleted', 'Some words again.'))  # deleted deleted deleted.
