n, m = map(int, input().split())

def countNumber(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

fiveCount = countNumber(n, 5) - countNumber(m, 5) - countNumber(n-m, 5)
twoCount = countNumber(n, 2) - countNumber(m, 2) - countNumber(n-m, 2)

print(min(fiveCount, twoCount))