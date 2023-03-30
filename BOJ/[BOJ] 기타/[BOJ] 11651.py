import sys

n = int(sys.stdin.readline())
dots = []

for _ in range(n):
    dots.append(list(map(int, sys.stdin.readline().split())))
dots.sort(key=lambda x: (x[1], x[0]))

for i in dots:
    print(i[0], i[1])