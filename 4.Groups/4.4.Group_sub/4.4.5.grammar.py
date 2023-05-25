import re
import util_4_4

replace_dict = {r'[еЕ]гонный': r'[еЕ]го', r'[еЕ]ённый': r'[еЕ]ё', r'[иИ]хний': r'[иИ]х'}
print(re.sub(r'[еЕ]гонный', r'[еЕ]го', 'Это был егонный билет.'))

# util_4_4.test('4.4.5.input.txt', make_result, make_found, make_regex, make_replace)
