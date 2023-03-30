import sys

n = int(sys.stdin.readline())
x = []

for _ in range(n):
    x.append(int(sys.stdin.readline()))
for i in sorted(x):
    print(i)