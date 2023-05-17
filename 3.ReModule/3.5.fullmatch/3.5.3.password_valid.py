import re, sys

for line in sys.stdin:
    print(bool(re.fullmatch(r'[a-zA-Z0-9@#$%^&*()_\-+!?]{8,}', line.rstrip())))
