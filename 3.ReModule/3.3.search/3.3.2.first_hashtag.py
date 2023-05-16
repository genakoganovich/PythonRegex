import re

result = re.search(r'#[a-z]+', input())
if result:
    print(result.group())