import sys

n = int(sys.stdin.readline())
member = []

for _ in range(n):
    member.append(list(sys.stdin.readline().split()))
member.sort(key=lambda x: (int(x[0])))

for i in member:
    print(*i)
