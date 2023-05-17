import re, sys

for line in sys.stdin:
    print(bool(re.fullmatch(r'[0-9]{13,}', line.rstrip())))
