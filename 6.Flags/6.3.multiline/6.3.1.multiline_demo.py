import re

string = '''
I like flags
I like flags
I like flags
'''

test1 = re.findall(r'^I like flags$', string, flags=re.MULTILINE)
test2 = re.findall(r'^I like flags$', string, flags=re.M)
test3 = re.findall(r'(?m)^I like flags$', string)

print(test1)  # ['I like flags', 'I like flags', 'I like flags']
print(test1 == test2 and test2 == test3)  # True
