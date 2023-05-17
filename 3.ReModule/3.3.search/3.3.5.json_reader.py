import re, sys

for line in sys.stdin:
    result = re.search(r't=[0-9.+]+', line.rstrip())
    if result:
        print(result.group())
