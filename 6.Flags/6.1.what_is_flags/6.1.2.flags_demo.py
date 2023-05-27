import re

test1 = re.findall('123', '123', flags=re.MULTILINE)  # 1 флаг
test2 = re.findall('123', '123', flags=re.MULTILINE + re.IGNORECASE)  # 2 флага
test3 = re.findall('123', '123', flags=re.MULTILINE + re.IGNORECASE + re.DOTALL)  # 3 флага

test1 = re.findall('123', '123', flags=re.MULTILINE)  # 1 флаг
test2 = re.findall('123', '123', flags=re.MULTILINE | re.IGNORECASE)  # 2 флага
test3 = re.findall('123', '123', flags=re.MULTILINE | re.IGNORECASE | re.DOTALL)  # 3 флага