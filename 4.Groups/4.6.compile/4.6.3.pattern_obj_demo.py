import re

pattern = re.compile(r'(?P<group1>[a-zA-Z]{1,})')
print(pattern.flags)  # 32
print(pattern.groups)  # 1
print(pattern.groupindex)  # {'group1': 1}
print(pattern.pattern)  # (?P<group1>[a-zA-Z]{1,})
match1 = pattern.match("Some words.", 4)  # None
match2 = pattern.match("Some words.", 5)  # words
