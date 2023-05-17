import re, sys

line_count = 0
found_flag = False

for line in sys.stdin:
    line_count += 1
    result = re.search(r'[Кк]од', line.rstrip())
    if result:
        found_flag = True
        print(f'{line_count} {result.start()}')

if not found_flag:
    print('код не найден')