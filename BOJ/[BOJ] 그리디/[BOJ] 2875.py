n, m, k = map(int, input().split())
res = 0

while n >= 2 and m >= 1 and n+m-3 >= k:
    n -= 2
    m -= 1
    res += 1
    
print(res)
