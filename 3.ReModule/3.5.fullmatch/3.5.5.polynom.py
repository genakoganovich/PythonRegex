import re, sys

for line in sys.stdin:
    print(re.fullmatch(r'(x)?(?(1)^[0-9]+)', line.rstrip()))