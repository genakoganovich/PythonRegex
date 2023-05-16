import sys


def format_input(value):
    return f'{value} * {value} = {value * value}'


def test():
    sys.stdin = open('2.2.1.input.txt', 'r')
    count = 0
    args = []
    for line in sys.stdin:
        line = line.rstrip()
        args.append(line)
        count += 1
        if count == 2:
            count = 0
            print(format_input(int(args[0])))
            assert format_input(int(args[0])) == args[1]
            args.clear()


print(format_input(int(input())))