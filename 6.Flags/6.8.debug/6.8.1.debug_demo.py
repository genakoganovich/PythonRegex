import re


regex = re.compile(r'I like flags', flags=re.DEBUG)

'''
Выводит следующую информацию:

LITERAL 73
LITERAL 32
LITERAL 108
LITERAL 105
LITERAL 107
LITERAL 101
LITERAL 32
LITERAL 102
LITERAL 108
LITERAL 97
LITERAL 103
LITERAL 115

 0. INFO 30 0b11 12 12 (to 31)
      prefix_skip 12
      prefix [0x49, 0x20, 0x6c, 0x69, 0x6b, 0x65, 0x20, 0x66, 0x6c, 0x61, 0x67, 0x73] ('I like flags')
      overlap [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
31: LITERAL 0x49 ('I')
33. LITERAL 0x20 (' ')
35. LITERAL 0x6c ('l')
37. LITERAL 0x69 ('i')
39. LITERAL 0x6b ('k')
41. LITERAL 0x65 ('e')
43. LITERAL 0x20 (' ')
45. LITERAL 0x66 ('f')
47. LITERAL 0x6c ('l')
49. LITERAL 0x61 ('a')
51. LITERAL 0x67 ('g')
53. LITERAL 0x73 ('s')
55. SUCCESS
'''