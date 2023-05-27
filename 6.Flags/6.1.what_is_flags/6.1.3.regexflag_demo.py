import re

pattern = re.compile(r'[a-zA-Z]{1,}')
print(pattern.flags)  # 32
print(re.RegexFlag(pattern.flags))  # re.UNICODE
