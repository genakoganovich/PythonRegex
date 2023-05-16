import re

print(re.search(r'\d{3}', 'abc 123 def 456 fed 321 cba'))  # <re.Match object; span=(4, 7), match='123'>
print(re.search(r'\d{3}', "abcdef"))  # None
