import re, sys

for line in sys.stdin:
    match = re.match(r'(?:[a-z]+\s){11,}[a-z]+', line.rstrip())
    if match:
        print('возможно, это seed-фраза')
