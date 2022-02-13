import sys

while True:
    tc = sys.stdin.readline().rstrip('\n')

    if not tc:
        break

    l, u, d, s = 0, 0, 0, 0
    for i in tc:
        if i.islower():
            l += 1
        elif i.isupper():
            u += 1
        elif i.isdigit():
            d += 1
        elif i.isspace():
            s += 1

    print(l, u, d, s)
