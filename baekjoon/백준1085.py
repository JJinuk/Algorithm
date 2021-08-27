import sys

x, y, w, h = map(int,sys.stdin.readline().rsplit())

print(min(x, y, w-x, h-y))


