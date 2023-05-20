import re

pattern = r'[a-z]{3}'
replace = '111'
string = 'abc 123 def 456 fed 321 cba'
result = re.sub(pattern, replace, string)
print(result)  # 111 123 111 456 111 321 111

pattern = r'[a-z]{3}'
replace = '111'
string = 'abc 123 def 456 fed 321 cba'
result = re.sub(pattern, replace, string, 2)
print(result)  # 111 123 111 456 fed 321 cba

pattern = r'[a-z]{10}'
replace = '111'
string = 'abc 123 def 456 fed 321 cba'
result = re.sub(pattern, replace, string)
print(result)  # abc 123 def 456 fed 321 cba
