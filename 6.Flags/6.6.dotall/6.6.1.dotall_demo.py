import re

string = '''
I like flags
I like flags
I like flags
'''

test1 = re.findall(r'I like flags.', string, flags=re.DOTALL)
test2 = re.findall(r'I like flags.', string, flags=re.S)
test3 = re.findall(r'(?s)I like flags.', string)

print(test1)  # ['I like flags\n', 'I like flags\n', 'I like flags\n']
print(test1 == test2 and test2 == test3)  # True
