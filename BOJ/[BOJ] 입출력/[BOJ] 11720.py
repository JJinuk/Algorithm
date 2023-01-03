import sys

total = 0
n = int(sys.stdin.readline())
tc = list(sys.stdin.readline())

for i in range(n):
    total += int(tc[i])
print(total)
