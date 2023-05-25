import re
import util_4_4


replace_dict = {r'[еЕ]гонный': r'[еЕ]го', r'[еЕ]ённый': r'[еЕ]ё', r'[иИ]хний': r'[иИ]х'}
print(re.sub(r'[еЕ]гонный', r'[еЕ]го', 'Это был егонный билет.'))


def make_regex():
    return r'(\d{2}[./])(\d{2}[./])'


def make_replacement(match_obj):
    if match_obj.group(1) and match_obj.group(2):
        return fr'{match_obj.group(2)}{match_obj.group(1)}'


print(util_4_4.make_result(make_regex(), make_replacement, input()))
# util_4_4.test('4.4.5.input.txt', util_4_4.make_result, make_regex(), make_replacement)
