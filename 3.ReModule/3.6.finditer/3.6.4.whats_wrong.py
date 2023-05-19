import re
# pattern = r"\b(\d{2},\d+)(&nbsp;)₽"
pattern = r"\b(\d{2},\d+) ₽"
# for i in re.finditer(pattern, input()):
#     print(i.group(0)[:-7], i.group(0)[-1])

print(len(list(re.finditer(pattern, input()))))