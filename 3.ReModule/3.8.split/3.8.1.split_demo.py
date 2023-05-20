import re

pattern = r'\s\d{3}\s'
string = 'abc 123 def 456 fed 321 cba'
result = re.split(pattern, string)
print(result) # ['abc', 'def', 'fed', 'cba']


pattern = r'\s\d{3}\s'
string = 'abc 123 def 456 fed 321 cba'
result = re.split(pattern, string, 2)
print(result) # ['abc', 'def', 'fed 321 cba']

pattern = r'123'
string = '456'
result = re.split(pattern, string)
print(result) # ['456']