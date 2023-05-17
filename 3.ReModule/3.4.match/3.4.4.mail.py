import re, sys

for line in sys.stdin:
    match = re.match(r'[a-z0-9_.-]+(?=@)', line.rstrip())
    if match:
        print(match.group())
