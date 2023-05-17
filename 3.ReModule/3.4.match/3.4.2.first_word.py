import re, sys

for line in sys.stdin:
    match = re.match(r'[a-zA-Z]+', line.rstrip())
    if match:
        print(f'Первое слово в предложении: {match.group()}')
