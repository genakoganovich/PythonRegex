import re


def func(m):
    return str(len(m[0]))


regex = r'[a-zA-Z]{1,}'
text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'

res_func = re.sub(regex, func, text)
res_lambda = re.sub(regex, lambda m: str(len(m[0])), text)

print(res_func)  # 5 5 2 6 5 4 2 3 8 3 11 8.
print(res_func == res_lambda)  # True
