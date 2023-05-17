import re

print(re.fullmatch(r'\d', '111'))  # None
print(re.fullmatch(r'\d', '1'))  # <re.Match object; span=(0, 1), match='1'>
