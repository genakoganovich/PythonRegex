import re

result = re.sub(r'(?<!\*)\*([a-zA-Zа-яА-ЯёЁ ]+)\*(?!\*)', r'<em>\1</em>', input())
result = re.sub(r'\*\*([a-zA-Zа-яА-ЯёЁ ]+)\*\*', r'<strong>\1</strong>', result)
print(result)
