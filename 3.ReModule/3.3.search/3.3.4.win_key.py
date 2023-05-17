import re, sys

for line in sys.stdin:
    result = re.search(r'(?<=Activation key: )(?:[0-9A-Z]{5}-){4}[0-9A-Z]{5}', line.rstrip())
    if result:
        print(result.group())
