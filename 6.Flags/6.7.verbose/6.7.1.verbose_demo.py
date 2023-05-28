import re

test1 = re.findall(r"""[1-9] +
                   .
                   \d {2,}""", '4G22', flags=re.VERBOSE)

test2 = re.findall(r"""[1-9] +
                   .
                   \d {2,}""", '4G22', flags=re.X)

test3 = re.findall(r"""(?x)
                   [1-9] +
                   .
                   \d {2,}""", '4G22')

print(test3)  # ['4G22']
print(test1 == test2 and test2 == test3)  # True
