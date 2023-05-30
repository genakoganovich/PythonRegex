import re
import util_7

value = r'[0-9]+(?:,[0-9]+)?'
inch = r'(?: дюйм(?:а|ов))'
inch_short = r'"'
usd = r'$'
usd_to_rub = 59.5
inch_to_cm = 2.54
usd_replacement = ' руб'
inch_replacement = ' см'


def round_number(number):
    return round(number) if str(round(number, 2))[-2:] == '.0' else round(number, 2)


def localize(string):
    return re.sub(r'\.', ',', string)


def delocalize(string):
    return re.sub(',', '.', string)


def make_regex():
    return fr'(\{usd}{value})|({value}(?:{inch}|\{inch_short}))'


def make_usd_regex():
    return fr'(\{usd})|({value})'


def make_inch_regex():
    return fr'({value})|({inch})|(\{inch_short})'


def make_usd_replacement(match_obj):
    if match_obj[1]:
        return usd_replacement
    if match_obj[2]:
        return localize(str(round_number(float(delocalize(match_obj[2])) * usd_to_rub)))


def make_inch_replacement(match_obj):
    if match_obj[1]:
        return localize(str(round_number(float(delocalize(match_obj[1])) * inch_to_cm)))
    if match_obj[2] or match_obj[3]:
        return inch_replacement


def make_replacement(match_obj):
    if match_obj[1]:
        return swap_rub_value(re.sub(make_usd_regex(), make_usd_replacement, match_obj[1]))
    if match_obj[2]:
        return re.sub(make_inch_regex(), make_inch_replacement, match_obj[2])


def swap_rub_value(string):
    return ''.join(re.split(f'({usd_replacement})', string)[-1:0:-1])


def make_result(regex, make_replacement_func, string):
    return re.sub(regex, make_replacement_func, string)


print(make_result(make_regex(), make_replacement, input()))
# util_7.test('7.4.input.txt', util_7.make_result, make_regex(), make_replacement)
