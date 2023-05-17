import re

print(re.match(r'\d{3}', 'abc 123 def 456 fed 321 cba'))
print(re.match(r'\d{3}', '123 abc 456 def 654 cba 321'))