import sys


def format_input(a, b):
    return rf'{a}\n + \n{b}\n = \n{a + b}'


def test():
    sys.stdin = open('2.3.3.input.txt', 'r')
    count = 0
    args = []
    for line in sys.stdin:
        line = line.rstrip()
        args.append(line)
        count += 1
        if count == 3:
            count = 0
            print(format_input(int(args[0]), int(args[1])))
            assert format_input(int(args[0]), int(args[1])) == args[2]
            args.clear()


print(format_input(int(input()), int(input())))