import re, sys

for line in sys.stdin:
    line = line.rstrip()
    full_match = re.fullmatch(r'\+?(?:[0-9]+[( )-]{0,2})+', line)
    print(bool(full_match and sum(map(lambda x: str(x).isdigit(), line)) > 10))