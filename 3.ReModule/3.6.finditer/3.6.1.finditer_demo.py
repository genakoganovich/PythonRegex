import re

pattern = r'\d{3}'
string = 'abc 123 def 456 fed 321 cba'

result = re.finditer(pattern, string, 0)

print(len(list(result)))

print(len(list(result)))

for i in result:
    print(i.group())