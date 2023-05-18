n = int(input())
p = list(map(int, input().split()))
p.sort()

res = 0
for i in range(1, n+1):
    res += sum(p[0:i])

print(res)